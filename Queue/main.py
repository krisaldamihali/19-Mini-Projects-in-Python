'''
Assignment 4: 
Exercise 2: Create an algorithm to sort the below numbers from the lowest to the highest:

Name: [Krisalda Mihali]
'''

from queue import Queue 

#This function returns index of minimum element from front to sortedIndex 
def minIndex(q, sortedIndex): 
	min_index = -1
	min_val = 999999999999
	n = q.qsize() 
	for i in range(n): 
		curr = q.queue[0] 
		q.get() 

		# we add the condition i <= sortedIndex 
		# because we don't want to traverse 
		# on the sorted part of the queue, 
		# which is the right part. 
		if (curr <= min_val and i <= sortedIndex): 
			min_index = i 
			min_val = curr 
		q.put(curr) 
	return min_index 

def insertMinToRear(q, min_index): 
	min_val = None
	n = q.qsize() 
	for i in range(n): 
		curr = q.queue[0] 
		q.get() 
		if (i != min_index): 
			q.put(curr) 
		else: 
			min_val = curr 
	q.put(min_val) 

def sortQueue(q): 
	for i in range(1, q.qsize() + 1): 
		min_index = minIndex(q, q.qsize() - i) 
		insertMinToRear(q, min_index) 

x1=int(input("Enter a number:"))
x2=int(input("Enter a number:"))
x3=int(input("Enter a number:"))
x4=int(input("Enter a number:"))
print("The order of the numbers you choose is:")

if __name__ == '__main__': 
	q = Queue() 
	q.put(x1) 
	q.put(x2)
	q.put(x3) 
	q.put(x4) 
	sortQueue(q) 
	
	while (q.empty() == False): 
		print(q.queue[0], end = " ") 
		q.get() 
