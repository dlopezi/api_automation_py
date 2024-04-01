import pytest

from odoo_module.odoo_test import OdooTest


@pytest.mark.employee
class EmployeeTest(OdooTest):
    model = "hr.employee"

    def test_read_employee(self, create_employee):

        employee = self.entity.read(create_employee)

        assert employee, "Failed to read employee"

    def test_create_employee(self):
        new_employee = [{'name': "New Employee"}]
        new_record_id = self.entity.create(new_employee)

        self.to_delete.append(new_record_id)

        assert new_record_id > 0, "Failed to create employee"

    def test_update_employee(self, create_employee):

        updated_employee = {'name': "Updated Employee"}
        result = self.entity.write(create_employee, updated_employee)

        assert result, "Failed to update employee"

    def test_delete_employee(self):
        new_employee = [{'name': "New Employee"}]
        new_record_id = self.entity.create(new_employee)

        result = self.entity.delete(new_record_id)

        assert result, "Failed to delete employee"
