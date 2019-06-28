"""Given an unsorted array arr[] of size N, rotate it by D elements (clockwise). 

Input:
The first line of the input contains T denoting the number of testcases. First line of eacg test case contains two space separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent line will be the N space separated array elements.

Output:
For each testcase, in a new line, output the rotated array.

Constraints:
1 <= T <= 200
1 <= N <= 107
1 <= D <= N
0 <= arr[i] <= 105

Example:
Input:
2
5 2
1 2 3 4 5 
10 3
2 4 6 8 10 12 14 16 18 20

Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
"""

for i in range(t):
    s=input().split()
    p=input().split()
    v=int(s[1])
    l1=[]
    l2=[]
    if (v<=len(p)):
        for j in range(v):
            l1.append(p[j])
    for k in range(v,len(p)):
        l2.append(p[k])
    l2.extend(l1)
    print(" ".join(l2))
    l1.clear()
    l2.clear()
