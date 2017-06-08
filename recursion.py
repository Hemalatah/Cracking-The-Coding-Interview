### Write a method to generate the nth Fibonacci number

def fibonacci(num):
	if num <= 1:
		return num;
	else:
		return fibonacci(num-1) + fibonacci(num-2);

print fibonacci(2);

### Write a method that returns all subsets of a set
# [1,[2,4],[3,[4,5]]] should be [1,[2,4],2,4,[3,[4,5]],3,[4,5],4,5]


def allsubset(arr):
	sets = [];
	def subset(arr):
		for i in arr:
			sets.append(i);
			if type(i) is list:
				subset(i);
	subset(arr);
	return sets;

print allsubset([1,[2,4],[3,[4,[5]]]]);
				

### Write a method to compute all permutations of a string


def permutation(s):
	if len(s) <= 1:
		return [s];
	if len(s) == 2:
		return [s, s[::-1]];
	perm = permutation(s[:-1]);
	results = [];
	for p in perm:
		for i in range(len(p)+1):
			results.append(p[:i]+s[-1]+p[i:]);
	return results;

print permutation("abc");

### Implement an algorithm to print all valid (e g , properly opened and closed) combi- nations of n-pairs of parentheses


def walk(s, l, r):
    if l > 0:
        walk(s + '(', l-1, r)
    if r > l:
        walk(s + ')', l, r-1)
    if not l and not r:
        print s
    
walk('', 1, 1);

### Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.

num = 10;
pos_way = set();
cents = [1,5,10,25];
def ways(current):
	if sum(current) == num:
		pos_way.add(tuple(sorted(current)));
		return;
	for cent in cents:
		if sum(current) + cent > num:
			break;
		ways(current + [cent]);

	return pos_way;

#print ways([]);


def walk(x, y, path=[]):
    if x >= N or y >= N:
        return
    if (x,y) in offlimits:
        return
    path = path[:]
    path.append((x,y))
    if x == N - 1 and y == N -1:
        paths.append(path)
    walk(x+1, y, path)
    walk(x, y+1, path)
    return paths;
N = 12;
paths = [];
offlimits = [(2,3)];
offlimits = set(offlimits)
print walk(0, 0)

### Write an algorithm to print all ways of arranging eight queens on a chess board so that none of them share the same row, column or diagonal



