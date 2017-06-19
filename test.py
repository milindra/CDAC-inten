import unittest
from SSSA import sssa

values = ["76", "5","33"]
minimum = [2, 1, 1]
shares = [3,3, 3]

sss = sssa()

for index,value in enumerate(values):
    print (index)
    s=sss.create(minimum[index], shares[index], value)
    print (s)
    print (s[0])
    k=[s[0],s[1]]
    print (sss.combine(k))
