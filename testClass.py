class laptop:
    a = 7  # attributes
    b = 'string'  # attributes

    def __init__(self):
        print("_init_ method is like constructor, remember this!")
        self.name = 'John'
        self.age = '30'

    def update_age(self):
        self.age = '35'

    def config(self):
        print("Config() : This is a function, but since we have declared in class it is called method")
        print("Asus Notebook, Inter i7, 16GB Ram, 256GB SSD")

    def meth_with_params(self, param1, param2):
        print("Method with params as input")
        self.param1 = param1
        self.param2 = param2

    def compare_attributes(self, other_object):
        if self.age == other_object.age:
            print('Attributes are equal')
            return True
        else:
            print("Attributes are not equal")
            return False


obj1 = laptop()  # Object OBJ1 Instantiation
obj2 = laptop()  # Object OBJ2 Instantiation
obj1.config()
obj1.meth_with_params(4, 9)  # passing parameters to method
obj1.update_age()  # Update attribute age
laptop.update_age(obj1)  # passing OBJ1 to self to update OBJ1 AGE attribute OBJ2 AGE will not be effected
print(obj1.age)  # Print OBJ1 age
print(obj2.age)  # Print OBJ2 age

## Comparing two OBJ1 && OBJ2 attributes using
result = obj1.compare_attributes(obj2)
if result:
    print("Attributes are same")  ## in case of True
else:
    print("Attributes are not same")  ## in case of False
