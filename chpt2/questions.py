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
"""
if __name__ == "__main__":
	unittest.main()
"""
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
"""
if __name__ == "__main__":
	unittest.main()
"""
#2.3
#delete the middle node

class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		return

	def has_value(self, value):
		if self.data == value:
			return True
		else:
			return False

class SingleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		return

	def add_list_item(self, item):
		if not isinstance(item, ListNode):
			item = ListNode(item)

		if self.head is None:
			self.head = item
		else:
			self.tail.next = item

		self.tail = item

		return

	def list_length(self):
		count = 0
		current_node = self.head

		while current_node is not None:
			count += 1
			current_node = current_node.next

		return count

	def output_list(self):
		current_node = self.head
		while current_node is not None:
			print(current_node.data)
			current_node = current_node.next
		return

	def delete_middle_node(self):
		current_node = self.head
		list_range = self.list_length()//2
		for _ in range(list_range):
			current_node = current_node.next 
		return current_node.data

	#2.4 parittion
	def partition(self, partition_value):
		less_linked_list = SingleLinkedList()
		large_linked_list = SingleLinkedList()
		self_range = self.list_length()
		for _ in range(self_range):
			return 0


#create four single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)
node5 = ListNode(13)

track = SingleLinkedList()
print("track length: %i" % track.list_length()):

for current_item in [node1, node2, item3, node4, node5]:
	track.add_list_item(current_item)
	print("track length: %i" % track.list_length())
	track.output_list()
print(track.output_list())
print("deleted node", track.delete_middle_node())