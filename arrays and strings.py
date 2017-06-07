### Implement an algorithm to determine if a string has all unique characters. What if youcan not use additional data structures?
def unique(str):
	str = str.lower();
	for i in range(len(str)):
		if str[i] in str[i+1: ]:
			return False;
	return True;

print unique("Today");

### Write code to reverse a C-Style String
def reverse_str(str):
	return str[::-1];

print reverse_str("Today");

### Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
def duplicate_Character(str):
	str = str.lower();
	new_str = '';
	for i in range(len(str)):
		if str[i] not in str[i+1:]:
			new_str += str[i];
	return new_str + str[-1];

print duplicate_Character('maddamn')

### Write a method to decide if two strings are anagrams or not.
def anagram(str1, str2):
	for i in str1:
		if i in str2:
			index = str2.index(i);
			str2 = str2[:index] + str2[index+1:];
	if len(str2):
		return False;
	return True;

print anagram('happy', 'apphhy')

### Write a method to replace all spaces in a string with %20
def replce(str):
	str = list(str);
	for i in range(len(str)-1,0,-1):
		if str[i] == ' ':
			str.pop();
		else:
			break;
	for i in range(len(str)-1):
		if str[i] == ' ':
			str[i] = '%20'
	return "".join(str);

print replce('he l o    ');

#Implement a method to perform basic string compression using the counts of repeated characters
#aabcccccaaa would become a2blc5a3.

def stringCompress(string):
	new_str = '';
	i = 0;
	while i <= range(len(string)-1):
		count = 1;
		new_str += string[i];
		while i+1 <= len(string)-1 and string[i] == string[i+1]:
			count = count + 1;
			i = i + 1;
		new_str += str(count);
		i = i + 1;
		if i == len(string):
			return new_str;
	return new_str;

print stringCompress('aabcccccaaaa');

#Rotate a NxN matrix 90 degrees
#(assuming clockwise rotation)
##[ 1  2  3  4 ]
##[ 5  6  7  8 ]
##[ 9  10  11  12 ]
##[ 13  14  15  16 ]

def rotate(matrix):
	n = len(matrix);
	new_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
	k = n-1;
	i = 0;
	while k >= 0 and i < n:
		row = matrix[k];
		j = 0;
		while j < n:
			new_matrix[j][i] = row[j]
			j = j + 1;
		i = i + 1;
		k = k - 1;
	return new_matrix;


print rotate([[ 1, 2, 3, 4 ],[ 5, 6, 7, 8 ],[ 9, 10, 11, 12],[13, 14, 15, 16 ]]);








