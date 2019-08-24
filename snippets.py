import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print( 'Arrany :', a , 'with dimension', a.ndim )

b = np.zeros(10)
print(b)

c = np.ones((2,3,4),dtype=np.int16)

print(c)

d = np.zeros((1,3,4), dtype= np.int16)

print(d)

# e = np.eye(100)
#print(e.dtype.name)

customer = {
 "name" : "John Smith",
 "age": 30,
 "is_verified": True
}
customer.update("new" : "test")
print(customer)


