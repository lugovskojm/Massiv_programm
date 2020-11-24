while True:
	a=input ("1,2 or 3?")
	if a=="1":
		q=list(map(int, input("реверс>>").split()))
		q.reverse()
	elif a=="2":
		q=list(map(int, input("сорт>>").split()))
		q.sort()
	elif a=="3":
		q=list(map(int, input("deg>>").split()))
		q.sort()
		q.reverse()
	print(q)