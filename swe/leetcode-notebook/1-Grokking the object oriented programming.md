Object Oriented Basics

Object-oriented programming (OOP) is a style of programming that focuses on using objects to design and build applications. Contrary to procedure-oriented programming where programs are designed as blocks of statements to manipulate data, OOP organizes the program to combine data and functionality and wrap it inside something called an “Object”.

If you have never used an object-oriented programming language before, you will need to learn a few basic concepts before you can begin writing any code. This chapter will introduce some basic concepts of OOP:

Objects: Objects represent a real-world entity and the basic building block of OOP. For example, an Online Shopping System will have objects such as shopping cart, customer, product item, etc.

Class: Class is the prototype or blueprint of an object. It is a template definition of the attributes and methods of an object. For example, in the Online Shopping System, the Customer object will have attributes like shipping address, credit card, etc., and methods for placing an order, canceling an order, etc.

# Class Code Snippet:

```py
Class ShoppingCart(object):
	def __init__(self):
		self.total=0
		self.items={}

	def add_item(self,item_name,quantity,price):
		self.total+=(quantity*price)
		self.item.update({item_name:quanitty})

	def remove_item(self,item_name,quantity,price):
		self.total-=(quantity*price)
		if quantity>self.items[item_name]:
			del self.items[item_name]
		self.items[item_name]-=quantity

	def checkout(self,cash_paid):
		balance=0
		if cash_paid<self.total:
			return "you paid {} but cart amount is {}".format(cas_paid,self.total)
		balance=cash_paid-self.total
		return "Exchange amount:{}".format(balance)

# Object and it's Uses Code Snippet:

#Driver code
cart=ShoppingCart()
cart.add_item('A',10,50)
cart.add_item('B',5,20)

cart.remove_item('B',1,20)

cart_res=cart.checkout(600)

print('Total cart amount:',cart.total)
print('Cart items',cart.items)

print(cart_res)
```

#Response:
Total cart amount: 580
Cart items: {'B': 4, 'A': 10}
Exchange amount: 20


The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.

Encapsulation: Encapsulation is the mechanism of binding the data together and hiding it from the outside world. Encapsulation is achieved when each object keeps its state private so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.

#Encapsulation Code Snippet:

```py
class Product:
	def __init__(self):
		self.__maxprice=900

	def sell(self):
		print("selling price:{}".format(self.__maxprice))

	def set_max_price(self,price):
		self.__maxprice=price

product=Product()
product.sell()

#change the price
product.__maxprice=1000
product.sell()

#use setter function
product.set_max_price(1000)
product.sell()
```

#Response:

Selling Price: 900
Selling Price: 900
Selling Price: 1000

Abstraction: Abstraction can be thought of as the natural extension of encapsulation. It means hiding all but the relevant data about an object in order to reduce the complexity of the system. In a large system, objects talk to each other, which makes it difficult to maintain a large code base; abstraction helps by hiding internal implementation details of objects and only revealing operations that are relevant to other objects.
#Abstraction Code Snippet:

```py
from abc import ABC,abstractmethod

class Parent(ABC):
	def common(self):
		print("In common method of Parent")

	@abstractmethod
	def vary(self):
		pass

	class Child1(parent):
		def vary(self):
			print('In vary method of Child1')

	class Child2(Parent):
		def vary(self):
			print("In vary method of Child2")



#object of Child1 class
child1=Child1()
child1.common()
child1.vary()

#object of Child2 class
child2=Child2()
child2.common()
child2.vary
```

#Response:

In common method of Parent
In vary method of Child1
In common method of Parent
In vary method of Child2


Inheritance: Inheritance is the mechanism of creating new classes from existing ones.
#Inheritance Code Snippet:

```py
class Person(object):
	def __init__(self,name):
		self.name=n
	def get_name(self):
		return self.name
	def is_employee(self):
		return False

class Employee(Person):
	def is_employee(self):
		return True

#Driver code
emp=Person("person 1")
print("{} is employee:{}".format(emp.get_name(),emp.is_employee()))

emp=Employee("employee 1")
print("{} is employee:{}".format(emp.get_name(),emp.is_employee()))

Response:
Person 1 is employee: False
Employee 1 is employee: True
```



