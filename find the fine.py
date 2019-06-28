"""Given an array of penalties P, an array of car numbers C, and also the date D. The task is to find the total fine which will be collected on the given date. Fine is collected from odd-numbered cars on even dates and vice versa.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of three lines of input. First line of each test case contains two integers N & D, second line contains N space separated car numbers C and third line contains N space separated penalties P.

Output:
For each test case,In new line print the total fine.

Constraints:
1 <= T <= 100
1 <= N <= 105
1000 <= Ci <= 9999
1 <= D <= 31
1 <= Pi <= 103
Example:
Input:
2
4 12
2375 7682 2325 2352
250 500 350 200
3 8
2222 2223 2224
200 300 400
Output:
600
300
"""

for i in range(t):
	n,s=map(int,input().split())
	p=input().split()
	v=input().split()
	k=0
	
	for i in range(n):
		l=int(v[i])
		if(s%2!=0 and int(p[i])%2==0):
			k+=l
		elif(s%2==0 and int(p[i])%2!=0):
			k+=l
	print(k)
