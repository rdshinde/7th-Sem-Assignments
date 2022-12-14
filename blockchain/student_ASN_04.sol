// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0 ;

contract Student_management{

    struct Student{
        int stud_id;
        string Name;
        string Department;
    }
        Student [] Students;


    function addNewStudent(int stud_id, string memory Name, string memory Department) public{
        Student memory stud = Student(stud_id, Name, Department);
        Students.push(stud);
    }

    function getStudent(int stud_id) public view returns(string memory, string memory){
        for(uint256 i = 0; i < Students.length; i++){
            Student memory stud = Students[i];
                if(stud.stud_id == stud_id){
                    return (stud.Name, stud.Department);
                }
            }
        }
       
}