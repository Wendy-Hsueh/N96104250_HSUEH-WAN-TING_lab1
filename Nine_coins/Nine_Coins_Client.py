from nine_coins import Nine_Coins
intnum = int(input('Input DECCIMAL:'))
c = Nine_Coins(intnum)
#補足位數
s = "%09d" % int(c.deccimalTObinary(intnum))
c.convertTOht(s)
print()
print('binary:', s, 'and decimal:', intnum)
c.toss()
