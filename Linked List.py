### Write code to remove duplicates from an unsorted linked list


class Node(object):
	def __init__(self, data):
		self.data = data;
		self.next = None;

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head;

	def addData(self, data):
		if self.head:
			current = self.head;
			while current.next:
				current = current.next;
			current.next = data;
		else:
			self.head = data;

e1 = Node(2)
e2 = Node(3)
e3 = Node(4)
e4 = Node(5)
e5 = Node(6)

ll = LinkedList(e1)
ll.addData(e2)
ll.addData(e3)
ll.addData(e4)
ll.addData(e5)

def duplicates(node):
	seen = set();
	current = node;
	while current:
		if current.data not in seen:
			seen.add(current.data)
		current = current.next;
	return tuple(seen);

print duplicates(ll.head);

### Implement an algorithm to  nd the nth to last element of a singly linked list


def nthtolast(nth):
	if ll:
		last = 0;
		current = ll.head;
		while current:
			last = last + 1;
			current = current.next;
		pos = last-nth;
		print pos;
		current = ll.head;
		while pos > 0:
			current = current.next;
			pos = pos - 1;
		return current.data;
	return None;

print nthtolast(3)

### Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node

def middle():
	last = 0;
	current = ll.head;
	while current:
		last = last + 1;
		current = current.next;
	pos = last/2;
	current = ll.head;
	while pos >= 0:
		if pos == 1:
			fromjoin = current;	
		if pos == 0:
			tojoin = current.next;
		pos = pos - 1;
		current = current.next;
	fromjoin.next = tojoin;
	return duplicates(ll.head);

#print middle();

### Given a circular linked list, implement an algorithm which returns node at the begin- ning of the loop

def circular():
	last = set();
	current = ll.head;
	while current:
		if current.data in last:
			return current.data;
		last.add(current.data);
		current = current.next;
	return;

print circular();

















			