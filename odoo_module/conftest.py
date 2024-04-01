import pytest

from entities.entities import OdooEntity


@pytest.fixture()
def create_employee():
    new_employee = [{'name': "New Employee from fixture"}]
    entity = OdooEntity("hr.employee")

    employee_id = entity.create(new_employee)

    yield employee_id

    entity.delete(employee_id)


@pytest.fixture()
def create_department():
    new_department = [{'name': "New Department from fixture"}]
    entity = OdooEntity("hr.department")

    department_id = entity.create(new_department)

    yield department_id

    entity.delete(department_id)


@pytest.fixture()
def create_job_position():
    new_job_position = [{'name': "New Job Position from fixture"}]
    entity = OdooEntity("hr.job")

    job_position_id = entity.create(new_job_position)

    yield job_position_id

    entity.delete(job_position_id)