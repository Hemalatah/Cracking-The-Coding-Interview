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
