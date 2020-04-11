


import time

def remove_same(name1,name2):
    ret = ['','',0]
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i]==name2[j]:
                temp=name2[j]
                name1.remove(temp)
                name2.remove(temp)
                ret[0]=name1
                ret[1]=name2
                ret[2]=1
                return ret
    ret[0]=name1
    ret[1]=name2
    return ret
    

print("WELCOME TO FLAMES!!!")
print("""
             Friends
             Love
             Affection
             Marriage
             Enemy
             Siblings

             """)
time.sleep(2)
name1 = input("Enter name of first person: ")
name1 = name1.lower()
name1 = list(name1)

name2 = input("Enter name of second person: ")
name2 = name2.lower()
name2 = list(name2)

rec = []
k = 1
while k:
    
    rec = remove_same(name1,name2)
    k = rec[2]

len1 = len(rec[0])
#print(len1)
len2 = len(rec[1])
#print(len2)
len_final=len1+len2

flames = ["Friends","Love","Affection","Marriage","Enemy","Siblings"]

while len(flames) > 1:
    pos = (len_final % len(flames))
    if pos>=1:
        r = flames[pos:]
        l = flames[:pos-1]
        flames = r+l
    else :
        flames = flames[:len(flames)-1]
    

print("Relationship Status : ",flames[0])
time.sleep(3)
