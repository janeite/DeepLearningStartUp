import numpy

def no_negative(x):
    if x < 0.0:
        return 0.0
    else:
        return x

arr = numpy.random.normal(0.0,1.0,100)
print(arr)
f = numpy.vectorize(no_negative)
print(f(arr))
