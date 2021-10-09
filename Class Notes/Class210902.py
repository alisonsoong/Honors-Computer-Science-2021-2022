#
# Alison Soong
#
# Implementing a pseudocode
#

#
# Prints out the first n terms of a geometric sequence
#
#       parameters:
#               n, an integer = the number of terms to be printed
#               a_0, an integer = the first term of the sequence
#               m, an integer = the common ratio of the geometric sequence
#
def geoSeq(n, a_0, m):
	# print greeting
	print("Print first",n,"terms of a geometric sequence where")
	print("the initial value is", a_0,"and the common ratio is",m)
	# a_n = next term which starts at a_0
	a_n = a_0
	# repeat n times
	for i in range(n):
		# print a_n
		print(a_n)
		# calculate next term by multiplying a_n by m
		a_n = a_n * m

# to test, try the boundary cases/numbers
# (so like 0, negative numbers, and fractions!)








##Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
##[Clang 6.0 (clang-600.0.57)] on darwin
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> greeting():
##	
##SyntaxError: invalid syntax
##>>> def greeting(n, a_0, m):
##	# print greeting
##	print("Print first n terms of a geometric sequence.")
##	# a_n = next term which starts at a_0
##	a_n = a_0
##	# repeat n timese
##	for i in range(n):
##		# print a_n
##		print(a_n)
##		# calculate next term by mult a_n by m
##		a_n = a_n * m
##
##		
##>>> greeting(3, 2, 4)
##Print first n terms of a geometric sequence.
##2
##8
##32
##>>> def geometricSequence(n, a_0, m):
##	# print greeting
##	print("Print first n terms of a geometric sequence.")
##	# a_n = next term which starts at a_0
##	a_n = a_0
##	# repeat n timese
##	for i in range(n):
##		# print a_n
##		print(a_n)
##		# calculate next term by mult a_n by m
##		a_n = a_n * m
##
##		
##>>> geometricSequence(3, 5, 2)
##Print first n terms of a geometric sequence.
##5
##10
##20
##>>> def geometricSequence(n, a_0, m):
##	# print greeting
##	print("Print first n terms of a geometric sequence.")
##	# a_n = next term which starts at a_0
##	a_n = a_0
##	# repeat n times
##	for i in range(n):
##		# print a_n
##		print(a_n)
##		# calculate next term by multiplying a_n by m
##		a_n = a_n * m
##
### pseudocode:
### print greeting
### a_n = next term which starts at a_0
### repeat n times
###       print a_n
###       calculate next term by mult a_n by m
##		
##>>> geometricSequence(3, 5, 2)
##Print first n terms of a geometric sequence.
##5
##10
##20
##>>> geometricSequence(2, 6, 6)
##Print first n terms of a geometric sequence.
##6
##36
##>>>
