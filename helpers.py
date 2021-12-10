def read_file_to_arr(filepath):
	print(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def read_file_to_int_arr(filepath):
	print(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(int(line.strip()))
	return arr

def transpose(matrix):
	rows = len(matrix)
	column = len(matrix[0])
	result = [[0 for i in range(rows)] for j in range(column)]

	for r in range(rows):
		for c in range(column):
			#here we are grabbing the row data of matrix and putting it in the column on the result
			result[c][r] = matrix[r][c]
	return result