def robotstep(stepno):
    robotstep = stepno
    steptakebyrobo = [5,4,3,2,1]
    new = []
    for step in steptakebyrobo:
        if robotstep != 0:
            if robotstep // step:
                new.append(robotstep // step)
                robotstep %= step
        else:
            break
    return sum(new)             
print(robotstep(18))
            
            