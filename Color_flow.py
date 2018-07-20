import os 

# Doi mau cac dong trong ida dua tren log flows

path = 'C:\\Users\\lu\\Downloads\\trace.txt'
color = 0xffff00

fi = open(path,'r')

for line in fi:
	addr_str = '0x' + line
	addr = int(addr_str, 16)
	SetColor(addr, CIC_ITEM, color)

fi.close()
