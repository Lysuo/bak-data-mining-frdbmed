import os

with open('procedures.txt') as f:
  content = f.readlines()


out = open("out1.txt", "w")

lloutname = [] 
lloutocc = []

for i, l in enumerate(content):
  lsplit = l.split(":")
  if not (lsplit[0] in lloutname):
    lloutname.append(lsplit[0])
    lloutocc.append(1)
  else:
    j = lloutname.index(lsplit[0])
    lloutocc[j] += 1

llout = []
for i, e in enumerate(lloutname):
  llout.append((lloutname[i], lloutocc[i]))
  out.write(lloutname[i] +" : "+ str(lloutocc[i]) + "\n")

out.close()

print llout
print len(llout)


