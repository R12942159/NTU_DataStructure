# Data Structure and Programming, Spring 2024 programming assignment #2

## Problem Description
Given an m × n grid graph, the cost of each graph edge (u, v) is d(u, v), a source grid is S, and a target grid is T (see Figure 1(a)). Let D(S, g) denote the minimum cost of a non-detour path from S to a grid g. Please write a program that finds a monotonic path from the source grid to the target grid, i.e., compute D(S, T), and reports the total edge cost, the number of grids, and the grid coordinates of the path.
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/8b014df3-afc6-422f-a965-8ca1499789fc)
### Notice:
1. Please use python3 to run your program.
2. Monotonic means that you can only go up or right, and you can’t go back (left or below).

## Input/Output Specification
### Input format
The file format for the monotonic routing is illustrated, with comments in italics (these will not be in actual input files). The 1st line gives the problem size in terms of the indices of the left-bottom and the right-top grids (the indices of the left-bottom grid will always be (0,0)). Each edge connecting two grids has either default cost or non-default cost. The default cost is given in the 2nd line. The 3rd line gives the number of edges that have non-default costs. Start from the 4th line, the cost difference compared to the default cost of each non-default edge is separately given. For example, if the default cost is 3, then 2 3 2 4 1 means the cost from (2, 3) to (2, 4) is 1 + 3 = 4 . Additionally, if the cost difference is denoted by ’x’, it signifies that the edge is not traversable, i.e, cost = ∞. For instance, 2 3 2 4 x indicates that there is no viable path from (2, 3) to (2, 4). Finally, the coordinates of the source and the target grids are listed in the last two lines.
The input file format is as follows:
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/9ce86f06-dd13-47de-90a8-726fe6b86bc9)
### output format
The resulting monotonic path needs to be described in the output file. The 1st line gives the total edge cost in the resulting path, and the 2nd line gives the number of grids on the path. After that, the consecutive grids in the path from source to target have to be listed in order.
The output file format is as follows:
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/141f312d-92b3-4e7d-bb34-0cdec090b224)
### Notice:
1. x1 and y1 must be the same as xS and yS, and xk and yk must be the same as xT and yT in the input file, respectively.
2. There is no need to consider cases where there is no viable path from S to T.
Here is an input/output example of Figures 1(b)/(c):
![image](https://github.com/R12942159/NTU_DataStructure/assets/145434739/0416fec9-eedf-4799-a907-48bac7b809c7)

## Command-line parameter
In order to test your program, please add the following command-line parameters to your program (e.g., python mono.py –input 5x5.in –output 5x5.out).

## Submission
Please put mono.py and readme.txt into a directory named studentID and compress the directory into studentID.zip. Finally, upload studentID.zip to NTU Cool. The homework is due on 4/18, at 23:59.

## Grading policy
This programming assignment will be graded based on (1) the correctness (2) solution quality, and (3) running time. Please check these items before your submission. We provide you three test data: 5x5.in, 50x50.in, 500x500.in, and we will score your program by two private data. If the output format, the number of grids on the path and the consecutive grids in the path from source to target are right, you will get 10% each private data. If the time of executing your algorithm is within the time limit, you will get 20% each private data. The remaining score depends on your solution quality. We will sort all the routing cost and give score from the least routing cost to the largest routing cost.
### Notice: 
If the time of executing your algorithm exceeds the time limit, we’ll stop the execution, and you will get 0% on this item. (Brute-Force method will definitely exceed the time limit.)
