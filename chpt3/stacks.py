graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()#A
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            print(stack)
            stack.extend(graph[vertex] - visited)
            print('----afterstack----')
            print(stack)
    return visited
'''
print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}
'''
def better_dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	for next in graph[start] - visited:
		better_dfs(graph, next, visited)
	return visited


#3.1
#Describe how you could use a single array to implement three stacks
#-> I can use list of three lists that each being the stack or dictionary (hash map) to keep up the three stacks.

#3.2
#design a stack which in addition to push and pop. has a function min which returns the minimum element?
#we can simply add a min value in class stack so that we can keep updating the value and return it whenever we need it

#3.3
#setofstacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity
#setofstacks.push() and setofstacks.pop() should behave identically to a single stack.
class stacks:
	def __init__(self):
		self.stacks = []
		self.current_stacks=[]
		#this is because immutable value is int
		self.current_length = len(self.current_stacks)

	def push(self, value):
		if len(self.current_stacks) == 10:
			self.stacks.append(self.current_stacks)
			self.current_stacks = []
		self.current_stacks.append(value)

	def pop(self, index = 0):
		if self.current_length == 0:
			if len(self.stacks) == 0:
				print('popping from nothing error')
				return 0

			self.current_stacks = self.stacks[-1]

		if index < self.current_length and index > 0:
			return self.current_stacks.pop()
		else:
			self.current_stacks = self.current_stacks[:value]+self.current_stacks[value+1:]
			return self.current_stacks[value]

	def current(self):
		print(self.stacks)
		print(len(self.stacks)+1, 'th stack is: ', self.current_stacks)
		print(len(self.current_stacks))

a = stacks()

for i in range(13):
	a.push(i)

a.current()
#print(a.current_length)

#3.4
#Implement myquee class which implements a queue using two stacks
#take the values out of one stack to the other and from that other stack, take out the numbers we get
#a queue.

#3.5
#sort a stack such that the samllest items are on the top.
#using two temps, what we cna do is while temp stacks'value is less than current queue's value,
#keep appending the value to the temp stack
#else, take out values from temp stack until the value from temp stack is less the value from original stack

