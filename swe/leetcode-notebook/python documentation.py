5. Data Structures
This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.

5.1. More on Lists
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
add an item to the end of the list.

list.extend(iterable)
list.insert(i,x)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[,start[,end]])
list.count(x)
list.sort(*,key=None,reverse=False)
list.reverse
list.copy()

fruits=['orange','apple','pear','banana','kiwi','apple','banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana',4)
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.pop()

You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python.

Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types. Also, there are some types that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison.

5.1.1 use lists as stacks

the list method make it very easy to use a list as a stack, where the last element added is the first element retrieved(last in first out). To add an itm to the top of the stack, use append. to retreieve an item from the top of the stack, use pop. for example:

stack=[3,4,5]
stack.append(6)
stack.append(7)
stack #[3,4,5,6]
stack.pop() #6
stack.pop() #5
stack #[3,4]

5.1.2use lists as queues
it is also possible to use list as a queue, where the first elements added is the first element retrieved, first in, first out. however, lists are not efficient for this purpose. while appends and pops from the end of list are fast, doing inserts or pops from the begining is slow because all the other elments have to be shifted by one.
to implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

from collection imports deque
queue=deque["Eric","John","Michael"]
queue.append("Terry") #t arrive
queue.append("Graham") #g arrive
queue.popleft() #the first to arrive now leaves
queue.popleft() #the second to arrive now leaves
queue

5.1.3 list comprehension 
list comprehensions provide a consise way to create lists. common application are to make new lists where each elements is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elments that satisfy a certain condition.

For example, assume we want to create a list of squares, like:

square=[]
for x in range(10):
	square.append(x**2)
squares

note that this creates a list of variable named x that still exists after the loop compeltes. we can calculate the list of squares without any side effects using:

map useage:
map(function,iterable,...)

def square(x):
	return x**2
map(square,[1,2,3,4,5])

#labda map():
map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10])
#[3,7,11,15,19]

map(lambda x,y:(x**y,x+y),[2,4,6],[3,2,1])
#[(8,5),(16,6),(6,7)]

当不传function时候，map() is zip()
map(None,[2,4,6],[3,2,1])
#[(2,3),(4,2,),(6,1)]

map(int,(1,2,3))
#[1,2,3]

map(int,"1,2,3,4")
#[1,2,3,4]

map(int{1:2,2:3,3:4})
#提取key [1,2,3]

squares=list(map(lambda:x**2),range(10))
or equivalently:

squares=[x**2 for x in range(10)]

a list comprehension consists of brackets containing an expression followed by a for clause,then zero or more for or if clauses. the result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
#[(1,3),(1,4),(2,3),(2,1),(2,4),(3,1),(3,4)]

and its equivalent to:

combs=[]
for x in [1,2,3]:
	for y in [3,1,4]:
		if x!=y:
			combs.append((x,y))
combs

Note how the order of the for and if statement is the same in both these snipets
if the expression is tuple, it must be parenthesized.

vec=[-4,-2,0,2,4]
#create a new list with values doubled
[x*2 for x in vec]
#[-8,-4,0,4,8]
#fliter the list to exclude negative numbers
[x for x in vec if x>0]
#[0,2,4]
#apply a function to all elements
[abs(x) for x in vec]
#call a method on each element
freshfruit=[" banana"," loganberry","passion fruit"]
[weapon.strip() for weapon in freshfruit]
#The Python strip() method removes any spaces or specified characters at the start and end of a string. strip() returns a new string without the characters you have specified to remove. This example removes all the leading and trailing white space characters in our string.
#['banana', 'loganberry', 'passion fruit']

#create a list of 2-tuple like(number square)
[(x,x**2) for x in range(6)]

#the tuple must be parenthesized,otherwise an error is raised

