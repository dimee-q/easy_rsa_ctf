from Crypto.Util.number import inverse


print("On the alpertron.com.ar/ECM.HTM you can get p and q using n.\n"
      "Enter only decimal numbers.")

n = int(input('Enter n: '))
e = int(input('Enter e: '))
c = int(input('Enter c: '))
p = int(input('Enter p: '))
q = int(input('Enter q: '))

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
try:
    res = bytearray.fromhex(str(hex(m)).split('x')[-1]).decode()
    print('Flag:', res)
except Exception:
    print('Invalid data, please check your input. Enter only decimal numbers.')
