#This program is for fun and also allow between some people talk to each others secretly
# This program is used for any message coverted into codded language and also decode 

import random
use="a b c d e f g h i j k l m n o p q r s t u v w x y z"
use = use.split(" ")
b=random.choice(use)
c=random.choice(use)
d=random.choice(use)
e=random.choice(use)
f=random.choice(use)
g=random.choice(use)
add2=e+f+g
add1=b+c+d

mess=input("Enter your message: ")
words=mess.split(" ")
coding = input("1 for Coding or 0 for Decoding ")
coding = True if (coding=="1") else False
print(coding)
if(coding):
    nwords=[]
    for word in words:
        if (len(word)>=3):
            messnew=add1 + word[1:] + word[0] + add2
            nwords.append(messnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            messnew = word[3:-3]
            messnew = messnew[-1] + messnew[:-1]
            nwords.append(messnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))



