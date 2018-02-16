import math
import sys
import time

def test(toTest):
	R = range(2, int(math.sqrt(toTest)))
	wasPrime = 'P'
	for i in R:
		if(toTest % i == 0):
			wasPrime = 'NP'
			return 'NP'
			break
	if(wasPrime == 'P'):
		return toTest
				
			
try:
	num = int(input('Enter a starting Number: '))
	initial = num
	how_many_primes = 0
	while(1):
		result = test(num)
		if(result != 'NP'):
			sys.stdout.write("\r{} is the highest prime, found {} primes since {}".format(result,how_many_primes, initial))
			how_many_primes += 1
			sys.stdout.flush()
			time.sleep(0.1)
			
		num += 1
except Exception as e:
	print('user exit on ' + str(e))
	