#Polymorphism: Polymorphism (from Greek, meaning “many forms”) is the ability of an object to take different forms and thus, depending upon the context, to respond to the same message in different ways. Take the example of a chess game; a chess piece can take many forms, like bishop, castle, or knight and all these pieces will respond differently to the ‘move’ message.

#Polymorphism Code Snippet:

```py
class Bishops:
	def move(self):
		print("biship can move diagnoally")

class Knights:
	def move(self):
		 print("Knights can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically")
#common interface
def move_test(chess_piece):
	chess_piece.move()

#driver code

#instantiate objects
bishop=Bishops()
knight=Kinghts()

#passing the object
move_test(bishop)
move_test(knight)
```

Response:

Bishops can move diagonally
Knights can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically


Object Oriented Analysis and Design
Object Oriented Analysis and Design is a structured method for analyzing and designing a system by applying object-oriented concepts. This design process consists of an investigation into the objects constituting the system. It starts by first identifying the objects of the system and then figuring out the interactions between various objects.

The process of object oriented analysis and design can be described as:
1.indetifying the objects in a system
2.defining relationships between objects
3.estabilishing the interface of each object
4.making a design, which can be converted to exectuables using object-oriented language



###Object Oriented Analysis and Design
Object Oriented Analysis and Design is a structured method for analyzing and designing a system by applying object-oriented concepts. This design process consists of an investigation into the objects constituting the system. It starts by first identifying the objects of the system and then figuring out the interactions between various objects.

The process of object oriented analysis and design can be described as:

Identifying the objects in a system.
Defining relationships between objects.
Establishing the interface of each object.
Making a design, which can be converted to executables using object-oriented languages.
We need a standard method/tool to document all this information; for this purpose we use UML. UML can be considered as the successor of object-oriented (OO) analysis and design. UML is powerful enough to represent all the concepts that exist in object-oriented analysis and design. UML diagrams are a representation of object-oriented concepts only. Thus, before learning UML, it is essential to understand object-oriented concepts.

Let’s find out how we can model using UML.


What is UML?
UML stands for Unified Modeling Language and is used to model the Object-Oriented Analysis of a software system. UML is a way of visualizing and documenting a software system by using a collection of diagrams, which helps engineers, businesspeople, and system architects understand the behavior and structure of the system being designed.

Benefits of using UML:

1.Helps develop a quick understanding of a software system.
2.UML modeling helps in breaking a complex system into discrete pieces that can be easily understood.
3.UML’s graphical notations can be used to communicate design decisions.
4.Since UML is independent of any specific platform or language or technology, it is easier to abstract out concepts.
5.It becomes easier to hand the system over to a new team.


Types of UML Diagrams: The current UML standards call for 14 different kinds of diagrams. These diagrams are organized into two distinct groups: structural diagrams and behavioral or interaction diagrams. As the names suggest, some UML diagrams analyze and depict the structure of a system or process, whereas others describe the behavior of the system, its actors, and its building components. The different types are broken down as follows:

Structural UML diagrams

Class diagram
Object diagram
Package diagram
Component diagram
Composite structure diagram
Deployment diagram
Profile diagram
Behavioral UML diagrams

Use case diagram
Activity diagram
Sequence diagram
State diagram
Communication diagram
Interaction overview diagram
Timing diagram
Rest of the sections, we will be focusing on the following UML diagrams:

Use Case Diagram: Used to describe a set of user scenarios, this diagram, illustrates the functionality provided by the system.

Class Diagram: Used to describe structure and behavior in the use cases, this diagram provides a conceptual model of the system in terms of entities and their relationships.

Activity Diagram: Used to model the functional flow-of-control between two or more class objects.

Sequence Diagram: Used to describe interactions among classes in terms of an exchange of messages over time.





