def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valley = 0
    for i in range(steps):
        if path[i] == 'D':
            altitude -=1
        if path[i] == 'U':
            altitude+=1
        if path[i] == 'U' and altitude == 0:
            valley+=1
    return valley