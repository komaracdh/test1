users=[]
passwords=[]
role=[]
def readingUser():
    for line in open('users.txt','r').readlines():
        line2 = line.strip().split('|')
        users.append(line2[0])
        passwords.append(line2[1])
        role.append(line2[6])

readingUser()
"""print(role)
print(users)
print(passwords)"""
  

