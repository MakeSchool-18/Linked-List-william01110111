#!python

from __future__ import print_function


class Node(object):

	def __init__(self, data):
		"""Initialize this node with the given data"""
		self.data = data
		self.next = None

	def __repr__(self):
		"""Return a string representation of this node"""
		return 'Node({})'.format(repr(self.data))


class LinkedList(object):
	
	def __init__(self, iterable=None):
		"""
		Initialize this linked list; append the given items, if any
		
		best case running time: O(1) if method is not sent an iterable
		worst case running time: O(n) if method is sent an iterable where n is the size for the iterable sent
		"""
		
		self.head = None
		self.tail = None
		if iterable:
			for item in iterable:
				self.append(item)

	def __repr__(self):
		"""
		Return a string representation of this linked list
		
		running time: same as as_list
		"""
		return 'LinkedList({})'.format(self.as_list())

	def as_list(self):
		"""
		Return a list of all items in this linked list
		
		running time: O(n) where n is the size of the list
		"""
		result = []
		current = self.head
		while current:
			result.append(current.data)
			current = current.next
		return result

	def is_empty(self):
		"""Return True if this linked list is empty, or False"""
		return self.head is None

	def length(self):
		"""
		Return the length of this linked list by traversing its nodes
		
		running time: O(n) where n is the number of nodes
		"""
		current = self.head
		count = 0
		while current:
			count+=1
			current = current.next
		
		return count

	def append(self, item):
		"""
		Insert the given item at the tail of this linked list
		
		running time: O(1)
		"""
		assert (self.head==None)==(self.tail==None)
		
		if self.head: #either head and tail should both contain values or both be None
			self.tail.next = Node(item)
			self.tail=self.tail.next
		else:
			self.head=self.tail=Node(item)
		
		return item
	
	
	def prepend(self, item):
		"""
		Insert the given item at the head of this linked list
		
		running time: O(1)
		"""
		if self.head: #either head and tail should both contain values or both be None
			tmp = self.head.next
			self.head = Node(item)
			self.head.next=tmp
		else:
			self.head=self.tail=Node(item)

	def delete(self, item):
		"""
		Delete the given item from this linked list, or raise ValueError
		
		best case running time: O(1) if the item to delete is at the beginning
		worst case running time: O(n) where n is the distance from the begining of the list to the item
		"""
		
		if self.head!=None:
			if item==self.head.data:
				if self.head.next==None:
					self.tail=None
				self.head=self.head.next
				return
				
			node=self.head
			
			while (node.next!=None):
				if node.next.data==item:
					if node.next.next==None:
						self.tail=node
					node.next=node.next.next
					return
				
				node=node.next
		
		raise ValueError
		

	def find(self, quality):
		"""
		Return an item from this linked list satisfying the given quality
		
		best case running time: O(1) if the item to delete is at the beginning
		worst case running time: O(n) where n is the distance from the begining of the list to the first item that satisfies the quality
		"""
		
		node=self.head
		while(node):
			if quality(node.data):
				return node.data
			
			node=node.next
		


def test_linked_list():
	ll = LinkedList()
	print(ll)
	ll.append('A')
	print(ll)
	ll.append('B')
	print(ll)
	ll.append('C')
	print(ll)
	print('head: ' + str(ll.head))
	print('tail: ' + str(ll.tail))
	print(ll.length())

	ll.delete('A')
	print(ll)
	ll.delete('C')
	print(ll)
	ll.delete('B')
	print(ll)
	print('head: ' + str(ll.head))
	print('tail: ' + str(ll.tail))
	print(ll.length())


if __name__ == '__main__':
	test_linked_list()
