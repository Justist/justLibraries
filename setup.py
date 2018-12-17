import sys

if not ((2,7,0) <= sys.version_info[:3] < (3,0,0)):
	raise RuntimeError("At least Python version 2.7 required, but not compatible with version 3.0 or higher!")

def setupFunction():
	from distutils.core import setup

	setupArgs = dict(
		name = 'simonPythonLibs',
		version = '0.0.1alpha',
		author = 'Simon R. Klaver',
		author_email = 'simonrklaver@gmail.com',
		description = 'Custom made libraries of Simon R. Klaver',
		packages=['pythonLibs'],
	)
	
	setup(**setupArgs)
	return

if __name__ == '__main__':
	setupFunction()
