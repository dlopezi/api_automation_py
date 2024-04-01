import pytest

from odoo_module.odoo_test import OdooTest


@pytest.mark.job_position
class JobPositionTest(OdooTest):
    model = "hr.job"

    def test_read_job_position(self, create_job_position):
        job_position = self.entity.read(create_job_position)
        assert job_position, "Failed to read work location"

    def test_create_job_position(self):
        new_job_position = [{'name': "New Job Position"}]
        new_record_id = self.entity.create(new_job_position)

        self.to_delete.append(new_record_id)

        assert new_record_id > 0, "Failed to create work location"

    def test_update_job_position(self, create_job_position):
        updated_job_position = {'name': "Updated Job Position"}
        result = self.entity.write(create_job_position, updated_job_position)

        assert result, "Failed to update work location"

    def test_delete_job_position(self):
        new_job_position = [{'name': "New Job Position"}]
        new_record_id = self.entity.create(new_job_position)

        result = self.entity.delete(new_record_id)

        assert result, "Failed to delete work location"
