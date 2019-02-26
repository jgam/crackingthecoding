#2.1
#remove duplicates from unsorted linked list
#how would you solve this problem if a temporary buffer is not allowed?

import unittest

def remove_dups(head):
	node = head
	if node:
		values = {node.data: True}
		while node.next:
			if node.next.data in values:
				node.next = node.next.next
			else:
				values[node.next.data] = True
				node = node.next
	return head
	#remove duplicates from an unsorted linked list

class Node():
	def __init__(self, data, next):
		self.data = data
		self.next = next

class Test(unittest.TestCase):
	def test_remove_dups(self):
		head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
		remove_dups(head)
		self.assertEqual(head.data, 1)
		self.assertEqual(head.next.data, 3)
		self.assertEqual(head.next.next.data, 5)
		self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
	unittest.main()

#2.2
# algorithm to find the kth to last element of a singly linked list
def return_kth_to_last(head, k):
	lead, follow = head, head
	for _ in xrange(k):
		if not lead:
			return None
		lead = lead.next
	while lead:
		lead, follow = lead.next, follow.next
	return follow

class Node():
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class Test(unittest.TestCase):
	def test_return_kth_to_last(self):
		head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
		self.assertEqual(None, return_kth_to_last(head,0).data)
		self.assertEqual(7, return_kth_to_last(head,1).data)
		self.assertEqual(4, return_kth_to_last(head,4).data)
		self.assertEqual(2, return_kth_to_last(head,6).data)
		self.assertEqual(1, return_kth_to_last(head, 7))

if __name__ == "__main__":
	unittest.main()


