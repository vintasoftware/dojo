class Node:

	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node


class LinkedList:

	def __init__(self, head):
		self.head = head

	def add(self, node, prev_node=None):
		if self.head.value > node.value:
			self.head, self.head.next_node = node, self.head
			return

		if not prev_node:
			prev_node = self.head

		if not prev_node.next_node:
			prev_node.next_node = node
			return

		if prev_node.value > node.value:
			prev_node, prev_node.next_node = node, prev_node
			return
		
		return self.add(node=node, prev_node=prev_node.next_node)
