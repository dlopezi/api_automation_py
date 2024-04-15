@employees @odoo_module
Feature: Employees

  Scenario: Verify all employees are returned when read all without filtering
  As a user I want to get all the employees from Odoo XML-RPC

    When I call to employee read without filter
    Then I receive the response
    And I validate the response is not empty

  @employee_id
  Scenario: Verify that an employee can be deleted using delete function
  As a user I want to delete an employee from Odoo XML-RPC

    When I call to employee delete without filter
    Then I validate the response equals than True

  Scenario: Verify that an employee can be created using create function
  As a user I want to create an employee from Odoo XML-RPC

    When I call to employee create without filter
    Then I validate the response is number

  @employee_id
  Scenario: Verify that an employee can be updated using update function
  As a user I want to update an employee from Odoo XML-RPC

    When I call to employee write without filter
    Then I validate the response equals than True
