#Singleton

Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code.


**Why Singleton considered as anti-pattern?** 
a singleton is basically a way to use global variables. And global variables are bad because any code anywhere in the system can change their values. So when debugging, it can be challenging to figure out which code path leads to the Singleton's current state.

The Singleton class can be implemented in different ways in Python. Some possible methods include: base class, decorator, metaclass. We will use the metaclass because it is best suited for this purpose.

**Another way to implement singleton in python**

Use a module. It is imported only once. Define some global variables in it - they will be singleton's 'attributes'. Add some functions - the singleton's 'methods'.

class Foo(object):
     pass

some_global_variable = Foo()