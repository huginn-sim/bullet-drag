g = 32

grains_to_pounds = 1./7000.

def convert(x, f='grains', t='pounds'):
	if f == 'grains' and t == 'pounds':
		return x*grains_to_pounds