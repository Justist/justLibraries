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

# Returns the amount of dimensions a list/array has.
# As a sArray can have an infinite amount of
# dimensions, this can be used to loop through all of
# them.
def _amountOfDimensions(array):
	i = 0
	copy = array # just keeping it clean
	while 1:
		try:
			copy = copy[0]
		except:
			return i

		i += 1
