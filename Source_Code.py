string=[x for x in input()]
counting=string.count('0')
for i in range(len(string)):
    for j in range(1,len(string)):
        if(len(string[i:j+1])>1):
            if(string[i:j+1][0]!='1'):
                if(string[i:j+1][0]==string[i:j+1][-1]):
                    counting=counting+1
print(counting)
