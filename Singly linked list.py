class bucket:
	def __init__(self, add):
		self.data = add
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def insert(self, new_bucket, point):
		if point == 'end':
			if self.head != None:
				last_bucket = self.head
				while last_bucket.next != None:
					last_bucket = last_bucket.next
				last_bucket.next = new_bucket
			else:
				self.head = new_bucket

		if point != 'end':
			last_bucket = self.head
			for i in range(0 , (point - 2)):
				last_bucket = last_bucket.next
			new_bucket.next = last_bucket.next
			last_bucket.next = new_bucket

	def count(self):
		temp_bucket = self.head
		i = 0
		while temp_bucket != None:
			temp_bucket = temp_bucket.next
			i = i + 1
		print(" ",{i})

	def printlist(self):
		temp_bucket = self.head
		print("[", end="")
		while temp_bucket != None:
			print(temp_bucket.data , end="")
			if temp_bucket.next != None:
				print(",", end=" ")
			temp_bucket = temp_bucket.next
		print("]")

	def check(self, tocheck):
		temp_bucket = self.head
		while temp_bucket != None:
			if temp_bucket.data == tocheck:
				print("Exists")
				temp_bucket = temp_bucket.next
				break
			else:
				temp_bucket = temp_bucket.next


if __name__ == '__main__':

	newlist = linkedlist()

	newlist.insert(bucket('s'), 'end')
	newlist.insert(bucket('a'), 'end')
	newlist.insert(bucket('n'), 'end')
	newlist.insert(bucket('d'), 'end')
	newlist.insert(bucket('u'), 'end')

	newlist.insert(bucket('h'), 5)

	newlist.count()
	newlist.printlist()
	newlist.check('h')