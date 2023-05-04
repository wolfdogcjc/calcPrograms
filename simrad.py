# Simplifying radicals

import math

rad1 = int(input("What is the radical you want to simplify?  √"))
workrad1 = rad1
sqrnum = 1

for i in range(2,rad1):
  mexp = 1
#  print(i)
  while i**mexp<=workrad1:
    if workrad1 % i**mexp == 0:
      mexp = mexp+1
    else:
      break
  if mexp > 2:
    sqrfac = i**(int((mexp-1)/2))
    sqrnum = sqrnum * sqrfac
    workrad1 = workrad1/(sqrfac**2)
    
outsidenum = int(sqrnum)
insidenum = int(rad1/(sqrnum**2))
print(" ")
print("The square root of "+str(rad1)+" is"),
if insidenum == 1:
  print(outsidenum)
else:
  if outsidenum == 1:
    print("√"+str(insidenum))
  else:
    print(str(outsidenum)+"√"+str(insidenum))
  

    
    