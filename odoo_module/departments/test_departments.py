import pytest

from odoo_module.odoo_test import OdooTest


@pytest.mark.department
class DepartmentTest(OdooTest):
    model = "hr.department"

    def test_read_department(self, create_department):

        department = self.entity.read(create_department)

        assert department, "Failed to read department"

    def test_create_department(self):
        new_department = [{'name': "New Department"}]
        new_record_id = self.entity.create(new_department)

        self.to_delete.append(new_record_id)

        assert new_record_id > 0, "Failed to create department"

    def test_update_department(self, create_department):

        updated_department = {'name': "Updated Department"}
        result = self.entity.write(create_department, updated_department)

        assert result, "Failed to update department"

    def test_delete_department(self):
        new_department = [{'name': "New Department"}]
        new_record_id = self.entity.create(new_department)

        result = self.entity.delete(new_record_id)

        assert result, "Failed to delete department"
