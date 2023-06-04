def binary_search(arr,element):
	low=0
	high=len(arr)-1
	while low<=high:
		mid=int((low+high)/2)
		e=arr[mid]
		if element==e:
			return mid
		elif element > e:
			#search  in the right half
			low=mid+1
		else:
			#search in the left half
			high=mid-1
	return None

if __name__=='__main__':
	arr=[1,2,3,4,5,14,25,36,47,56,67,78,89,345,3456,34567,567890]
	print(binary_search(arr,47))
