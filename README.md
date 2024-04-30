# Data Structure and Programming, Spring 2024 Programming Assignment #3
## Problem Description:
In this homework, you’re going to implement a binary search tree by yourself. Your BSTree needs to have the following functions: insert(), delete(), find max(), find min(), inorder(), preorder(), postorder(), level(), leafnode(), internalnode().
There are more detailed descriptions of the functions.
### insert()
The function follows the rule of the standard binary search tree. The key in each node must be greater than any key stored in the left sub-tree, and less than any key stored in the right sub-tree.
### delete()
The function removes a node whose key equals the input value. Please maintain the properties of binary search tree after doing delete() operation. If the given key value is not in the current tree, don’t modify the tree. (If there are two children, replacing the node’s value with its smallest value in the right sub-tree)
### find max()
The function finds the maximum value in the current binary search tree.
### find min()
The function finds the minimum value in the current binary search tree.
### inorder()
Print the current tree in the inorder traversal sequence. You should use space(’ ’) to separate the key of each node, and the output should end up with a newline character.
### preorder()
Print the current tree in the preorder traversal sequence. You should use space(’ ’) to separate the key of each node, and the output should end up with a newline character.
### postorder()
Print the current tree in the postorder traversal sequence. You should use space(’ ’) to separate the key of each node, and the output should end up with a newline character.
### level()
Print the height of the current tree. (The height of the leaf node is 0)
### leafnode()
Print all leaf nodes of the current tree from the leftmost one to the rightmost one. You should use space(’ ’) to separate the key of each node, and the output should end up with a newline character.
### internalnode()
Print all internal nodes of the current tree from the smallest one to the largest one. You should use space(’ ’) to separate the key of each node, and the output should end up with a newline character.

## Evaluation
We have provided a code file BSTree.py. You have to fill in the class BSTree.py which is used for testing. Write your codes in TODO.
1. Do not modify the interface of the functions, but you can add your own functions.
2. Binary search tree is not always balanced.
3. Use command ”python BSTree.py --input input1.txt --output output1.txt” to check your output. Use command ”bash evaluation.sh” to check result (just as P1).

## Grading policy
This programming assignment will be graded based on correctness. We have 8 test cases in total, and we provide you three of these test cases: input 1.txt, input 2.txt, input 3.txt, and their corresponding golden output: golden 1.txt, golden 2.txt, golden 3.txt. We also provide a script: evaluation.sh, so that you can check whether your program passes these three test cases. We have 5 hidden test cases. The size of hidden test cases is much the same as the size of public test cases, but we may test your code by using an unbalanced binary search tree. If your program can pass one of the public test cases, you will get 10% each. If your program can pass one of the private test cases, you will get 14% each. The total point is 10 ∗ 3 + 14 ∗ 5 = 100.

## Submission
Please put your codes (including BSTree.py or any other code files) into a directory named studentID and compress the directory into studentID.zip to NTUCOOL. The homework is due on 05/09, at 23:59
