def f(x):
	return{
	0: "00\n",
	1: "11\n",
	2: "22\n"
	}.get(x, "need 0, 1 or 2\n")

if __name__ == '__main__':
	print f(11)