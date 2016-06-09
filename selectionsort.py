# scan entire array. find minimum. swap that index with the first one in the array.

def populateSample():
	import random
	count = 0
	sample = []
	while count < 101:
		sample.append(random.randint(1,10000))
		count += 1
	return sample

randList = populateSample()

bCase = [50, 34, 2, 18, 46, 10]

def selectionSort(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min]:
				min = j

		temp = arr[min]
		arr[min] = arr[i]
		arr[i] = temp

selectionSort(randList)
print randList