import cppimport

mylib = cppimport.imp("mylib") #This will pause for a moment to compile the module
a = mylib.square(9)
print('square 9 = ', a)

print('done')