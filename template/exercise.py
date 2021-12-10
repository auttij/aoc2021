import sys
sys.path.insert(0,'..')
import helpers

def exercise1(arr):
	pass

def exercise2(arr):
	pass

if __name__ == "__main__":
	f1 = "input1.txt"
	f2 = "input2.txt"

	filename = f1
	if len(sys.argv) > 1:
		input = sys.argv[1]
		print(input)
		if input == "1":
			filename = f1
		elif input == "2":
			filename = f2

	arr = helpers.read_file_to_arr(filename)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
