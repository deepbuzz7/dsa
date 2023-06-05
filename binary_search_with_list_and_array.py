# The below code is to see how the binary search function behaves when using a list and a static array.
# output:
#element found at 999998
#time taken to search in the list 3.147125244140625e-05
#element found at 999998
#time taken to search in the list 2.8133392333984375e-05

import random
import time
import array

def binary_search(arr,element):
	low=0
	high=len(arr)-1
	while low <=high:
		mid=int((low+high)/2)
		e=arr[mid]
		if e==element:
			return mid
		elif e<element:
			low=mid+1
		else:
			high=mid-1
	return None

if __name__=='__main__':
	#adding 1000000 elements to list/array
	#list
	list_arr=[]
	for i in range(0,1000000):
		list_arr.append(random.randrange(1,1000000))
	#sorting the array
	list_arr.sort()
	#searching for the last element for worst case
	some_element=list_arr[1000000-1]
	#search for the element in the LIST
	start_time=time.time()
	print("element found at",binary_search(list_arr,some_element))
	end_time=time.time()
	print("time taken to search in the list",str(end_time-start_time))
	
	#array
	array_arr=array.array('i',list_arr)
	
	#searching for the last element for worst case
	some_element=array_arr[1000000-1]
	#search for the element in the ARRAY
	start_time=time.time()
	print("element found at",binary_search(array_arr,some_element))
	end_time=time.time()
	print("time taken to search in the list",str(end_time-start_time))

