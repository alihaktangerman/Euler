from sympy import binomial

tar = int(2e6)

x, y = 2001, 2

ans = x, y

while x>=y:
	y += 1
	x, z = x+1, x
	while abs(binomial(z, 2)*binomial(y, 2) - tar) < abs(binomial(x, 2)*binomial(y, 2) - tar):
		x, z = z, z-1
	errnew = abs(binomial(x, 2)*binomial(y, 2) - tar)
	errold =  abs(binomial(ans[0], 2)*binomial(ans[1], 2) - tar)
	if errnew < errold:
		ans = x, y

print((ans[0]-1)*(ans[1]-1))
