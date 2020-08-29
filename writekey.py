from random import randint

stkey1=[]
stkey2=[]

for i in range(16):
  key=[]
  for j in range(32):
    key.append(randint(0,1))
  stkey1.append(key)

for i in range(16):
  key=[]
  for j in range(32):
    key.append(randint(0,1))
  stkey2.append(key)


print(stkey1[0])
print(stkey2[0])

f= open("key1.txt","w+")
for i in range(16):
  key=stkey1[i]
  string=''
  for j in range(32):
    string=string+str(key[j])
  string=string+'\n'
  f.write(string)

f.close()

f= open("key2.txt","w+")
for i in range(16):
  key=stkey2[i]
  string=''
  for j in range(32):
    string=string+str(key[j])
  string=string+'\n'
  f.write(string)

f.close()
