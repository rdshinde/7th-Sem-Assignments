// SPDX-License-Identifier: MIT

//Write a smart contract on a test network for bank account of the customer for following operations.
// #1. Deposite Money
// #2. Withdraw Money
// #3. Show Money

pragma solidity ^0.8;

contract bank{
    mapping (string => uint256) BankUsers;
    
    function addNewUser(string memory userName, uint256 openingBalance) public returns(string memory, uint256){
        BankUsers[userName] = openingBalance;
        return (userName, openingBalance);
    } 

    function depositMoney(string memory userName, uint256 moneyToAdd) public returns(string memory, uint256){
        BankUsers[userName] = BankUsers[userName] + moneyToAdd;
        return (userName, BankUsers[userName]);
    }

    function withdrawMoney(string memory userName, uint256 moneyToWithdraw) public returns(string memory, uint256){
        require(BankUsers[userName] > moneyToWithdraw, "Insufficient balance.");
        BankUsers[userName] = BankUsers[userName] - moneyToWithdraw;
        return (userName, BankUsers[userName]);
    }

    function getUserBalance(string memory userName) public view returns(string memory, uint256){
        return(userName, BankUsers[userName]);
    }
    
}