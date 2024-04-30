# Data Structure and Programming Spring 2024 Programming Assignment 1

## Problem Statement
This programming assignment asks you to read in a series of commands e.x. (PUSH 10, PUSH 9, POP, ......), and execute it using stack. We have written a code template for you, and you should only fill in the TODO in stack.py.
### Notice:
• For stack.py, please use python3 to run.
• You should not modify the codes which are not specified by TODO.
• You should call the class node() when storing your data structure. That is, your data structure is limited to linked lists.
• You should be able to implement push and pop operations in stack with O(1).

## Input/Output Specification
### Input Format
Inputs are a series of commands separated by newlines. The following is an example:
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/d81b84f5-2166-441a-b048-f9aed3ad6d4b)
### Output Format
You should print out your stack of each execution process. Below is an example of executing the above input using stack.
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/018dc6d9-03d8-4902-85a9-8b406912e6b0)

## Submission
Please put stack.py into a directory named studentID and compress the directory into studentID.zip. Finally, upload studentID.zip to NTU COOL.The homework is due on 3/28, at 23:59.

## Evaluation
All of our test cases will not execute pop() on an empty stack. You won’t need to handle this exception.
### Scoring Criteria:
Correctness and Time Complexity, 100% : We will evaluate your code on five test cases. We provide you three of these test cases: input 1.txt, input 2.txt, and input 3.txt, and their corresponding golden output: golden 1.txt, golden 2.txt, and golden 3.txt. We also provide a script: evaluation.sh so that you can check whether your programs pass these test cases. Furthermore, this script will display the runtime. Passing each test case with time complexity O(1) will get 20% of the total score.

## Appendix
As a reference, the python runtime of input 3.txt is around 0.0067s – 0.019s. Remember that it is a reference value and we will grade based on your code if your code runtime exceeds the range.
