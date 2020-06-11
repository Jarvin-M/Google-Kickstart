from itertools import combinations

def training(n,p,s):
    #N is the total number of students
    #P is the students needed for the team
    #S is an array of the skills of the ith student
    
    sorted_s = sorted(s,reverse=True) # highest to lowest
    max_s = max(s)
    number_of_hours = 0;
    if p==n:
        for elem  in sorted_s:
            training_time = max_s - elem
            number_of_hours += training_time
    elif p<n:
        subarrays = list(combinations(sorted_s,p))
        tr_times = []
        for sub in subarrays:
            max_sub = max(sub)
            sub_hours = 0
            for i in sub:
                training_time = max_sub - i
                sub_hours += training_time
                print(sub_hours)
            tr_times.append(sub_hours)
                
        number_of_hours = min(tr_times)
    return number_of_hours
    

test_cases = int(input())
for t in range(test_cases):
    n,p = list(map(int,input().split()))
    s = list(map(int,input().split()))
    print(s)
    result = training(n,p,s)
    print("Case #"+ str(t+1) + ": " + str(result))
