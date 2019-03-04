#4.1
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes
def Route_between_nodes(graph, a, b):
	#directed in adjacency list will contain outbounds
	# we can implement bidrectional? -> more efficient when having two graphs
	#This is bfs problem
	#graph = [1:[2,3], 2:[4,5],3:[1,2]]
	#a and b being the two points
	queue_list = []
	tmp_list = [a]
	for _ in range(len(graph)):
		queue_list = temp_list
		for point in queue_list:
			if b in graph[point]:
				return True
			else:
				tmp_list.extend(graph[point])
	return False

#print(Route_between_nodes())

#4.2
#Given a sorted(increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height
class Node:
	def __init__(self, item):
		self.right = None
		self.left = None
		self.val = item

	def __str__(self):
		return '('+str(self.left) + ':L ' + "V:" + str(self.val) + " R:" + str(self.right) + ')'



def Minimal_tree(array, start = 0, end = 0):
	#BST is a binary tree(up to two children) that has left descendents <= n < right descendents
	#array = [2,4,6,8,10,20]
	#output = [8:[4,10],4:[2, 6], 10:[20]]
	mid_point = 0
	if start > end:
		return ''

	mid = (start+end+1)//2
	root = Node(array[mid])
	root.left = Minimal_tree(array, start, mid-1)
	root.right = Minimal_tree(array, mid+1, end)
	return root

array = [2,4,6,8,10,20]
print(Minimal_tree(array, 0, len(array)-1))

#4.3
#Given a binary tree, design an algorithm which creates a linked list of all the nodes at
#each depth.(if you have a tree with depth D, you will have D linked Lists)

def list_of_depths(binary_tree):
  if not binary_tree:
    return []
  lists = []
  queue = Queue()
  current_depth = -1
  current_tail = None
  node = binary_tree
  node.depth = 0
  while node:
    if node.depth == current_depth:
      current_tail.next = ListNode(node.data)
      current_tail = current_tail.next
    else:
      current_depth = node.depth
      current_tail = ListNode(node.data)
      lists.append(current_tail)
    for child in [node.left, node.right]:
      if child:
        child.depth = node.depth + 1
        queue.add(child)
    node = queue.remove()
  return lists

class TreeNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.depth = None

class ListNode():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self.data) + ',' + str(self.next)

class Queue():
  def __init__(self):
    self.head, self.tail = None, None
  
  def add(self, item):
    if self.head:
      self.tail.next = ListNode(item)
      self.tail = self.tail.next
    else:
      self.head = self.tail = ListNode(item)
  
  def remove(self):
    if not self.head:
      return None
    item = self.head.data
    self.head = self.head.next
    return item

import unittest

class Test(unittest.TestCase):
  def test_list_of_depths(self):
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = list_of_depths(node_a)
    self.assertEqual(str(lists[0]), "A,None")
    self.assertEqual(str(lists[1]), "B,C,None")
    self.assertEqual(str(lists[2]), "D,E,F,None")
    self.assertEqual(str(lists[3]), "H,G,None")
    self.assertEqual(len(lists), 4)
    print('lists are: ',lists)

if __name__ == "__main__":
  unittest.main()

