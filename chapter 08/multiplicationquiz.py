import pyinputplus as pyip
import random, time

rightanswers = 0
for q in range(10):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    
    ques = '%s: %s x %s = ' % (q, a, b)
    
    try:
       pyip.inputStr(ques, allowRegexes=['^%s$' % (a * b)],  blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    
    else:
        print("nice one")
        rightanswers += 1
    
    time.sleep(1)
print("you got", rightanswers, "answers correct")
                              
                            
    