###You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B Write a method to merge B into A in sorted order

def merge(arr1,arr2):
	arr1 = sorted(arr1);
	arr2 = sorted(arr2);
	new_arr = [];
	i, j = 0, 0;
	while i < len(arr1) and j < len(arr2):
		if arr1[i] > arr2[j]:
			new_arr.append(arr2[j]);
			j = j + 1;
		else:
			new_arr.append(arr1[i]);
			i = i + 1;
	while i < len(arr1):
		new_arr.append(arr1[i]);
		i = i + 1;
	while j < len(arr2):
		new_arr.append(arr2[j]);
		j = j + 1;
	return new_arr;

print merge([2,4,7],[7,1,0]);

### Write a method to sort an array of strings so that all the anagrams are next to each other


def sort_anagram(arr):
	return sorted(arr, cmp=lambda x,y: cmp(sorted(x),sorted(y)));

print sort_anagram(["god", "dog", "abc", "cab", "man"]);

###Given a sorted array of n integers that has been rotated an unknown number of times,giveanO(logn)algorithmthat ndsanelementinthearray Youmayassume that the array was originally sorted in increasing order EXAMPLE: Input:  nd 5 in array (15 16 19 20 25 1 3 4 5 7 10 14) Output: 8 (the index of 5 in the array)

def find_pos(arr):
	for i in range(len(arr)-1):
		if arr[i+1] < arr[i]:
			return i + 1;


def find_elem(arr, element):
	pos = find_pos(arr);
	left_arr = arr[:pos];
	right_arr = arr[pos:];
	if left_arr[0] > element:
		for i in right_arr:
			if i == element:
				return arr.index(element);
	for i in left_arr:
		if i == element:
			return arr.index(element);

print find_elem([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5);

### Given a sorted array of strings which is interspersed with empty strings, write a meth- od to  nd the location of a given string

def find_loc(arr, elem):
	mid = len(arr) - 1;
	if elem >= arr[mid]:
		for i in range(len(arr)-1, mid, -1):
			if arr[i] == elem:
				return i;
	for i in range(mid-1, 0, -1):
		if arr[i] == elem:
			return i;
	return -1;

print find_loc(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ballcar");


### Given a matrix in which each row and each column is sorted, write a method to  nd an element in it

def find_mat(mat, elem, m, n):
	row = 0;
	col = n-1;
	while row < m and col >= 0:
		if mat[row][col] == elem:
			return True;
		elif mat[row][col] > elem:
			col = col - 1;
		else:
			row = row + 1
	return False;

print find_mat([[1,2,3],[4,5,6],[7,8,9]], 0, 3, 3);


def circus_tower(arr):
	arr = sorted(arr);
	new_arr = [];
	new_arr.append(arr[0]);
	i = 1;
	for i in range(len(arr)):
		if arr[i][1] > arr[i-1][1] and new_arr[-1][1] < arr[i][1]:
			new_arr.append(arr[i]);
	return new_arr;

print circus_tower([[65, 100], [70, 150], [56, 90], [75, 190], [60, 95], [68, 110]]);








