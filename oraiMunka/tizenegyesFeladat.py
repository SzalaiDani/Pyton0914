import random

szam1 = random.randint(50,150)
szam2 = random.randint(50,150)

print("A szám 1 = "+str(szam1)+", szam 2 = "+str(szam2))

#csere
atmenet = szam1
szam1 = szam2
szam2 = atmenet

#csere2
"""
atmenet = szam2
szam2 = szam1
szam1 = atmenet
"""

print("szam 1="+str(szam1)+", szam 2="+str(szam2))