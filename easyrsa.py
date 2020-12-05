from Crypto.Util.number import inverse

print('On the factordb.com you can get p and q using n.\nEnter only decimal numbers.')

n = int(input('Enter n: '))
e = int(input('Enter e: '))
c = int(input('Enter c: '))
p = int(input('Enter p: '))
q = int(input('Enter q: '))

phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
res = bytearray.fromhex(str(hex(m)).split('x')[-1]).decode()
print('Flag:', rez)
