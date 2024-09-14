import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

#műveletek
osszeg = szam1 + szam2
kulonbseg = szam1 - szam2
szorzat = szam1 * szam2
hanyados = szam1 / szam2
maradek = szam1 % szam2
hatvany = szam1 ** szam2

#kiíratás
print (str(int(szam1))+" + "+str(int(szam2))+" = "+str(int(osszeg)))
print (str(int(szam1))+" - "+str(int(szam2))+" = "+str(int(kulonbseg)))
print (str(int(szam1))+" * "+str(int(szam2))+" = "+str(int(szorzat)))
print (str(int(szam1))+" / "+str(int(szam2))+" = "+str(int(hanyados)))
print (str(int(szam1))+" % "+str(int(szam2))+" = "+str(int(maradek)))
print (str(int(szam1))+" ** "+str(int(szam2))+" = "+str(int(hatvany)))