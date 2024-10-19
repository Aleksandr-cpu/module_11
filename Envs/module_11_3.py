
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, {self.name}!')

    def describe(self):
        print(f'{self.name} is {self.age} years old.')

def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    info['module'] = obj.__module__

    return info

my_obj = MyClass('John Doe', 30)

info = introspection_info(my_obj)
print(info)

