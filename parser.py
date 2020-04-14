global d
global count
count = 0
d = {}


def sym(c):
	global count
	global d
	start = count+1
	end = count+2
	count += 2
	
	d[start] = [(end, 1.0, c)]
	d[end] = []

	return (start, end)


def conc(nfa1, nfa2):
	global d	

	(start1, end1) = nfa1
	(start2, end2) = nfa2

	d[end1] = [(start2, 1.0, "epsilon")]

	return (start1, end2)


def choice(p, nfa1, nfa2):
	if (p < 0.0) or (p > 1.0):
		print("The probability must be between 0.0 and 1.0.")
		return False
	
	global count	
	count += 1

	(start1, end1) = nfa1
	(start2, end2) = nfa2

	d[count] = [(start1, p, "epsilon"), (start2, 1-p, "epsilon")]

	count += 1
	d[end1] = [(count, 1.0, "epsilon")]
	d[end2] = [(count, 1.0, "epsilon")]
	d[count] = []

	return (count-1, count)


def star(p, nfa):
	if (p < 0.0) or (p > 1.0):
		print("The probability must be between 0.0 and 1.0.")
		return False

	global count	
	count += 1

	(start, end) = nfa
	d[end] = [(count, 1.0, "epsilon")]
	d[count] = [(start, 1-p, "epsilon"), (count+1, p, "epsilon")]
	count += 1
	d[count] = []

	return (count-1, count)




