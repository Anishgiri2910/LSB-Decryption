from PIL import Image
import binascii
#Changing binary 
def int2bytes(i):
	hex_string ='%x'%i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
	n = int(bits, 2)
	return int2bytes(n).decode(encoding, errors)	
def find(img):
	header, trailer = 2*"11001100",2*"0101010100000000"
	pixels, mode = list(img.getdata()), img.mode
	payload = []
	bits=[]
	oldPixels=[]
	for i in range (len(pixels)):
		oldPixels.append(bin(pixels[i][i%len(mode)]))
	for j in range (len(oldPixels)):
		bits.append(oldPixels[j][-1])
	bit=''.join(bits)
	bit=bit.split(trailer)
	bit=bit[0].split(header)
	return text_from_bits(bit[1])

if __name__=="__main__":
	img=Image.open("Secret.png")
	print find(img)
