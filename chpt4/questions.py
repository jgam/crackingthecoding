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
def Minimal_tree(array):
	#BST is a binary tree(up to two children) that has left descendents <= n < right descendents
	#array = [2,4,6,8,10,20]
	#output = [8:[4,10],4:[2, 6], 10:[20]]
	mid_point = 0
	if len(array) % 2 == 0:
		mid_point = len(array)//2
	else:
		mid_point = len(array)//2 + 1

	
print(solution([2,4,6,8,10,20]))

