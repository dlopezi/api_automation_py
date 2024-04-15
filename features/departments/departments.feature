@departments @odoo_module
Feature: Departments

  Scenario: Verify all departments are returned when read all without filtering
  As a user I want to get all the departments from Odoo XML-RPC

    When I call to department read without filter
    Then I receive the response
    And I validate the response is not empty

  @department_id
  Scenario: Verify that a department can be deleted using delete function
  As a user I want to delete a department from Odoo XML-RPC

    When I call to department delete without filter
    Then I validate the response equals than True
    
  Scenario: Verify that an department can be created using create function
  As a user I want to create an department from Odoo XML-RPC

    When I call to department create without filter
    Then I validate the response is number

  @department_id
  Scenario: Verify that a department can be updated using update function
  As a user I want to update a department from Odoo XML-RPC

    When I call to department write without filter
    Then I validate the response equals than True