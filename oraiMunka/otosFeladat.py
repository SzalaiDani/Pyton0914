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
print("A két szám összege: "+str(osszeg))
print("A két szám különbsége: "+str(kulonbseg))
print("A két szám szorzata: "+str(szorzat))
print("A két szám hanyada: "+str(hanyados))
print("A két szám maradéka: "+str(maradek))
print("A két szám hatványa: "+str(hatvany))