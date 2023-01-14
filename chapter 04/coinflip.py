import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    flip100 = []
    for i in range(1,101):
        flip = random.randint(0,1)
        flip100.append(flip)
    
    streak = 0
    for i in range(100):
        if flip100[i:i+6] == [0,0,0,0,0,0] or flip100[i:i+6] == [1,1,1,1,1,1]:
            streak += 1
        if streak == 6:
            numberOfStreaks+=1
            
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))