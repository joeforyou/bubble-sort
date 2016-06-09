
def populateSample():
	import random
	count = 0
	sample = []
	while count < 101:
		sample.append(random.randint(1,10000))
		count += 1
	return sample

randList = populateSample()

# my pseudo-code: 
# iterate through an array. 
# at each item, ask: is the next item less than this item (me)? 
# if yes: swap. if no, don't do anything.

easyList = [6,1,8,10,4]

def bubbleSort(arr):

	passnum = len(arr) - 1

	while passnum > 0:

		for i in range(passnum):
			if (arr[i] > arr[i + 1]):
				temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = temp
		passnum -= 1

# bubbleSort(easyList)
# print easyList
bubbleSort(randList)
print randList