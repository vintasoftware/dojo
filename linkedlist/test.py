import unittest


from prog import Node, LinkedList


class LinkedListTests(unittest.TestCase):

	def test_object_is_node(self):
		node = Node(value=10)

		self.assertIsInstance(node, Node)

	def test_node_has_value(self):
		node = Node(value=10)

		self.assertEqual(node.value, 10)

	def test_node_has_next(self):
		next_node = Node(value=11)
		node = Node(value=10, next_node=next_node)

		self.assertEqual(node.next_node, next_node)

	def test_object_is_linked_list(self):
		node = Node(value=23)
		linked_list = LinkedList(head=node)

		self.assertIsInstance(linked_list, LinkedList)

	def test_list_has_head(self):
		node = Node(value=23)
		linked_list = LinkedList(head=node)

		self.assertEqual(linked_list.head, node)

	def test_insert_node_into_list(self):
		node = Node(value=23)
		another_node = Node(value=24)
		linked_list = LinkedList(head=node)

		linked_list.add(another_node)
		self.assertEqual(linked_list.head, node)
		self.assertEqual(linked_list.head.next_node, another_node)

	def test_nodes_are_added(self):
		head_node = Node(value=23)
		second_node = Node(value=24)
		third_node = Node(value=25)
		linked_list = LinkedList(head=head_node)
		linked_list.add(second_node)
		linked_list.add(third_node)

		self.assertEqual(linked_list.head, head_node)
		self.assertEqual(head_node.next_node, second_node)
		self.assertEqual(second_node.next_node, third_node)

	def test_nodes_replaces_head(self):
		head_node = Node(value=23)
		second_node = Node(value=19)
		linked_list = LinkedList(head=head_node)
		linked_list.add(second_node)

		self.assertEqual(linked_list.head, second_node)
		self.assertEqual(linked_list.head.next_node, head_node)

	def test_nodes_are_added_in_order(self):
		head_node = Node(value=23)
		second_node = Node(value=19)
		third_node = Node(value=25)
		linked_list = LinkedList(head=head_node)
		linked_list.add(second_node)
		linked_list.add(third_node)

		self.assertEqual(linked_list.head, second_node)
		self.assertEqual(linked_list.head.next_node, head_node)
		self.assertEqual(linked_list.head.next_node.next_node, third_node)


if __name__ == '__main__':
	unittest.main()