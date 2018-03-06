//chuyen day byte dang str -> hex str, sau do copy ket qua vao ham duoi
string_byte =  '1F 08 13 13 04'
split_str = string_byte.split()
return_str = ''
for i in split_str:
	return_str += '0x' + i + ','
print(return_str)


//thao tac voi day byte tren
byte_arr = bytes([return_str])
