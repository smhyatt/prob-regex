import random
import parser as ps


def randomGenerator(d, nfa):
	output = ""
	(start, end) = nfa
	idx = start

	while (idx != end):
		edges = d[idx]
		current = edges[0]

		rand = random.uniform(0.0, 1.0)	
		if rand < current[1]:
			idx = current[0]
			if current[2] != 'epsilon':
				output += current[2]
		else:
			current = edges[1]
			idx = current[0]
			if current[2] != 'epsilon':
				output += current[2]

	return output



def stringProbability(st, d, nfa):
	stack = []
	total = 0
	(start, end) = nfa
	stack.append((start, 1.0, st))

	while len(stack) > 0:
		(i, p, s) = stack.pop()

		if (i == end) and (s == ''):
			total += p

		edges = ps.d[i]

		for edge in edges:
			if edge[2] == 'epsilon': 	
				np = p * edge[1]
				stack.append((edge[0], np, s))
			elif (s != '') and (edge[2] == s[0]):
				np = p * edge[1]
				ns = s[1:]
				stack.append((edge[0], np, ns))

	return total



