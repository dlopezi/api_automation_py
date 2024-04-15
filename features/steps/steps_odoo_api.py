from behave import when, then
from utils.logger import get_logger

logger = get_logger(__name__)


@when("I call to {model} {function_name} without filter")
def call_func_of_model(context, model, function_name):
    logger.info("Calling '%s' function for '%s' model", function_name, model)
    func = getattr(context.entity, function_name)
    if func:
        if function_name == "delete":
            context.response = func(context.record_id)
        elif function_name == "read":
            context.response = func()
        elif function_name == "create":
            new_entity = [{'name': "New %s".format(model)}]
            context.response = func(new_entity)
            context.entity.delete(context.response)
        elif function_name == "write":
            new_entity = {'name': "Updated %s".format(model)}
            context.response = func(context.record_id, new_entity)
            context.entity.delete(context.record_id)
    else:
        context.response = None


@then('I receive the response')
def validate_response_is_not_none(context):
    assert context.response is not None


@then('I validate the response is not empty')
def validate_response_is_not_empty(context):
    assert isinstance(context.response, list)
    assert len(context.response) > 0


@then('I validate the response equals than {expected}')
def validate_response_is_boolean(context, expected):
    assert isinstance(context.response, bool)
    assert context.response is bool(expected)


@then('I validate the response is number')
def validate_response_is_number(context):
    assert isinstance(context.response, int)
