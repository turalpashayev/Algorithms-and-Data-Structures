'''
Example how to use Kadane's algorith to find max sum of subarray
'''
array = [1,-3,2,1,-1]
array = [-2,3,2,-1]

def max_subarray(array):
	max_current = max_global = array[0]
	for i in range(1,len(array)-1):
		max_current = max(array[i], max_current + array[i])
		if max_current > max_global:
			max_global = max_current
			position_array = []
	return max_global

# print(max_subarray(array))


'''
How to use Binary Search in a sorted array
'''

arr = [-2,3,4,7,8,9,11,13]

def find_target(array,target):
	left = 0
	right = len(array)-1
	while left <= right:
		mid = (left + right)//2
		if array[mid] == target:
			return mid
		elif target > array[mid]:
			left = mid+1
		else:
			right = mid-1

	return -1

# print(find_target(arr,11))



'''
word searching in 2 dimensional array
'''

board = [['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E']]
word = 'ABCCED'

def word_search(board,word)->bool:
	COLS, ROWS = len(board[0]), len(board)
	path = set()

	def dfs(r,c,i):
		if i==len(word):
			return True
		if (r<0 or c<0 or r>=ROWS 
			or c>=COLS or word[i] != board[r][c] 
			or (r,c) in path ):
			return False
		
		path.add((r,c))
		print(path)
		res = (dfs(r+1,c,i+1) or
			dfs(r-1,c,i+1) or
			dfs(r,c+1,i+1) or
			dfs(r,c-1,i+1)
			)
		path.remove((r,c))
		print(path)

		return res 

	for r in range(ROWS):
		for c in range(COLS):
			if dfs(r,c,0):
				return True

	return False


# print(word_search(board,word))

def anagram(str1,str2):
	list1 = list(str1)
	list2 = list(str2)
	list1.sort()
	list2.sort()
	if list1 == list2:
		return True


def palindorme(str1):
	reversed = str1[::-1]
	if str1 == reversed:
		return True

'''
open close parenthesis
'''
s = '((){}[])}'

def isValid(s:str) -> bool:
	stack = []
	isOpenClose = {')':'(',']':'[','}':'{'}
	for c in s:
		if c in isOpenClose:
			if stack and stack[-1] == isOpenClose[c]:
				stack.pop()
			else:
				return False

		else:
			stack.append(c)

	return True if not stack else False


print(isValid(s))



def wordle(uinput,secret):
	output = ''
	l_uinput = list(uinput)
	l_secret = list(secret)
	# print(l_uinput)
	for i, l in enumerate(uinput):
		if l in l_secret:
			if secret[i] == l:
				output += 'G'
			else:
				output += 'Y'

		else:
		 output += 'R'

	return output


print(wordle('craig','artyu'))
