// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Bank2 {
    address public owner;       // Account owner address
    uint256 private balance;    // Store account balance
// Constructor runs only once when deployed
    constructor() {
        owner = msg.sender;
        balance = 0;
    }
// Deposit Ether into contract
    function deposit() public payable {
        balance += msg.value;   // msg.value is amount sent (in wei)
    }
// Withdraw Ether from contract
    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount <= balance, "Insufficient funds");
        balance -= amount;
        payable(owner).transfer(amount);
    }
// View current balance (in Ether)
    function getBalance() public view returns (uint256) {
        return balance;
    }
// Fallback function (if Ether is sent without calling deposit)
    receive() external payable {
        balance += msg.value;
    }
}
