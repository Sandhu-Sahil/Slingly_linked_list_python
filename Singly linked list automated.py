def options():
	print('Choose one of the following options:')
	print('1- Add a value to the front of the list.')
	print('2- Add a value to the back of the list.')
	print('3- Add a value to next to a target location in the list.')
	print('4- Print the list.')
	print('5- Count the number of elements in the list.')
	print('6- Determine if a certain value is present in the list.')
	print('7- End Program.')
	i = int(input())
	return i;

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

		if point == 0:
			new_bucket.next = self.head
			self.head = new_bucket

		if point != 'end' and point > 0:
			last_bucket = self.head
			for i in range(0 , (point - 1)):
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

newlist = linkedlist();

if __name__ == '__main__':

	number = options();
	while True:
		if number == 1:
			newlist.insert(bucket(input("value: \n")), 0)
			number = options()
		elif number == 2:
			newlist.insert(bucket(input("value: \n")), 'end')
			number = options()
		elif number == 3:
			i = int(input("Target location: \n"))
			newlist.insert(bucket(input("value: \n")), i)
			number = options()
		elif number == 4:
			newlist.printlist()
			number = options()
		elif number == 5:
			newlist.count()
			number = options()
		elif number == 6:
			i = input("value: \n")
			newlist.check(i)
			number = options()
		elif number == 7:
			quit()
		else:
			number = options()