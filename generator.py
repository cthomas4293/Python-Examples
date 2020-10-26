# Example of how to use Generators
import sys

# define the generator
def my_generator():
	# create an iter 
	for i in range(20):
		# instead of return, have it yield the result
		yield i


# assign the generator func to a variable
step = my_generator()

# loop over the iter using the "next" keyword and
# give it your variable as an argument
for i in range(20):
	print(next(step))
	# each assignment of the iter is only 28 bits
	print(sys.getsizeof(i))


# Generators are best used to maintain low memory usage

a = [i for i in range(20)]

print(a)

# shows that the size of this list is 256 bits
print(sys.getsizeof(a))