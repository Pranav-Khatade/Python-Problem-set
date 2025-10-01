class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	
class Linkedlist:

	def __init__(self):
		self.head=None


	def insert_start(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node


	def insert_index(self, data, ind):
		if (ind==0):
			self.insert_start(data)
			return 

		position = 0
		currt = self.head
		while (position+1 != ind and currt != None):
			position+=1
			currt = currt.next
		if currt != None:
			new_node = Node(data)
			new_node.next = currt.next
			currt.next = new_node
		else:
			print("error NO further node present!")

	def insert_end(self,data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		current = self.head
		while(current.next != None):
			current = current.next
		current.next = new_node
	def print_linked_list(self):
		current = self.head 
		while(current):
			print(str(current.data), end=" -> ")
			current = current.next
		print("NULL")

	def link_anywhere(self, link, fin):
		current = self.head
		pre = self.head
		count = 0
		while(current.data != fin and current is not None):
			current = current.next

		while( pre is not None and count != link):
			pre = pre.next
			count += 1
		current.next = pre
		print(current.next.data)

	def loop_check(self):
		current = self.head
		my_list =[]
		while(current != None):
			if current.data not in my_list:
				my_list.append(current.data)
			else:
				print("Loop detected")
				break

def main():
	new_list =[]
	node = Linkedlist()
	n = int(input("Enter The no. of Input :"))
	for i in range(n):
		a = int(input("enter element :"))
		new_list.append(a)
		node.insert_start(a)
	p = int(input("Enter Link :"))
	dat = new_list[n-1]
	node.link_anywhere(p,dat)
	node.loop_check()


if __name__ == "__main__":
	main()