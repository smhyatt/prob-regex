import generator as g
import parser as ps

print("_________________________________________________________________")
print("\n Testing semantics  that generates sequences of random strings.")
print("_________________________________________________________________")

# RegEx: (a |0.4 ab)*0.3
ran_test1 = ps.star(0.3, ps.choice(0.4, ps.sym('a'), 
				ps.conc(ps.sym('a'), ps.sym('b'))))

# RegEx: PLD is (fun |0.55 hard)
ran_test2 = ps.conc(ps.conc(ps.sym('P'), ps.conc(ps.sym('L'), 
	ps.conc(ps.sym('D'), ps.conc(ps.sym(' '),
	ps.conc(ps.sym('i'), ps.conc(ps.sym('s'), ps.sym(' ')) ))))), 
	ps.choice(0.55, ps.conc(ps.sym('f'), ps.conc(ps.sym('u'), ps.sym('n'))), 
	ps.conc( ps.sym('h'), ps.conc(ps.sym('a'), ps.conc(ps.sym('r'), ps.sym('d'))))))

# RegEx: (H((i)*0.7 |0.7 (ey |0.3 ello)))*0.1
ran_test3 = ps.star(0.1, ps.choice(0.7, ps.conc(ps.conc(ps.sym(' '), ps.sym('H')), 
	ps.star(0.7, ps.sym('i'))), ps.choice(0.3, ps.conc(ps.sym('e'), ps.sym('y')),
	ps.conc(ps.conc(ps.sym('e'), ps.sym('l')), ps.conc(ps.sym('l'), ps.sym('o'))))))

ran_test4 = ps.conc(
	ps.choice(0.7, ps.conc(ps.conc(ps.sym(' '), ps.sym('H')), 
	ps.star(0.7, ps.sym('i'))), ps.choice(0.3, ps.conc(ps.sym('e'), ps.sym('y')),
	ps.conc(ps.conc(ps.sym('e'), ps.sym('l')), ps.conc(ps.sym('l'), ps.sym('o'))))),
	ps.conc(ps.choice(0.4, ps.conc(ps.conc(ps.sym(' '), ps.sym('b')), 
	ps.conc(ps.sym('u'), ps.sym('d'))), ps.conc(ps.conc(ps.sym(' '), ps.sym('l')), 
	ps.conc(ps.sym('o'), ps.sym('v')))), ps.conc(ps.sym('l'), ps.sym('y'))))


print("\nTesting the RegEx: (a |0.4 ab)*0.3")
for i in range(0, 10):
	print("\n{0}. {1}".format(i+1, g.randomGenerator(ps.d, ran_test1)))

print("\n\nTesting the RegEx: PLD is (fun |0.55 hard)")
for i in range(0, 10):
	print("\n{0}. {1}".format(i+1, g.randomGenerator(ps.d, ran_test2)))

print("\n\nTesting the RegEx: (H((i)*0.7 |0.7 (ey |0.3 ello)))*0.1")
for i in range(0, 10):
	print("\n{0}. {1}".format(i+1, g.randomGenerator(ps.d, ran_test3)))

print("\n\nTesting the RegEx:  H((i)*0.7 |0.7 (ey |0.3 ello))( bud |0.4 lov)(ly |0.5 dy)")
for i in range(0, 10):
	print("\n{0}. {1}".format(i+1, g.randomGenerator(ps.d, ran_test4)))

print("\n______________________________________________"
		"_____________________________")
print("\n Testing semantics that finds the probability "
			"of deriving a given string.")
print("______________________________________________"
		"_____________________________")

# RegEx: a *0.3 b 
str_test1 = ps.conc(ps.star(0.3, ps.sym('a')), ps.sym('b'))

# RegEx: (a |0.2 b |0.3 c |0.4 d |0.5 r)*0.2
str_test2 = ps.star(0.2, ps.choice(0.2, ps.sym('a'), 
		ps.choice(0.3, ps.sym('b'), ps.choice(0.4, 
		ps.sym('c'), ps.choice(0.5, ps.sym('d'), ps.sym('r'))))))

# RegEx: H((i)*0.7 |0.7 (ey |0.3 ello))( bud |0.4 lov)(ly |0.5 dy)
str_test3 = ps.conc(
	ps.choice(0.7, ps.conc(ps.conc(ps.sym(' '), ps.sym('H')), 
	ps.star(0.7, ps.sym('i'))), ps.choice(0.3, ps.conc(ps.sym('e'), ps.sym('y')),
	ps.conc(ps.conc(ps.sym('e'), ps.sym('l')), ps.conc(ps.sym('l'), ps.sym('o'))))),
	ps.conc(ps.choice(0.4, ps.conc(ps.conc(ps.sym(' '), ps.sym('b')), ps.conc(ps.sym('u'), 
	ps.sym('d'))), ps.conc(ps.conc(ps.sym(' '), ps.sym('l')), ps.conc(ps.sym('o'), 
	ps.sym('v')))), ps.choice(0.5, ps.conc(ps.sym('l'), ps.sym('y')), ps.conc(ps.sym('d'), 
	ps.sym('y')))))

print("\nFinding the string 'abracadabra' from regex: "
		"a |0.2 b |0.3 c |0.4 d |0.5 r)*0.2 \nhas the probability: {0}"
			.format(g.stringProbability('abracadabra', ps.d, str_test2)))


print("\nFinding the string 'aaab' from regex: "
		" a *0.3 b \nhas the probability: {0}"
		.format(g.stringProbability('aaab', ps.d, str_test1)))


print("\nFinding the string ' Hi lovly' from regex: "
		" H((i)*0.7 |0.7 (ey |0.3 ello))( bud |0.4 lov)(ly |0.5 dy) \nhas the probability: {0}"
		.format(g.stringProbability(' Hi lovly', ps.d, str_test3)))

# Edge cases
print("\nFinding an empty string has the probability: {0}."
		.format(g.stringProbability('', ps.d, str_test3)))

print("\nFinding a string 'sss' that cannot be found of the particular NFA " 
		"has the probability: {0}."
		.format(g.stringProbability('sss', ps.d, str_test1)))



