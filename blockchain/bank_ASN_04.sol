// SPDX-License-Identifier: MIT

//Write a smart contract on a test network for bank account of the customer for following operations.
// #1. Deposite Money
// #2. Withdraw Money
// #3. Show Money

pragma solidity ^0.8;

contract bank{
    mapping (uint256 => uint256) BankUsers;
    
    uint256 public userCount  = 0;

    function addNewUser(uint256 openingBalance) public returns(uint256, uint256){
        userCount++;
        BankUsers[userCount] = openingBalance;
        return (userCount, openingBalance);
    } 

    function depositMoney(uint256 userId, uint256 moneyToAdd) public returns(uint256, uint256){
        BankUsers[userId] = BankUsers[userId] + moneyToAdd;
        return (userCount, BankUsers[userId]);
    }

    function withdrawMoney(uint256 userId, uint256 moneyToWithdraw) public returns(uint256, uint256){
        require(BankUsers[userId] > moneyToWithdraw, "Insufficient balance.");
        BankUsers[userId] = BankUsers[userId] - moneyToWithdraw;
        return (userCount, BankUsers[userId]);
    }

    function getUserBalance(uint256 userId) public view returns(uint256, uint256){
        return(userId, BankUsers[userId]);
    }
    
}