from entities.entities import OdooEntity
from utils.logger import get_logger


logger = get_logger(__name__)

FEATURE_MODEL_DICT = {
    "Employees": "hr.employee",
    "Job Positions": "hr.job",
    "Departments": "hr.department"
}


def before_all(context):
    logger.debug("Before all")
    context.to_delete = []
    context.record_id = None


def before_feature(context, feature):
    logger.debug("Before Feature")
    logger.debug("Feature tags: %s", feature.tags)
    model = FEATURE_MODEL_DICT.get(feature.name)
    if model:
        context.entity = OdooEntity(model)
    else:
        logger.warn("Model no found for feature '%s'", feature.name)


def before_scenario(context, scenario):
    logger.debug("Before Scenario")
    logger.debug("Scenario tags: %s", scenario.tags)
    logger.debug("Scenario Name: %s", scenario.name)

    if "employee_id" in scenario.tags:
        new_employee = [{'name': "New Employee from feature"}]
        context.record_id = context.entity.create(new_employee)
    elif "department_id" in scenario.tags:
        new_department = [{'name': "New Department from feature"}]
        context.record_id = context.entity.create(new_department)


def after_scenario(context, scenario):
    logger.debug("After Scenario")
    context.record_id = None


def after_feature(context, feature):
    logger.debug("After Feature")
    context.entity.delete(context.to_delete)
    context.to_delete = []


def after_all(context):
    logger.debug("After all")
