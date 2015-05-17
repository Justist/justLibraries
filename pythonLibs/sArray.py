import sys
from copy import deepcopy

# Defines a list of lists of specified dimensions
# Acts the same as a C++ array definition:
# To create an array[w][x][y][z][etc], the correct call is
# sArray(w, x, y, z, etc)
# The amount of dimensions is, in theory, only limited by
# available memory.
def sArray(*dimensions):
	array = []
	for i in reversed(range(len(dimensions))):
		array = deepcopy(array)
		array = _addLayer(array, int(dimensions[i]))
	return array

# Adds a layer to the array, in reverse order:
# For array[x][y][z] we first have the empty list,
# then we add this z times to another empty list, giving
# an array of [z]. Then this is added y times to
# another empty list, giving [y][z]. Then the same
# for x giving [x][y][z].
# Deepcopy is used to prevent multiple lists having
# the same reference, which would result in multiple
# sublists being changed together when not issued so.
def _addLayer(array, layerCount):
	return [deepcopy(array) for n in range(layerCount)]

# Returns the biggest array element for a given amount
# of dimensions: For an array [X][Y][Z] the correct calls
# of this function are (with bAE being a abbreviation of 
# biggestArrayElement):
# bAE(array, x), bAE(array, x, y), bAE(array, x, y, z)
# with 0 <= x < X, 0 <= y < Y, 0 <= z < Z
# bAE(array, 1, 2) will then return the biggest array element
# of Z elements: Of all elements array[1][2][0 -> Z-1]
#def biggestArrayElement(array, *dimensions):
#	copy = array
#	for i in dimensions:
#		copy = copy[i]
#	#TODO: loop recursively over all (remaining) dimensions, take the global max, and return the indices in a list
#	print _amountOfDimensions(copy)
	
# Returns the amount of dimensions a list/array has.
# As a sArray can have an infinite amount of
# dimensions, this can be used to loop through all of
# them.
def _amountOfDimensions(array):
	i = 0
	copy = array
	while 1:
		try:
			copy = copy[0]
		except:
			return i
		i += 1
	

biggestArrayElement(sArray(4, 4, 5), 1, 2)