#flatten a list using a limtcomp with two "for"
vect=[[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]
#[1,2,3,4,5,6,7,8,9]

List comprehensions can contain complex expressions and nested functions:

from math import pi
[str(round(pi,i)) for i in range(1,6)]
#['3.1', '3.14', '3.142', '3.1416', '3.14159']

5.1.4 nest list comprehensions
the initial expression in a list comprehension can be any arbitary expression, including another list comprehension.

Consider the following example of a 3*4 matrix implemented as a list of 3 lists of length 4:

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

[[row[i] for row in matrix] for i in range 4]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

as we saw in prev section the nested listcomp is evaluated in the context of the for that follows it, so this example is eqiv to:

transposed=[]
for i in range(4):
	transposed.append((row[i] for row in matrix))
transposed

which in turn is samed as:

transposed=[]
for i in range(4):
	transposed_row=[]
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
transposed

in real world, you should prefer built in functions to complex flow statement. the zip function would doa great job:

list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

5.2 the del statement
there is a way to remove an item from a list given its index instead of ites value: the del statement. this differs from the pop() method which returns a value. the del statement can also be used to remove slices from a list or clear the entire list(which we did earlier by assignment of an empty list to the slice) for example:

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
#[]

del can also be used to delete entire variable
del a

referenceing a name a hereafter is an error. we will find other uses for del later.

5.3 tuples and sequences
we saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequences data types(see sequence type-list tuple). Since python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple

A tuple consists of a number of values seperated by commas, for instance:

t=12345,54321,'hello!'
t[0]
#12345
t
#(12345, 54321, 'hello!')
#nested
u=t,(1,2,3,4,5)
#((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

#tuples are immutable:
#t[0]=88888
#error

v=([1,2,3],[3,2,1])
v

As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

empty=()
singleton="hello", #note trailing comma
len(empty)
len(singleton)
singleton
#('hello',)

The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:

x,y,z=transposed_row #unpacking
x
y
z

This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

5.4 Sets

python also includes a data type of sets. a set is an unordered collection with no duplicateds elements. basics uses includes membership testing and eliminating duplicates entries. Set objects also support mathematical operation like union,intersection,difference, and symmeric difference.

Curly braces or set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

Here is a brief demonstration.

bastket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#{"orange","banana","pear","apple"}
"orange" in basket
#True

#demonstrate set operations on unique letters from two words
a=set('abracadabra')
b=set('alacazam')

>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

similar to list comprehensions, set comprehensions are also supported:
a={x for x in 'abracadabra' if x not in 'abc'}
a
#{'r','d'}

5.5 Dictionaries
another useful data type built into python is the dictionary(see mapping types-dict) Dictionaries are sometimes found in other languages as associative memories and arrays. unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutibale type; strings are numbers can always be keys. tuples can be used as keys if they only contains strings numbers or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be a key. You cannot use list as keys, since lists can be modified in place using index assignment, slice assignment or method like append() and extend.
It is best to think of a dictionary as a set of key:value pairs, with the reqirement that the keys are unique(within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.
The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you shore using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.
Performing list(d) on dictionary returns a list of all the keys used in the dictionary, in insertion order(if your want it stored, just use sorted(d) instead). To check whether a single key is in the dictionray, use the in keyword.
Here is some example using a dictionray:

tel={'jack':4098,'sape':4139}
tel['guido']=4127
tel
del tel['sape']
tel['irv']=4127
tel
#{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
#['jack', 'guido', 'irv']
sorted(tel)
#['guido', 'irv', 'jack']
'guido' in tel
'jack' not in tel

The dic() constructor builds dictionary dirctly from the sequence of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

in addition, dict comprehensions can be used to create dictionary from arbitary key and value expression:
{x: x**2 for x in {2,4,6}}

when the keys are simple strings it sometimes eaiser to specify pairs using keyword arguments:
dict(saple=4139,guido=4127,jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

5.6 looping
when looping through dict the key and value can be retrieved at the same time use item() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights():
	print(k,v)
#gallahad the pure
#robin the brave

when looping through a sequence, the position index and corresponding value can be retrieved using enumerate() function
for i,v in enumerate(['tic','tac','toe']):
	print(i,v)
#0 tic
#1 tac
#2 toe

to loop over two or more sequence at the same time, the entries can be paired with the zip() function
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
	print("what is your{0} It is {1}.".format(q,z))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

To loop over a sequence in reverse, first specifiy the sequence in a forward direction and then call the reverse() function
for i in reversed(range(1,10,2)):
	print(i)

#9
7
5
3
1

To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

basket=['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
	print(i)

#apple
apple
banana
orange
orange
pear

Use set() on a sequence eliminates duplicate elements. The use of sorted in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

basket=['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	print(f)

#apple
banana
orange
pear

it is sometimes temping to change a list while you are looping over it; however it is often simpler and safer to create a new list instead.

import math
raw_data=[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data=[]
for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)
filtered_data

5.7. More on Conditions
The conditions used in while and if statements can contain any operators, not just comparisons.

The comparison operators in and not in check whether a value occurs (does not occur) in a sequence. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

>>>
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator :=. This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

5.8. Comparing Sequences and Other Types
Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.



6.expressions
Syntax Notes: in this and the following chapers, extended BNF notation will be sed to describe syntax, not lexical analysis. When a syxtax rule has the form, name::= othername
and no semantics are givien, the semantics of this form are the same as for othername.

6.1 Arithmetic conversions
When a description of an arhmetic operator below uses the phrase the numeric argument are converted to a common type, this means that the operator implementations for built-in types works as follows:
`if either augument is a complex number, the other is converted to complex
`otherwise, if either argument is a floating point number, the other is converted to a floating point.
`otherwise, both must be integers and no conversion is necessary.
Some additional rules apply for certain operators(e.g., a string as left argument to the %.)Extensions must define their own conversion behavor.
























8.error and exceptions
until now error messages havnt been more than mentioned, if you tried out examples you have probabily seen some. there are at leas two distinguishable kinds of errors:syntax and exceptions.

8.1 syntax error
8.1. Syntax Errors
Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

>>>
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

8.2. Exceptions
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:

>>>
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what caused it.

The preceding part of the error message shows the context where the exception occurred, in the form of a stack traceback. In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3handling exceptions
it is possible to write programs that hadnle selected eccetion. look at the following example, which asks the user for input until a valid integer has been entered but allows the users to interrupt the porgram(using control c or what ever the operating system supports) note that a user generated interruption is signally by raising the keyboard interrupt excetion. 

while True:
	try:
		x=int(input("plz enter a number:"))
		break
	expept ValueError:
		print("Oops! That was no valid number. Try again")

The try statement work as follows.
`First the try clause the statements between the try and except keywaords is ececuted.
`if no exception occurs, the except clause is skipped and excetion of the try statement is finished
`if an excpetion occurs during exectution of the try clause, the rest of clause is skipped. then if its type mathces the exception named after the except keyword the except clause is executed the and then excution continues after the try/except block.

`if an expcetion occurs which does not match the exception named in the except clause it is passed on to outer try statements if no handler is ofund, it is an unhandled and stops with a message as shown above.

A try statement may have more than one except clause, to specify hadlers for different expcetions. At most one handler will be executed.Handelers only handle exceptions that occur in the coreesponding try clause, not in other handlers of the same try statement. An except clause may name mutiple exceptions as a parenthesized tuple, for exampel:

excpet(RuntimeError, TypeError,nameError):
	pass

A class in an except clause is compatible with an exception if it is the same class or a base class thereof(but not the other way around- an except clause listing a derived class is not compatible with a base class) For example, the following code will print bcd in that order:

class B(Exception):
	pass
class C(B):
	pass
class D(C):
	pass

for cls in [B,C,D]:
	try:
		raise cls()
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")	

Now that if the except clauses were reversed with ecept B first, it would have printed B,B,B-the first matching except claus is triggered.

All exceptions inherit from BaseException and so it can be used to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way. Itt can also be used to print an error message and then re-raise the exception(allowing a caller to handle the exception as well.)

import sys
try:
	f=open("myfile.txt")
	s=f.readline()
	i=int(s.strip())
except OSError as err:
	print("OS error:{0}".format(err))
except ValueError:
	print("could not conver data to an integer")
except BaseException as err:
	print(f"unexpeted {err=},{type(err)=}")
	raise

Alternatively the last excpet clause may omit the exception names, however the exception value must then be retrieved from sys.exc_info()[1].

The try...except statement has an optional else clause, which when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

for arg in sys.argv[1:]:
	try:
		f=open(arg,"r")
	excpet OSError:
		print("cannot open",arg)
	else:
		print(arg,"has",len(f.readlines(),"lines"))
		f.close()

The use of the else clause is better than adding additonal code to try clause because it avoids accidentally catching an excpetion that wasn't raised by the code being protected by try...except statement.

When an eception occurs, it may have an associated value, well known as the exception's argument. The presence and type of the argument depend on the exception type.

The except clause may specify a variable after the exception name. The varibale is bound to an exception instance with the argument stored in instance.argus. For convenience, the exception instance defines __str__() so the arguments can be printed without having to reference .args. One may also instantiate an exception first before raising it and add any attributes to it as desired.

>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

If exception has arguments, they are printed as the last part of the message for unhandled exceptions.

Exceptions handler dont just handle expcetions if they occur immediately in the try clause, but also if they occur inside functions that are aclled in the try clause.

For example
def this_fail():
	x=1/0
try:
	this_fairs()
except ZeroDivisionError as err:
	print("handling run-time error",err)

Handling run-time error: division by zero

8.4raising exceptions
the raise statement allows the programmer to force a specified exception to occur. For example:

raise NameError("Hithere")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere

The sole argument to raise indicates the excepton to be raised. This must be either an exception instance or an exception class.(a class that derives from exception).If an exception class is passed, it will implicitly instatiated by calling its constructor with no argument:

theraise ValueError: # shorthand for 'raise ValueError()'
If you need to determine whether an exception was raised but dont intend to hanndle it, a simpler form of raise tatement allows you to re-raise the exception:

try:
	raise NameError("HiThere")
except NameError:
	print("an exception flew by")
	raise
	
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere


