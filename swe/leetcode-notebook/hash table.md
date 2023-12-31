#Introduction
Hash Table is a data structure which organizes data using hash functions in order to support quick insertion and search.

There are two different kinds of hash tables: hash set and hash map.

The hash set is one of the implementations of a set data structure to store no repeated values.
The hash map is one of the implementations of a map data structure to store (key, value) pairs.

It is easy to use a hash table with the help of standard template libraries. Most common languages such as Java, C++ and Python support both hash set and hash map.

By choosing a proper hash function, the hash table can achieve wonderful performance in both insertion and search.

In this card, we will answer the following questions:

What is the principle of a hash table?
How to design a hash table?
How to use hash set to solve duplicates related problems?
How to use hash map to aggregate information by key?
How to design a proper key when using a hash table?
And we also provide exercises for you to be familiar with hash table.

The Principle of Hash Table
Report Issue
As we mentioned in the introduction,  Hash Table is a data structure which organizes data using hash functions in order to support quick insertion and search. In this article, we will take a look at the principle of the hash table.

 

#The Principle of Hash Table
The key idea of Hash Table is to use a hash function to map keys to buckets. To be more specific,

When we insert a new key, the hash function will decide which bucket the key should be assigned and the key will be stored in the corresponding bucket;
When we want to search for a key, the hash table will use the same hash function to find the corresponding bucket and search only in the specific bucket.
 
#An Example


In the example, we use y = x % 5 as our hash function. Let's go through the insertion and search strategies using this example:

Insertion: we parse the keys through the hash function to map them into the corresponding bucket.
e.g. 1987 is assigned to bucket 2 while 24 is assigned to bucket 4.
Search: we parse the keys through the same hash function and search only in the specific bucket.
e.g. if we search for 1987, we will use the same hash function to map 1987 to 2. So we search in bucket 2 and we successfully find out 1987 in that bucket.
e.g. if we search for 23, will map 23 to 3 and search in bucket 3. And We find out that 23 is not in bucket 3 which means 23 is not in the hash table.


#Keys to Design a Hash Table
Report Issue
There are two essential factors that you should pay attention to when you are going to design a hash table.

 

1. Hash Function
The hash function is the most important component of a hash table which is used to map the key to a specific bucket. In the example in previous article, we use y = x % 5 as a hash function, where x is the key value and y is the index of the assigned bucket.

The hash function will depend on the range of key values and the number of buckets.

Here are some examples of hash functions:

It is an open problem to design a hash function. The idea is to try to assign the key to the bucket as uniform as you can. Ideally, a perfect hash function will be a one-one mapping between the key and the bucket. However, in most cases a hash function is not perfect and it is a tradeoff between the amount of buckets and the capacity of a bucket.



2. Collision Resolution
Ideally, if our hash function is a perfect one-one mapping, we will not need to handle collisions. Unfortunately, in most cases, collisions are almost inevitable. For instance, in our previous hash function (y = x % 5), both 1987 and 2 are assigned to bucket 2. That is a collision.

A collision resolution algorithm should solve the following questions:

How to organize the values in the same bucket?
What if too many values are assigned to the same bucket?
How to search for a target value in a specific bucket?
These questions are related to the capacity of the bucket and the number of keys which might be mapped into the same bucket according to our hash function.

Let's assume that the bucket, which holds the maximum number of keys, has N keys.

Typically, if N is constant and small, we can simply use an array to store keys in the same bucket. If N is variable or large, we might need to use height-balanced binary search tree instead.


#Exercise
By now, you should be able to implement a basic hash table. We provide the exercise for you to implement a hash set and a hash map. Read the requirement, determine your hash function and solve the collision if needed. 

If you are not familiar with the concepts of hash set and hash map, you can go back to the introduction part to find out the answer.

Insertion and search are two basic operations in a hash table.

Besides, there are operations that are based on these two operations. For example, when we remove an element, we will first search the element and then remove the element from the corresponding position if the element exists.


#Complexity Analysis - Hash Table
Report Issue
In this article, we are going to discuss the performance of hash table.

 

#Complexity Analysis
If there are M keys in total, we can achieve the space complexity of O(M) easily when using a hash table.

However, you might have noticed that the time complexity of hash table has a strong relationship with the design.

Most of us might have used an array in each bucket to store values in the same bucket. Ideally, the bucket size is small enough to be regarded as a constant. The time complexity of both insertion and search will be O(1).

But in the worst case, the maximum bucket size will be N. And the time complexity will be O(1) for insertion but O(N) for search.

 

#The Principle of Built-in Hash Table
The typical design of built-in hash table is:

 The key value can be any hashable type. And a value which belongs to a hashable type will have a hashcode. This code will be used in the mapping function to get the bucket index.
 Each bucket contains an array to store all the values in the same bucket initially.
 If there are too many values in the same bucket, these values will be maintained in a height-balanced binary search tree instead.
The average time complexity of both insertion and search is still O(1). And the time complexity in the worst case is O(logN) for both insertion and search by using height-balanced BST. It is a trade-off between insertion and search.

#Hash Set - Usage

The hash set is one of the implementations of a set which is a data structure to store no repeated values. 

We provide an example of using the hash set in Java, C++ and Python. If you are not familiar with the usage of the hash set, it will be helpful to go through the example.

hashset-usage
```python
#1.initialize the hash set
hashset=set()
#2.add a new key
hashset.add(3)
hashset.add(2)
hashset.add(1)
#3.remove a key
hashset.remove(2)
#4.check if the key is in the hash set
if(2 not in hashset):
	print("key 2 is not in the hash set")
#5.get the size of the hash set
print("size of hashset is:",len(hashset))
#6.iterate the hash set
for x in hashset:
	print(x,end="")
print("are in the hash set.")
#7.clear the hash set
hashset.clear()
print("size of hashset:",len(hashset))
```

#Find Duplicates By Hash Set

As we know, it is easy and effective to insert a new value and check if a value is in a hash set or not.

Therefore, typically, a hash set is used to check if a value has ever appeared or not.

 

An Example
Let's look at an example:

Given an array of integers, find if the array contains any duplicates. 

This is a typical problem which can be solved by a hash set.

You can simply iterate each value and insert the value into the set. If a value has already been in the hash set, there is a duplicate.

 

Template
Here we provide a template for you to solve this kind of problems:

```java
boolean findDuplicates(List<Type> keys){
	//replace Type with actual type of your key
	Set<Type> hashset=new HashSet<>();

	for(Type key:keys){
		if(hashset.contains(key)){
			return true;
		}
		hashset.add(key;)
	}
	return false;
}
```

#hash map-usage
The hash map is one of the implementations of a map which is used to store (key, value) pairs.

We provide an example of using the hash map in Java, C++ and Python. If you are not familiar with the usage of the hash map, it will be helpful to go through the example.

```py
#1.initilize a hash map
hashmap={0:0,2:3}
#2.insert a new(key,value) pair or update the value of existed key
hashmap[1]=1
hashmap[2]=2
#3.get a value of a key
print("the value of key 1 is"+str(hashmap(1)))
#4.deletea key
del hashmap[2]
#5.check if a key is in the hash map.
if 2 not in hashmap:
	print("key 2 is not in the hash map.")
#6.both key and value can have different type in a hash map
hashmap["pi"]=3.1415
#7.get the size of the hash map
print("size of hash map is:"+str(len(hashmap)))
#8.iterate the hash map
for key in hashmap:
	print("("+str(key)+","+str(hashmap[key])+")",end="")
print("are in the hash map.")
#9.get all keys in hash mao
print(hashmap.keys())
#10.clear the hash map
hashmap.clear()
print("the size of hash map is:"+str(len(hashmap)))
```


#Scenario I - Provide More Information
Report Issue
The first scenario to use a hash map is that we need more information rather than only the key. Then we can build a mapping relationship between key and information by hash map.

 

An Example
Let's look at an example:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

In this example, if we only want to return true if there is a solution, we can use a hash set to store all the values when we iterate the array and check if target - current_value is in the hash set or not.

However, we are asked to return more information which means we not only care about the value but also care about the index. We need to store not only the number as the key but also the index as the value. Therefore, we should use a hash map rather than a hash set.

 

What's More
In some cases, we need more information not just to return more information but also to help us with our decisions.

In the previous examples, when we meet a duplicated key, we will return the corresponding information immediately. But sometimes, we might want to check if the value of the key is acceptable first.

 

Template
Here we provide a template for you to solve this kind of problems:


```java
/*
 * Template for using hash map to find duplicates.
 * Replace ReturnType with the actual type of your return value.
 */
ReturnType aggregateByKey_hashmap(List<Type>& keys){
	//replace Type and InfoType with actual type of your key and value
	Map<Type,InfoType> hashmap=new Hashmap<>();
	for(Type key:keys){
		if(hashmap.containsKey(key)){
			if(hashmap.get(key) satsfies the requirement){
				return needed_information;
			}
		}
		//value can be any information you needed
		hashmap.put(key,value);
	}
	return needed_information;
}
```


