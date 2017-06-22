### Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].

def twosum(arr, target):
	i, j = 0, 1;
	while i < len(arr):
		while j < len(arr):
			if i != j and arr[i] + arr[j] == target:
				return [i,j];
			j = j + 1;
		i += 1;
	return;

print twosum([2,7,11,5], 9);

### Given a string, find the length of the longest substring without repeating characters. Given "abcabcbb", the answer is "abc", which the length is 3.

def longestsubstring(s):
	new_str = "";
	longest = '';
	for i in s:
		if i in new_str:
			if len(longest) < len(new_str):
				longest = new_str;
			new_str = '';
		new_str += i;
	return longest;

print longestsubstring("pwwkew");

### There are two sorted arrays nums1 and nums2 of size m and n respectively. nums1 = [1, 3]nums2 = [2] The median is 2.0

def median(arr1, arr2):
	i, j = 0, 0;
	new_arr = [];
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			new_arr.append(arr1[i]);
			i = i + 1;
		else:
			new_arr.append(arr2[j]);
			j += 1;
	while i < len(arr1):
		new_arr.append(arr1[i]);
		i += 1;
	while j < len(arr2):
		new_arr.append(arr2[j]);
		j += 1;
	length = len(new_arr);
	print new_arr;
	if length % 2 == 0:
		return (float(new_arr[(length/2)-1]) + float(new_arr[length/2]))/2;
	else:
		return float(new_arr[length/2]);
	return;

print median([1,3], [2]);

### Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

def longestpalindrome(s):
	longest = '';
	for i in range(len(s)):
		for j in range(len(s)):
			subs = s[i:j];
			if subs == subs[::-1] and len(longest) <= len(subs):
				longest = subs;
	return longest;

print longestpalindrome("babad");

### The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
#P   A   H   N
#A P L S I I G
#Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

def zigzag(s, row):
	col = (len(s)/(row + 1)) * 2;
	if (len(s)%(row + 1)) > 0 and (len(s)%(row + 1)) <= row:
		col += 1;
	i = 0;
	matrix = [[0 for _ in range(col)] for _ in range(row)];
	while i < col:
		j = 0;
		print s;
		while j < row:
			if i % 2 != 0:

				matrix[j][i] = s[0];
			print matrix;
			s = s[1::];
			j += 1;
		i += 1;
	return matrix;


#print zigzag("PAYPALISHIRING", 3);


### Reverse digits of an integer.

def reverse(integer):
	res = '';
	if integer[0] == '+' or integer[0] == '-':
		res += integer[0];
		integer = integer[1:];
	if len(integer) > 32:
		return 0;
	integer = integer[::-1];
	while integer[0] == '0':
		integer = integer[1:];
	res += integer;
	return res;

print reverse("-0031");

### Determine whether an integer is a palindrome. Do this without extra space.

def palindrome(integer):
	integer = str(integer);
	return integer == integer[::-1];

print palindrome(1331);

###Implement regular expression matching with support for '.' and '*'.

def isMatch(s,p):
	if s == p:
		return True;
	else:
		if '.' in p or '*' in p:
			for i in range(len(p)):
				if p[i] == '.' or p[i] == '*':
					p = p.replace(p[i], s[i]);
			if s in p:
				return True;
			else:
				return False;
		else:
			return False;

print isMatch("aa","a") # false
print isMatch("aa","aa") # true
print isMatch("aaa","aa") # false
print isMatch("aa", "a*") # true
print isMatch("aa", ".*") # true
print isMatch("ab", ".*") # true
print isMatch("aab", "c*a*b") # true

### 3sum

def threeSum(s):
	res_arr = []
	for i in range(len(s)):
		for j in range(len(s)):
			sub_arr = s[i:j]
			if len(sub_arr) == 3:
				if sum(sub_arr) == 0:
					res_arr.append(sub_arr)
	return res_arr;

print threeSum([-1,0,1,2,-1,-4])

### three Sum Closest

def threeSumClosest(s, target):
	res_arr = []
	for i in range(len(s)):
		for j in range(len(s)):
			sub_arr = s[i:j]
			if len(sub_arr) == 3:
				if sum(sub_arr) == target or abs(target - sum(sub_arr)) == 1:
					res_arr.append(sub_arr)
	return res_arr

print threeSumClosest([-1,2,1,-4], 1)

### Letter Combinations of a Phone Number

def letterCombinations(s):
	myDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
	arr = []
	res_arr = []
	for i in range(len(s)):
		if s[i] in myDict:
			arr.append(myDict[s[i]])
	print arr
	l = 0
	while l < len(arr[0]):
		k = 0
		while k < len(arr[1]):
			res_arr.append(arr[0][l]+arr[1][k])
			k += 1
		l += 1
	return res_arr;


print letterCombinations("23")

### 4sum

def fourSum(s):
	res_arr = []
	for i in range(len(s)):
		for j in range(len(s)):
			sub_arr = s[i:j]
			if len(sub_arr) == 4:
				if sum(sub_arr) == 0:
					res_arr.append(sub_arr)
	return res_arr


print fourSum([1,0,-1,0,-2,2])

### valid paranthesis

def validParanthesis(s):
	opn = 0
	arr= []
	for i in s:
		print i
		if i == '(' or i == '{' or i =='[':
			opn += 1
			arr.append(i)
		elif i == ')':
			if arr[-1] == '(':
				arr.pop()
				opn -= 1
			else:
				return False
		elif i == '}':
			if arr[-1] == '{':
				arr.pop()
				opn -= 1
			else:
				return False
		elif i == ']':
			if arr[-1] == '[':
				arr.pop()
				opn -= 1
			else:
				return False
	if opn == 0:
		return True
	else:
		return False

print validParanthesis('[[]}')

### Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParanthesis(n):
	def walk(l, r, s):
		if l > 0:
			walk(l-1, r, s + '(')
		if r > l:
			walk(l, r-1, s + ')')
		if not l and not r:
			print s;
	walk(n,n,'')

generateParanthesis(3)

### Remove Element in place 

def removeElement(arr, val):
	arr.sort()
	while val in arr:
		arr = arr[:arr.index(val)] + arr[((arr.index(val))+1):]
	return len(arr), arr

print removeElement([3,2,2,3,3,3,3,2],3)

### Remove Duplicates from Sorted Array in place

def removeDuplicates(arr):
	i = 0
	while i in range(len(arr)):
		if arr[i] in arr[((arr.index(arr[i]))+1):]:
			arr = arr[:i] + arr[i+1:]
			i -= 1
		i += 1
	return arr


print removeDuplicates([1,1,1,1,2,2])

















