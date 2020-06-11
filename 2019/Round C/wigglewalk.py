def move(R,C,sR,sC,instruct):
    if sR <= R and sC <= C:
        if instruct == 'E':
            #east
            sC += 1
        elif instruct == 'W':
            #west
            sC -= 1
        elif instruct == 'N':
            #north
            sR -= 1
        elif instruct == 'S':
            #south
            sR += 1
        
    return (sR,sC)

T = int(input())
for ts in range(T):
    testcase = list(map(int, input().split())) #array of inputs
    N,R,C,sR, sC = testcase[0], testcase[1], testcase[2], testcase[3], testcase[4]
    # iterate through the instructions
    instructions = input()
    
    pointsTraversed = []
    pointsTraversed.append((sR,sC)) # append starting point
    
    for i in range(0,N):
        instruct = instructions[i]
        sR,sC = move(R,C,sR,sC,instruct)
        while (sR,sC) in pointsTraversed:
            sR,sC  = move(R,C,sR,sC, instruct)
            
        pointsTraversed.append((sR,sC)) #add current position
    result = [str(i) for i in pointsTraversed[-1]]

    print("Case #" + str(ts+1) +" " + ' '.join(result))