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
