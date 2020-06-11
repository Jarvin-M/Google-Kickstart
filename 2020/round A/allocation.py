from itertools import combinations
"""
Parameters:
    N houses
    ith house costs A_i dollars
    B - Budget
Input:
    T - number of test cases ()
    Tt - test cases first line has first 2 intergers N and B
    second line contains N integers of the costs of the houses A_i

Output:
    Cases #x:y where x is the test case and y - maximum number of houses you can buy
"""
def allocation(N,B,A):
    max = 0
    for x in range(1,len(A)):
        possible_combinations = list(combinations(A,x))
        for pc in possible_combinations:
            if sum(pc) <= B and max < len(pc):
                max = len(pc)
    return max


n_test_cases = int(input())
for t in range(n_test_cases):#iterate through the test cases
    N,B = list(map(int,input().split()))
    A = list(map(int,input().split()))
    print(N)
    result = allocation(N,B,A)
    print("Case #"+ str(t+1) + ": " + str(result))