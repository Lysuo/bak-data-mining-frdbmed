import os
import re

with open('effets_notoires.csv') as f:
  content = f.readlines()
#  content[0] = content[0][3:]

def rewriteEffets():
  out1 = open("out_effets.csv", "w")
  out2 = open("out_effets_ind.csv", "w")

  outL = []
  outLL = []
  lasti = -1

  for e in content:
    l = e[0:-2].split(",")
    if len(l[0]) < 1 or len(l[1]) < 1:
      if len(l[0]) > 1:
        outL[lasti] += l[0]
    else:
      outL.append(",".join(l))
      lasti += 1

  for i,e in enumerate(outL):
    out1.write(e)
    out1.write("\n")
    l = e.split(",")
    if not l[2] in outLL:
      outLL.append(l[2])

  for i,e in enumerate(outLL):
    out2.write(e)
    out2.write("\n")

  out1.close()
  out2.close()

if __name__ == "__main__":
  rewriteEffets()
