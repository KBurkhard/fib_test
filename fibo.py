def fib(n):    # write Fibonacci series up to n
   a, b = 0, 1
   while a < n:
       print(a, end=' ')
       a, b = b, a+b
   print()

   
def fib2(n):   # return Fibonacci series up to n
	"""
	As described by Fibonacci et al.
	doi:..
	
	
	========================
		==========
		-------
		Overlap
	>>> from fib import fib2
	>>> fib2(10)
	[1, 2, 3, 4]

	"""
   a, b = 0, 1
   while a < n:
       result.append(a)
       a, b = b, a+b
   return result