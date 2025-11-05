// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EmployeeData {
    // Structure to hold employee details
    struct Employee {
        uint id;
        string name;
        uint salary;
        string joiningDate;
    }

    // Array to store multiple employees
    Employee[] public employees;

    // Add a new employee
    function addEmployee(
        uint _id,
        string memory _name,
        uint _salary,
        string memory _joiningDate
    ) public {
        employees.push(Employee(_id, _name, _salary, _joiningDate));
    }

    // Get employee details by index
    function getEmployee(uint index)
        public
        view
        returns (uint, string memory, uint, string memory)
    {
        Employee memory e = employees[index];
        return (e.id, e.name, e.salary, e.joiningDate);
    }

    // Get total number of employees
    function getEmployeeCount() public view returns (uint) {
        return employees.length;
    }
}
