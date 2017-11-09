from concurrent.futures import as_completed, ThreadPoolExecutor
import sys

def sum(x, y):
	result = 0
	for i in range(1, x + 1):
		#print("iterator: " + str(i))
		result += i ** y
	return result

def sum_future(xs, ys):
	result = 0
	pool = ThreadPoolExecutor()
	with pool as executor:
		futures = []
		for index, x in enumerate(xs):
			futures.append(executor.submit(sum, x, ys[index]))
		#print(future.done())
		for future in as_completed(futures):
			result += future.result()
			#print(future.done())
		return result

def sums(xs, ys):
	result = 0
	for index, x in enumerate(xs):
		result += sum(x, ys[index])
	return result

def parseArguments(argv):
	first_file = open(argv[0], "r")
	xs = list()
	for line in first_file:
		xs.append(int(line))
	first_file.close()

	second_file = open(argv[1], "r")
	ys = list()
	for line in second_file:
		ys.append(int(line))
	second_file.close()
	return xs, ys


if __name__ == '__main__':
	xs, ys = parseArguments(sys.argv[1:])

	print(sums(xs, ys))
	print(sum_future(xs, ys))

