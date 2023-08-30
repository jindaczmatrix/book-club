1.选用python实现算法的原因
python作为一门编程语言已经越来越流行，python的爬虫，python的大数据，python的机器学习，python大数据，python机器学习的web框架，一眼望去，皆是python。在最新的编程语言排行榜中，虽然python还有两座大山，
作为一门动态语言，python使用简单方便，无需编译，即写即用，在解决一些简单问题时优势非常明显。
2.算法的作用
程序=算法+数据结构
3.设计的技术
4.读者能达到的效果

第一章 浅谈算法
学习计算机编程，需要解决不会总是简单的计算问题，也不会总是简单的逻辑判断，总会有一些具体，实际的问题需要解决，要解决这些问题，光靠逻辑计算和判断恐怕是不够的，即使勉强达到目的，效率也不会太高，这时候就该算法上场了。

1.1.算法概述
算法的定义：在学计算机时，曾流行一种观点，程序=数据结构+算法

1.2度量算法
衡量一个算法是不是好算法，一般看这个算法的时间复杂度和空间复杂度。时间复杂度决定了算法运行时间的长短，空寂那复杂度决定了计算时所需资源（空间资源）多少。通常很难两者兼顾。根据不同的需求，满足一方面即可。大多数时间都是优先缩短运行时间。

1.2.时间复杂度
一个算法所耗费的时间，从理论上是不能算出来的，必须上机运行测试才能知道，但我们不肯能也没有必要对每一个算法测试，只需要知道哪个算法花费时间多少就可以了。并且算法花费的时间和算法中语句的执行次数成正比例。哪个算法中语句执行次数多，它花费的时间就多。对于时间复杂度，通常是O，以一个长度为n的sList求和为例。遍历一次slist代码如下。
sum=0
for I in sList: #len(SList)=n
	sum+=i;
此时的时间复杂度为O（n）
从长度为n的列表sList中获取两个数，要求两个数的和是一个定量，最直接的算法是嵌套循环，代码如下：
sum=16
for I in sList:
	for j in sList:
		if I+j==x:
			return (I,J);
此时的时间复杂度是o（n*n）当然不是最优，如果三个数的和是定呢？用最笨的办法，时间复杂度是o（n*n*n）

1.2.2 空间复杂度
空间复杂度是对一个算法在运行中临时占用存储空间大小的量度。一个算法在计算机存储器占用的存储空间包括存储算法本身占用的空间，算法的输入输出数据所占用的存储空间和算法运行时临时占用存储空间这三个方面。算法的输入输出数据所占用的存储空间是由要解决的问题决定的，是通过调用函数传递而来的，它不随本算法的不同而改变。
存储算法本身所占用的存储空间和算法书写的长度有关，要压缩，就写出较短的算法，算法在运行过程中临时占用的存储空间因算法而不同，有的算法只需要少数临时工作单元，而且不随问题规模的大小而改变，称这种算法是就地。进行节省存储的算法。
当一个算法的空间复杂度是一个constant，不随着n的大小而改变，可表示为o（1）...

1.3 pythonic
定义：
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
或者可以简单理解为使用python特有的函数，以求100以内所有整数和为例，代码如下：
s=0
i=1
while i<=100
s+=i
	i+=1
这样当然是对的但是这种写法偏c语言风格，如果只看这一部分代码，无法分辨是c，c++，还是python，这不是python风格。比较pythonic的写法如下
s=0
for i in range(101):
	s+=i
>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

这段代码一看就知道是用python写的，但是不够pythonic，eg
list100=list(range(1,101));
s=sum(list100)

2.基础算法之排序
讲到算法，最基础，最简单的大概要数排序了。排序，简单来说就是将一组数列（一般是打乱顺序的int）按照从小到大，或者从大到小顺序重新排列，很简单的一个问题，很多经典的答案，实际运用中，可以有针对性地选择相应的算法为不同的特点序列来排序。
python中的有序序列是列表（元组是不可修改的，无法原地排序），本章就用python的列表展示集中常见简单的经典算法。

2.1冒泡排序
冒泡排序是一种很原始的排序方法，就是通过不断地交换大数的位达到排序的目的。因为不断出现大数类似于水泡不断出现，因此被形象地成为冒泡算法

2.1.1 原理
从一组数列列表中挑选一个最大的数，如果这个数列比较小，还有可能看出，如果比较大呢？那就不好确定。好在冒泡算法不需要直接挑选出最大，只需要从两个里面挑选出比较大的，那就简单了。
冒泡算法的基本原理就是比较相邻两个数字。将两数种比较大的那个数字交换到靠后的位置。不断地交换下去就可以将最大的数字放到队列的尾部。然后重头再次交换，直到数列排成有序数列。
1.第一轮排序
第一次的排序，按照冒泡排序的原理，比较相邻两个数字的大小。从数列头开始，第一次比较7和3的大小。很明显7比3大，交换7，3，较大的那个数7交换到靠后的位置，代码：
if iList[j]>=iList[j+1]:
	iList[j],iList[j+1]=iList[j+1],iList[j]
交换后的结果如图所示：
第二次的排序比较7和5的大小。7比5大，交换7和5，
第三次比较7和1大小，交换7，1，
第四次排序比较7和9的大小，7比9小，无需交换，保持原位。
第五次排序，比较9和4的大小，9比4大，交换9和4的位置。
现在第一轮结束，成功将9交换到了最后的位置。

2.第二轮排序
第二轮排序的重新回到数列开头，重新比较两个数的大小，第一次排序，比较3，5，的大小，3比5小，无需交换位置。第二次排序，比较5，1，5比1大，交换位置。得到的序列是3，1，5，7，4，9.第三次排序是比较5和7的大小，无需交换位置。第四次排序比较7和4的大小，交换位置，得到3，1，5，4，7，9.
不需要第五次排序了。第一轮的排序中保证了最后的最大。因此爹润排序的作用是次大的放到倒数第二。具体这个数列就是把第二大的7放到倒数第二的位置。
3.第三轮排序
依旧是回到数列的开头，重新比较相邻的两个数。第一次排序，比较3，1的大小，新数列为1，3，5，4，7，9，第二次排序，比较3，5，无需交换位置。第三次排序，比较5，4，新数列为1，3，4，5，7，9.本轮排序将第三大的数字5交换到了数列倒数第三的位置。如图2-8所示。
4.第四轮排序
回到开头，比较相邻。第一次比较比较1，3，无需交换，第二次比较，比较3，4大小，无需交换位置。新数列为1，3，4，5，7，9.
5.第五轮排序
在第四列排序时，已经是个有序，理论不需要继续排序，但是程序只能按照设定的步骤继续排序，这轮排序中只需要比较1次就够了。比较数列最开头的两个数1和3的大小，无需交换位置。最终得到了有序数列。
冒泡排序数列完毕，总共六个数字，排序了5轮.可以得到结论，一个n个数需要n-1轮，这样可以确保得到一个有序数列。因此冒泡时间复杂度是o（n^ 2）

2.1.2 代码
在写冒泡排序的代码钱，需要创建一个无需数列的程序，用于测试排序算法，创建无序数列的程序randomList.py，代码如下，

import random

def randomList(n):
	#reutrn a length n list from 0 to 1000
	iList=[]
	for i in range(n):
		iList.append(random.randrange(1000))
	return iList

if __name__=="main":
	iList=randomList(10)
	print(iList)

在ide中运行randomList.py
random.py利用random.randrange函数返回一个设定范围内的int，然后加入到无需数列iList中。最后返回iList列表。
冒泡排序的程序bubbliesort.py的代码如下

from randomList import randomList
import timeit

iList=randomList(20)

def bubbleSort(iList):
	if len(iList)<=1:
		return iList
	for i in range(1,len(iList)):
		for j in range(0,len(iList)-i):
			if iList[j]>=iList[j+1]: #compare相邻数字大小
				iList[j],iList[j+1]=iList[j+1],iList[j]
		#print("第 %d轮排序结果："%i,end="")
		#print(iList)
	return iList
if __name__=="__main__":
	print(iList)
	print(bubbleSort(iList))
	print(timeit.timeit("bubbleSort(iList)","from __main__ import bubbleSort,iList",number=100))


buubleSort.py中第九行导入之前的randomList函数，用于创建一个无序的数列（列表）。第10行，导入了timeit模块，用于测试函数的运行时间，最后显示排序100次用了0.06秒

2.2选择排序
与冒泡排序相比，选择排序算法的原理更加简单粗暴，就是在数列中不断地寻找最小/大的那个数。

2.2.1原理
简单地说，选择排序只做了一件事，就是从数列中选择最大/小的那个数，将这个数放到合适的位置，然后在子数列中找到最大/小的那个数放到合适的位置，然后一直到子数列为空位置。与冒泡不同的是，不是相邻两个数字比较，而是某个数字和所有其他数比较，挑出最小/大的那个数字就好了。还是用熟悉的7，3，5，1，9，4。
1.第一轮 
以数列的第一个数为基数，遍历数列中的其他数字，找到最小的那个数，然后交换两个数的位置，代码类似于：
for i in range(0,len(iList)-1):
	minIndex=1
	for j in range(i+1,len(iList-1)):
		if iList[j]<=iList[minIndex]: #find the smallest index in the sublist
			minIndex=j
本轮排序的结果是将数列中最小的那个数放到了数列的第一位

2.第二轮排序
然后以数列的第二个数为基数，遍历数列中剩余的其他数字，找到最小的那个数，交换这两个数的位置。第二个数字3已经是剩余数列中最小的数了。因此本轮无需交换数字。
3.第n轮排序，按照这个规律，不断地找剩余数列中最小的数字，交换位置，直到将原始数列排成有序数列。

选择数列排序完成，共6个数，排序了5轮，理论上来说，选择排序的时间复杂度是o—n平方，但在python中稍微有点特殊，因为python列表中寻找最小的那个数不需要逐个比较。使用min(iList[i:])就可以得到最小的那个数，所以使用pythonic风格的选择排序，时间复杂度是o-n，因此理论上python版本的排序算法中选择排序算法是最快的。

2.2.2 代码
选择排序的pythonic版本算法程序selectionSort.py的代码如下：
from randomList import randomList
import timeit

iList=randomList(20)
def selectionSort(iList):
	if len(iList)<=1:
		return iList
	for i in range(0,len(iList)-1):
		if iList[i]!=min(iList[i:]) #使用min函数找到剩余数列中最小的那个数
			minIndex=iList.index(min(iList[i:])) #minIndex是最小数的下表
			iList[i],iList[minIndex]=iList[minIndex],iList[i]
		#print("第%d轮排序结果："%(i+1),end="")
		#print(iList)
	return iList

if __name__=="__main__":
	print(iList)
	print(selectionSort(iList))
	print(timeit.timeit("selectionSort(iList)","from __main__ import selectionSort,iList",number=100)

在ide中运行randomList中执行selectionSort.py,结果如图2-17所示。

在selectionSort.py的第19行使用python的分片和min函数快速找到数列中最小数字进行交换，节约了大量时间。和冒泡相比，是数量级的差距。这是因为利用python中的min函数可以一步到位地获取列表中的最小值。如果使用其他编程语言可能效果没有这么明显。

2.3插入排序
插入排序可能是最容易理解的排序了，插入排序方法与打扑克牌的排序很相似。在打扑克时，每取一张新牌，都会与手上已经有的牌相比较，将新牌插入到比自己小的牌后面，在取完所有的牌后，手上已有的牌就是个有序的序列。

2.3.1原理
插入排序首先将数列分成两部分，数列的第一部分为left部分，其他的数为right部分。然后将right部分中的数逐一取出，插入left部分中合适的位置。当right部分为空时，left部分就成为了一个有序数列。代码类似于：
target=iList[right]
for left in range(0,right):
	if target<=iList[left]:
		iList[left+1:right+1]=iList[left:right] #比target大的left部分整体后移1位
		iList[left]=target

1.第一轮排序
首先要做的是把数列分成两部分。left部分是第一个数字，其他的数为right部分，首先在牌堆。首先在牌堆中取出第一张牌，是7。
2.第二轮排序
然后从牌堆中取出第二张牌，牌面是3。将牌面是3的牌放入手中合适的位置。将right部分的第一个数字3插入left部分合适的位置。3比7要小，插到7的前面，如图所示
3.第三轮排序
从牌堆中取出新的手牌插入手中，将新的iList[right]列表元素5插入iList的left部分，5比3大，比7小，所以把5插到3之后，7之前，如图所示。
4.第n轮排序，循环将right部分的数字插入left部分，插入排序数列完毕，插入排序的时间复杂度是o_n^2

2.3.2代码
选择排序的python算法程序insertionSort.py的代码如下:

from randomList import randomList
import timeit

iList=randomList(20)

def insertionSort(iList):
	if len(iList)<=1:
		return iList;
	for right in range(1,len(iList)):
		target=iList[right]
		for left in range(0,right):
			if target<=iList[left]:
				iList[left+1:right+1]=iList[left:right] #使用python切片敷值
				iList[left]=target
				break
		#print(“第%d轮排序结果:” %（right),end="")
		#print(iList)
	return iList

if __name__ == '__main__':
	print(iList)
	print(insertionSort(iList))
	print(timeit.timeit("insertionSort(iList)","from __main__ import insertionSort, iList",number=100))

在ide中运行insertionsort.py结果如图所示，使用python的分片赋值可以很方便地将列表整体移动。插入排序100次使用时间为0.07秒。与冒泡排序使用的时间相当。
2.4归并排序
归并排序 Merge sort是一种典型的递归法排序。它把复杂的排序过程分解为一个简单的合并子序列的过程，至于怎么得到这个字序列，就要自己调用自己了。
2.4.1原理
归并排序首先要做的是将数列分成左右两部分，最好是等分，然后将左右两个子数列排序完毕后再合并到一起就成了一个有序数列。左右两个子数列怎么变成有序数列呢？那就回头调用自己，再把子数列分成左右两部分，然后把子子数列排序完毕后合并成子数列。当子子子。。。数列分到不可再分割的时候，就可以返回开始合并数列了。逐步合并子子子。。。数列，到最后就得到了一个新的有序数列。
还是用7，3，5，1，9，4为例，首先要做的是将这个数列分成基本相等的两部分（列表总数为奇数时候，两个子数列不可能完全相等），代码类似于：
middle=len(iList)//2
left,right=iList[0:middle],iList[middle:]

1.第一次分组
第一次分组后，变成两个子数列left和right，此时的子数列left和right都有3个元素，也不是有序数列，不能合并，所以将子数列继续分解为子子数列。
2.第二次分组
经过第二次分组后，现在的子子数列还有长度为2的数列，无法确定这两个长度为2的是否为有序数列，所以继续往下分组，直到将所有的子数列长度分为1位置。
3.第三次分组
将所有的子子数列都分解为长度为1的子子子数列。
经过三次分组已经将所有的子子子数列都变成了长度为1的数列，现在可以确定这些长度为1的数列必定是有序数列了，然后开始反向合并这些数列。
4.合并两个数列的代码类似于：
while left and right:
	if left[0]>=right[0]:
		mList.append(right.pop())
	else:
		mList.append(left.pop())

这里还要考虑left和right长度不一致的情况，先合并3，5，和9，4
将两个有序子数列合并成1个新的有序数列，还有4个子数列，需要进行第二次合并。

5.第二次合并
将4个子子数列合并成两个子数列，如图2-28所示。
现在还剩下2个子数列，继续进行第三次合并。

6.第三次合并
将剩余的数列合并到一个数列中
归并排序完毕，经过三次合并，最终得到了一个有序数列，归并排序的时间复杂度是o(nlogn)。

2.4.2代码
归并排序的python算法程序mergeSort.py的代码如下

from randomList import randomList
import timeit

iList=randomList(20)

def mergeSort(iList):
	if len(iList)<=1:
		return iList
	middle=len(iList)//2
	left,right=iList[0:middle],iList[middle:]
	return mergeList(mergeSort(left),mergeSort(right))

def mergeList(left,right):
	mList=[]
	while left and right:
		if left[0]>=right[0]:
			mList.append(right.pop(0))
		else:
			mList.append(left.pop(0))
	while left:
		mList.append(left.pop(0))
	while right:
		mList.append(right.pop(0))
	return mList
#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
#list.pop([index=-1]) 默认删除最后一个列表

if __name__ == '__main__':
	print(iList)
	print(mergeSort(iList))
	print(timeit.timeit("mergeSort(iList)","from __main__ import mergeSort, iList",number=100))

代码21-32行的mergeList函数用于合并两个数列。在归并排序中，同样的20个数排序，100次，运行时间是0.0121，这个效率比较低，不过递归的算法效率通常不高。

2.5快速排序
快速排序quick sort算法也是一种递归排序用简单的方法来解决复杂的问题，唯一不太好的地方就是稍微有点浪费空间

2.5.1
以列表任意一个数为基准（一般选择列表中的第一个数），将列表 分为左右（前后）两个子列表左边子列表要比基准数字小，右边子列表要比基准数字大，然后继续把左边子列表和右边子列表按照同样的方法继续分解，比较，一直到分无可分位置，然后按照左边子列表（比基准数小）+基准数+右边子列表（比基准数字大）的方式连接起来。最后得到一个有序的数列。
用7，3，5，1，9，4为例，首先是以数列中的第一个数7为基准，将后面的3 5 1 9 4分为左右两个子数列

1第一次分组
以7为基准，比7小的在左边，比7大的在右边。
此时左边的字序列有3，5，1，4，还需要继续分组。右边的子序列只有一个数9，就不需要再分了。第二次只需要将右边的部分分组排序就可以了。

2.第二次分组
左边的子序列还剩下3，5，1，4，现在以3为基准数，将后面的5，1，4，分成两份，同样是比基准书3小的放在左边子数列，比3大的放在右边子序列。
经过第二次的分组后，左边子序列只有一个数，无需再次分组了。右边子序列还有5，4，还得分一次。

3.第三次分组
将子序列5，4，分组，以5为基准，将3序列分成三个部分，如图2-33所示

现在所有的数都已经分组完毕，只要按照一定的顺序重新组合起来就可以了，组合很简单，就是左边+中间+右边。

4.第一次合并
将子序列合并，具体规则是，left+【base】+right。这里稍微注意，left和right都是序列，而base是一个数字，需要将它序列化
左边是【4】，基准是5，右边是【】，【4】+【5】+【】得到序列【4，5】

5.第二次合并
同样是left+【base】+right，得到一个新的序列，
left=【1】，base=3，right=【4，5】，left+【base】+right得到子序列【1，3，4，5】

6.第三次合并
现在整个序列只剩下三个部分了，left=【1，3，4，5】，base=7，right=【9】，合并后得到新的有序数列
经过三次分组，合并后，得到了有序数列。快速排序的时间复杂度最坏情况下是o_n平方

2.5.2代码
快速排序的算法quickSort.py的代码如下

from randomList import randomList
import timeit

iList=randomList(20)

def quickSort(iList):
	if len(iList)<=1:
		return iList
	left=[]
	right=[]
	for i in iList[1:]:
		if i<=iList[0]:
			left.append(i)
		else:
			right.append(i)
	return quickSort(left)+[iList[0]]+quickSort(right)

if __name__ == '__main__':
	print(iList)
	print(quickSort(iList))
	print(timeit.timeit("quickSort(iList)","from __main__ import quickSort,iList",number=100))

在ide中运行quicksort.py
提示，在分组时，分的三个部分是子数列，基准，子数列，在合并时，必须是数列才能合并，所以24行中需要把基数列表化才能进行合并

在快速排序算法中，20个数字排序100次，运行时间是0.0055。。。

2.6计数排序
计数排序算法并不直接通过比较数字的大小来确定位置，它采用了一个巧妙的方法，选择一个数字为基数，然后统计整个数列中有多少个数字比基准小。如果有n个比基准小。那么基准就放到新数列的第n+1的位置上rList[n]，以【7，3，5，1，9，4】为例，首先要做的事先创建一个与【7，3，5，1，9，4】相同长度的空数列。
iLen=len(iList)
rList=[None]*iLen

原数列第一个数字7为基数，将7插入到新的列表中。
1.第一个数的位置
遍历整个数列，统计出比7小的数的个数。比7小的有3，5，1，4共4个，那么数字7就应该放在新数列的第五位，也就是iList【4】。

2.第二个数的位置
第二个数字是3，统计出数列中比3小的数字的个数。比3小的数字只有1，一个，所以3应该放在第二位，也就是list【1】。

3.第三个数的位置
第三个数字是5，比5小的有3，1，4，三个，因此5应该放在第四位，iList【3】

4.第四个数的位置
第四个是1，应该放在iList【0】

5.第五个数的位置
第五个数字是9，比9小的有5个，9应该放在第六位。ilist5

6.第六个数字的位置
第六个数字是4，小的有3，1，放在ilist2。

将所有数字插入到新数列后，排序就完成了。counting排序复杂度是o(n+k)，k是整数的范围

from randomList import randomList
import timeit

from randomList import randomList
import timeit

iList=randomList(20)

def countingSort(iList):
	if len(iList)<=1:
		return iList
	iLen=len(iList)
	rList=[None]*iLen
	for i in range(iLen):
		small=0 #less than base
		same=0 #same as base
		for j in range(iLen):
			if iList[j]<iList[i]:
				small+=1
			elif iList[j]==iList[i]:
				same+=1
		for k in range(small,small+same):
			rList[k]=iList[i]
	return rList

if __name__ == '__main__':
	print(iList)
	print(countingSort(iList))
	print(timeit.timeit("countingSort(iList)","from __main__ import countingSort,iList",number=100)) 

20个数字排序100次，运行时间为0.01

2.7算法小结
除了简单的经典排序算法，还有堆排序（二叉树排序），希尔排序，基数排序。。。
排序算法比较
冒泡排序 n平方
选择排序 n平方，在python下时间复杂度是 n
插入排序 n平方
归并排序 nlogn
快速排序 nlogn 最坏n平方
计数排序 n+k

第三章 基础算法之查找
查找算法也可以叫做搜索算法。查找算法就是从一个有序数列中找出一个特定的数字，常用于判断某个数是否在数列中，或者某个数字在数列中的位置。

3.1顺序查找
顺序查找是最简单直接的查找算法，从头到尾找

3.1.1原理查找数列操作方式可以分成静态查找，动态查找。静态查找只在数列中查找特定数字，不对数列修改，可以进行排序。静态查找出了返回特定数字是否哦存在，还可以返回特定数字的下表。动态查找，在查找的同时进行插入或者删除操作。因此，动态查找只能返回特定书是否存在当前数列中。

顺序查找是静态查找。因为顺序查找是从头到尾查找，不排列，直接查找。为了统一，采取有序数列，用ilist为例子，顺序查找最坏的情况需要查找len(iList)次才能确认。

1.第一次查找，从ilist0开始，比较查找的数字是否相等，如果相等就返回数字的下表并推出，否则比较入列中的下一个数字。

第一次不等于。

2.第二次查找
如果是c语言只需要指针往后移动，python没有指针，但是更加方便，直接通过下标取出ilist1，不想等，继续下一个数字。一直到等于key，或者比较到结尾ilist【-1】不等于key返回程序

3.第n次查找
在这个简单的ilist数列中可以议案看出key存在，因此返回ilist.index（key）

经过第n次查找，终于在数列中找到了key相等的元素，返回下表，排除可能有多个元素符合情况

3.1.2代码在第二章中使用ramdomlistpy，本章也需要。
还需要一种排序算法将数列变成有序数列，这里采用quicksort

顺序查找算法squentialSearch的代码如下：

from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))

def sequentialSearch(iList,key):
	print("iList= %s" %str(iList))
	print("find the number: %d" %key)
	iLen=len(iList)
	for i in range(iLen):
		if iList[i]== key:
			return i
	return -1

if __name__ == '__main__':
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=sequentialSearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)

在sequentialSearch.py中的第25行中制定了2个key给keys列表
·一个是random.choice（iList）这个key是从iList数列中挑选的随机数，是必定存在的
·另一个是random.randrange（min（iList），max（iList）），这个key随机，存在的概率比较低。

3.2二分法查找
有个经常被拿来练手的猜数字的程序，1-100，如果用户猜错了，提示这个数字比随机数字大还是小。用户继续猜，直到猜到为止，通常第一个数字都是50.因为这样至少排除了一半不可能的数字，继续排除，最大数为100，最多6次一定能猜到。

3.2.1原理
在一个有序数列中查找一个特定的数字，用顺序查找最没效率。查找数列中间那个数字和被查找数字有关。如果小，在后半，否则在前半。下面ilist数列，0到9为例子，假设查找9.

1.第一次查找
ilist的长度为len（ilist）=10，最中间的元素下表就是首元素和尾元素的和除以2，（0+9）//2=4。ilist【mid】就是ilist【4】，第一次比较就是和ilist【4】比较。
显然key比ilist【4】大，在后半

2.第二次查找
后半部分中间元素下表是（5+9）//2=7，所以ilast【mid】是ilast【7】，第二次比较是和ilast7比较，大，所以在后半。后半元素下表是（8+9）//2=8
只剩下2个元素了，再用二分法查找就得不偿失了

3.第三次查找
不再使用二分法了，直接比较两个数字是否和key相等：如果想等就返回该元素的下标，如果不等就返回未找到。

同样是查找9，顺序查找10次，二分法只需要3次，也是最不顺利的情况。效率更高。

3.2.2代码二分法查找算法的binarysearch1.py的代码如下

from randomList import randomList
from quickSort import quickSort
import random

from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))

def binarySearch(iList,key):
	print("iList=%s" %str(iList))
	print("find the number:%d" %key)
	iLen=len(iList)
	left=0
	right=iLen-1

	while right-left>1:
		mid=(left+right)//2
		if key<iList[mid]:
			right=mid
		elif key>iList[mid]:
			left=mid
		else:
			return mid
		if key==iList[left]:
			return left
		elif key==iList[right]:
			return right
	return -1 #debug成功，return -1必须在循环外面
    

if __name__ == '__main__':
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=binarySearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)


在binarySearch的34，35行是为了避免key不在iList里设计的

二分法查找速度要比顺序查找快很多，很容易理解，毕竟顺序查找最坏的情况下，一个长度为n的数列可能会查n次才会找到，key在列表尾部。使用二分法最坏的情况也只是需要log2—n次就够了。二分法查找是比较常用的查找方法之一。

3.3斐波那契查找
斐波那契数列又称黄金分割数列，1，1，2，3，5，8，在数学上，斐波那契数列被递归方法如下定义：f（1）=1，f（2）=1，fn=fn-1+fn-2.越往后相邻两个数字相差趋于0.618.

3.3.1原理
几乎和二分法一样。只是在选取参照点有所不同。以0，1，3，4，5，6，7，8，9位例子，共有10个元素。选择一个比len（ilist）稍大的fib数字，也就是13，比13小一号的fib数就是8，首次选择参照点是ilist8，如果被寻找的key比ilist小，就选去比8小的fib数5，第二个点是ilist5，以此类推。
以ilist为数列，key=7位例子。

1.第一次查找
ilist长度为10，fib里没有10，假定ilist长度13，比13小的fib数是8，也就是参照点是第八个数字，也就是ilist7.因为key比参照点ilist8小，说明被寻找的数在ilist的前面部分。

2.第二次寻找
第二次在ilist【0:8】参照点ilist5，key大于5 说明在ilist【6：8】之间

3.第三次查找
只剩下ilist6，7，无需用fib了，但还是找一次。ilist【6，8】只有两个数字，但是查找确是在ilist6，7，8，这三个数字组成的数列，被查找数列长度是3，参照点是比3小一号的fib数2，也就是被查找数列的第二个数ilist【7】。

fib作为二分法的变种，与二分法不相上下。

3.3.2代码
fib查找的演示程序fibsearch1.py的代码如下：

from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))

def fibonacci(n):
	'''return the last element of the fib seq'''
	fList=[1,1]
	while n>1:
		fList.append(fList[-1],fList[-2])
		n-=1
	return fList[-1]

def fibonacci_search(lst, target):
    size = len(lst)
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return -1

if __name__ == '__main__':
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=fibonacci_search(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)

在fibsearch1.py中使用自定义的fib函数通过遍历k返回一个fib数字fib（k），返回的这个fib（k）可以看成被搜索的数列的长度，而fib（k-1）则是被搜索的数列占参照点的相对位置。在fibsearch1.py 36行生命的mid=left+fib（k-1）则是参照点在ilist数列红的绝对位置，是下标

fib查找利用fib数列的特性不断产生新的参照点，通过对这些参照点比较来确定被查找数的位置。斐波那契查找法是二分法的进阶算法。

3.4插值查找
在被查找数列中选取比较点（参照点）时，二分法采用的是终点，fib法采用的是黄金分割点。二分查找发是最直观的，fib是最美观的，但不是最科学的。如何选取最科学的那个比较点呢？通常情况下被查找数列不是等差的，也不知道等差的差值分布状态，没法确定哪个点是最优解，插值算法则给出了大多数情况下理论最科学的比较点

3.4.1原理
以英语词典位例，如果是要找以a开头的单词。一般都不会从终极那位置开始翻（二分查找），直觉上从前面开始查找。mid=left+(key-iList[left])*(right-left)//(iList(right-left)),不管是哪个字母开头的单词，还是在任意数列中寻找任意数，这个点在大多数就是最优的比较点。

1.第一次查找
以list为被查找数列，key=7为例开始查找
当前ilist=range(0,10),是一个差值为1的等差数列，在差值查找给出的公式中mid为比较点，left为被查找数列首的下表，right为被查找数列列尾的下标
从3-13可以看到，第一次就找找到了，搜索等差数列可能是最快的算法。

2.第二次查找
再来看看等比数列的查找，重新设定ilist=【pow（2，i） for i in range（0，10）】，即ilist=【1，2，4，8，16，32，64，128，256，512】。当前ilist为一个比值为2的等差数列，设置key=128，开始在ilist中查找。
第一次查找没找到，重新在ilist[mid,right]中查找，也就是把left右移到当前mid的位置，然后重新计算mid。第二次还是没找到。把lieft移动到mid的位置，继续查找，效率不如二分法和fib。

3.4.2代码
插值查找的演示程序insertSearch.py

from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))

def insertSearch(iList, key):
	print("iList=%s" %str(iList))
	print("Find the number: %d" %key)
	iLen=len(iList)
	left=0
	right=iLen-1
	 
	while right-left>1:
		mid=left+(key-iList[left])*(right-left)//(iList[right]-iList[left])
		if mid==left:
			mid+=1 #if iList[right] and iList[left] differs a lot, which might cause mid=left, endless loop
		if key<iList[mid]:
			right=mid
		elif key>iList[mid]:
			left=mid
		else:
			return mid
	if key==iList[left]:
		return left
	elif key==iList[right]:
		return right
	else:
		return -1

if __name__ == '__main__':
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=insertSearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)

当ilist数列分布比较大时，mid这个比较点可能会一直都等于left造成死循环，因此需要加入限制条件，在ide运行。插值查找也是二分进阶，如果元素分布比较广插入查找效果不好。

3.5.分块查找
分块查找和以上几种查找方式有所不同，顺序查找的数列可以是无序的；二分查找和斐波那契查找的数列必须是有序的；分块查找介于两者之间，块有序，元素可以无序

3.5.1原理
分块查找首先按照一定的取值范围将数列分成数块，块内的元素可以是无序的，但是块必须是有序的。意思是处于后面块最小元素比前面位置块最大元素大。
重新设置一个iList=【9，17，13，5，2，26，7，23，29】。当前这个数列是无序的。设置被查找key=26.按照分块查找的步骤，首先把ilist分为数块，至少分为两块，否则就和顺序查找没区别了。观察ilist数列，发现最大数不超过30，所以这里按照0-9，10-19，20-29三个区间把ilist分为三块。也可以分成2，4，5块，选择比较方便的好玩。
分完块后，块与块之间有序。block2中的最小13比block1中最大的9大。block1，2，3无序。分完块开始查找。

1.第一次查找
第一次查找是将被查找数key与块的分界相比较（也可以与每个块中最大的元素比较，确认key在哪个块）
被查找数key比block2的分界19大，因此只能在block3查找了。

2.第二次查找
块内的查找比就是对比，也就是顺序查找key

3.5.2代码
blockserarch.py

from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))
indexList=[[250,0],[500,0],[750,0],[1000,0]]

def divideBlock():
	global iList,indexList
	sortList=[]
	for key in indexList
		subList=[i for i in iList if key[0]] #列表推到，小于key【0】的单独分块
		key[1]=len(subList)
		sortList+=subList
		iList=list(set(iList)-set(subList)) #过滤掉已经加入subList的元素
	iList=sortList
	print()
	return indexList

def blockSearch(iList, key):
	print("iList=%s" %str(iList))
	print("indexList=%s" %str(indexList))
	print("Find the number: %d" %key)
	iLen=0 #搜索数列的起点索引
	left=0 #搜索数列的终点索引
	
	for indexInfo in indexList:
		left+=right
		right+=indexInfo[1]
		if key<indexInfo[0]:
			break
	for i in range(left,right):
		if key==iList[i]:
			return i
	return -1

if __name__ == '__main__':
	print(iList)
	divideBlock()
	print(iList)
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=blockSearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)

分块可以看成顺序查找的进阶算法。比顺序查找快

CH4 数组
4.1从排序数组中删除重复
在python中去掉列表重复元素的方法很多，比如用集合set的特性，使用包含in的特性去重

4.1.1算法要求
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
不要使用额外的数组空间，你必须在原地修改输入数组并在o—1额外空间的条件下完成。

eg1:
给定nums=【1，1，2【 函数返回新的长度2，并且原数组nums的前两个元素被修改为1，2
说明，为什么返回数值是整数，输出的答案是数组呢？
请注意，输入数组是以引用方式传递的，意味着在函数中修改输入数组对调用者是可见的。想想内部操作如下。

//nums是引用传递的，不对实际参数做任何备份
int len=removeDuplicates(nums)

//在函数里修改输入数组对于调用者是可见的
//根据函数返回的长度打印出数组中长度范围的所有元素
for(int i=0;i<len;i++){
	print(nums[i]);
}

4.1.2解题思路
题中给出了一个已经排序过的列表，需要原地去重，然后返回新数组长度。要求不用额外空间。
nums已经是排序的列表，相同的元素必定是相邻的。要返回去重后元素的个数，要返回去重后元素的个数，借助python的集合概念，只需要len(set(nums))就足够了。要求新列表前面的元素为去重后的元素，那也不难，只需要将nums中相邻的元素比较即可，重复的相邻的两个元素，则将后面那个元素排到列表尾部就可以了。注意比较香玲两个元素不需要从头到尾，只需要比较到len（set（nums））就足够了。后面的列表nums【len（set（nums））：】必然都是重复的元素，不需要浪费时间比较了。设置【0，0，1，1，1，2，2，3，3，4】，首先要做的是去重，确定比较元素的边界，也就是len（set（sum））。
然后从列表头开始，一直到len（set（sum））为止，比较相邻元素。如果发现相邻的元素相等，就把后面部分整体向前移动一位。当前len（set（sum））=5，所以只需要从sum【0=比较到sum4就够了。sum【4】后面的元素sum【5:】必然都是重复的元素。首先开始比较sum【0】和sum【1】
用切片，可以把sum【2:】全体往前移动一位，把sum【1】移动到sum列表的尾部。全部移动到位后，新的sum列表为【0，1，1，1，2，2，3，3，4，0】。
sum【0】和sum【1】比较完毕。下一步是sum1和sum2.一次比较，一直到sum【len（set（sum））-1】，也就是sum4为止。

4.2买卖股票的最佳时期 II
4.2.1 算法要求
给定一个数组，它的第i个元素是一支给定股票第i天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能多次买卖。但不能同时参与多笔交易。

eg1:输入【7，1，5，3，6，4】
输出：7
在第二天，价格=1买入，在第三天，价格=5卖出，这笔交易所能获取利润5-1=4
随后，在第四天，价格=3买入，第五天，价格=6卖出，获得利润3

输入【1，2，3，4，5】
输出 4
第一天买入，第五天卖出，获得利润4

输入【7，6，4，3，1】
输入 0

4.2.2解题思路
要获取股票买卖的最大利益，只需要买入的价格低于卖出的价格就可以了。代入题目中就是数列中的某个元素小于它之后的元素，就认为有利可图。eg 【9，5，2，7，3，6，8】。price0=9，price1=5，只有相邻两个数字中后面数字大于前面的数时（例如prices【2】=2小雨prices3=7，股票才是盈利的。
一旦数列后面的数小于前面的数字，交易就是亏损的。
如果数列后面的数越来越大呢？以prices【4:】为例子，prices【4】=3，小于prices5=6，小于prices6=8.第四天买入，第五天第六天卖出盈利，此时怎么办？多次交易的利润就是相邻两次交易的和。
因此在此题中将总利润设置为0，比较相邻两元素。如果后面的元素大于前面的元素，就把差加入到总利润。如果后面的元素小于前面的元素，就进行下一轮比较。

代码第10行的profit是单次交易利润。在这道题中之需要关心当前交易是否盈利。至于之后是亏损还是盈利无关。统计所有盈利的和就是所能获得的最大利润。

4.3旋转数组
给定一个数组，将数组中的元素向右移动k个位置，其中k大于0.

eg1:
输入【1，2，3，4，5，6，7】和k=3
输入【5，6，7，1，2，3，4】

4.3.2解题思路
至少要三种算法达到目的。仔细看一下要求，实际就是将列表尾部的元素添加到列表头部，而且按照给出的例子，添加到列表头部的这部分子列表还是原来的顺序

1.颠倒列表弹出添加元素
以示例中的数组nums=【1，2，3，4，5，6，7】为例。当k=1时，需要将数组尾部的元素7移动到nums0的位置。nums中其他的元素逐个往后变成7，1，2，3，4，5，6。
在python中把列表尾部的单个元素取出来很容易，使用list的函数pop（）就可以了。即使想取出列表头部的元素，也可以用pop（0）来取得，但想把一个元素插入到列表的头部就比较麻烦了。倒是把一个元素追加到列表尾部比较容易。使用list的内建函数append(n)就能做到。那么，将整个列表颠倒一下所有的问题解决。颠倒列表后，问题就变成了从列表头取出一个元素，然后把元素追加到尾巴。一个pop（0）和一个append（n）就解决了问题。按照题目问题，将k个元素追加到颠倒的列表尾巴后，将列表再颠倒一次就可以了。将列表整体颠倒有个方便的内奸函数reverse（）。
首先要做的就是先将列表颠倒一下。
按照题目要求，将k个元素逐个弹出追加到列表尾巴后，再次颠倒列表。
经过两次颠倒列表后得到了题目所要求的列表。

2.逐个移动元素
颠倒列表是一个取巧，现在来试一下笨办法。按照题目要求把尾巴插入头部。获取尾巴使用pop（）。插入稍微复杂点，使用切片赋值，将出了队列尾巴的所有整体往后移动。然后把取出的列表尾巴元素赋值给列表头。
经过k轮的取列表尾插入后，就得到了题目要求的列表。这个方法但是避免了颠倒。

3.整体移动元素块
按照示例中的最终结果，移动后的列表元素顺序并没有变化。直接一步到位地移动所有元素不是更简单吗？需要移动k个元素，直接把列表尾巴的k个元素整体移动到列表头部就好了。
这种方法可以一步到位，在数组很长，移动的元素比较多的情况下，理论上这种方法是最快的。

4.3.3解题代码
1.运行颠倒列表法
颠倒列表的rotate函数如下所示

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
        	return
        k=k%len(nums)
        temp=nums[len(nums)-k:] #5,6,7
     	nums[k:]=nums[:len(nums)-k]
        nums[:k]=temp
        return

4.4存在重复
4.4.1算法要求
给定一个整数数组，判断是否存在重复元素。如果任何值在数组中出过至少两次，函数就返回True。如果数组中每个元素都不相同，就返回False.
eg1 输入【1，2，3，1】
输出 true

4.4.2解题思路
判断一个数字在数列中有没有重复，最直接的想法是包含判断。nums=【1，2，3，4，5，6】

1.包含判断
包含判断很粗暴，从头到尾遍历所有元素，判断元素是否包含在它之后的部分列表中，用in判断就可以了。
遍历整个列表，只要有一个if判断条件成立，就说明至少有一个数是重复的，函数就可以返回True了。如果一直到nums【len（nums）-1】都没返回false，则说明没重复。
2.排序比较判断
首先把列表排序，如果相同，必然是相邻。然后遍历列表，判断相邻的元素是否相同就可以了。
遍历列表，相邻的元素有相等的函数返回true，没有则返回false

3.集合判断
这个方法利用了python独有的类型set的特性。有一个常用的python小窍门，排除nums中的重复元素。用nums=list（set（nums））就可以轻松拍出了。因此如果想判断一个列表中是否有重复的元素，只需要比较一下集合化之前和之后的长度就可以了。

4.4.3
1.包含判断方法的containsDuplicate函数的代码如下：
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:]:
                return True  
        return False

2.运行排序比较判断法
排序比较判断法的comtainsDuplicate函数的代码如下

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
        	if nums[i]==nums[i+1]:
        		return True
        return False

3.运行集合判断法：
集合判断法的代码如下：
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))==len(nums):
        	return False
        else:
        	return True
       

4.5只出现一次的数字
4.5.1 算法要求
给定一个非空整数数组，除了某个元素只出现一次以外，其余某个元素出现两次，找出那个只出现一次的元素。
说明：
你的算法应该具有线性时间复杂度，可以不使用额外空间吗？
eg1:
输入【2，2，1】
输出 1

eg2 
输入 【4，1，2，1，2】
输出 4

4.5.2解题思路
本题和上面的存在重复一题有点相反：一个是判断重复，一个是返回不重复。因此存在重复使用的方法稍微修改一下在本题中同样有效。nums=【4，1，2，3，1，2，3】为例。

1.排序比较判断
和上题类似。排序完成后，比较相邻两个元素，将nums排序后，nums变成【1，1，2，2，3，3，4】。
遍历列表，逐组比较（每两个元素为一组）。组内（相邻两个）元素相等则比较下一组，一直比较到不相等的元素出现为止，或者最后一个元素只出现一次的数字

2.集合交叉法：
集合交叉法虽然利用了集合的特性，但也需要排序。排序后利用列表的slice method，按照下表的奇数偶数将nums分成两个不同集合。
这两个集合绝大部分元素都是相同的，两个集合的差就是单独的那个元素（因为其他的元素都出现了两次，按照排序后的列表切片方法，出现两次的元素分别在两个集合中出现一次）。

4.5.3解题代码

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        if length<3: #防止出现nums比较短的情况，比如nums=【1】。
        	return nums[0]
        i=0
        while i<length-2:
        	if nums[i]!=nums[i+1]:
        		return nums[i]
        	else:
        		i+=2
        return nums[-1]
排序比较，通用，常规，建议使用。

2.运行集合交叉法

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=list(set(nums[::2])-set(nums[1::2]))[0]
        return n

#seq[::n]是每一个序列n个项的整个序列中。

4.6 两个数组的交集II
4.6.1 算法要求
给定两个数组，编写一个函数计算相交集。
eg1:
输入nums1=【1，2，2，1】，nums2=【2，2】
输出【2，2】
eg2:
输入nums1=【4，9，5】，nums2=【9，4，9，8，4】
输出【4，9】
说明：
输出结果每个元素出现的次数应该与元素在两个数组中出现的次数一致。
可以不考虑输出结果的顺序。

follow-up：
·如果给定的数组已经排好序？如何优化？
·如果nums1的大小比nums2小很多，哪种方法更优？
·如果nums2的元素存储在磁盘，内存有限，并且你不能一次加载所有的元素到内存中，你该怎么办？

4.6.2解题思路
如果只要求返回交集的元素就非常简单了，直接用python的list（set（nums1）&set（nums2））就搞定了；但题目还要求返回元素的个数，包括相同的交集元素。那就只能按步就规地一步一步算了。以 nums1=【1，2，2，1】，nums2=【4，1，2，3，1，2，3】为例。

1.排序求交集
首先要做的当然是排序，分别给nums1和nums2排序，然后在两个列表中按顺序各取出一个元素来比较.

比较的结果不相等，说明该元素不是交集。哪个列表取出的元素比较小，就取出这个列表中的下一个元素（类似于c语言中的指针往后一位），代替之前的元素，因为列表已经排序过了，下一个元素必定不小于前面的元素。
比较的两个元素相等时，说明这元素是交集元素，将这个元素加入到交集列表中，然后nums1和nums2同时取出下一个元素继续比较。

一直到某个列表所有的元素比较完毕为止。此时交集列表rList就是nums1和nums2列表的所有交集。

2.两列表长度相差大求交集
如果两个列表长度相差很大，就没有必要排序了，可以使用更加简单的办法来获取交集元素。不过首先要做的是确定哪个是长度短的列表。在函数未接受参数前，并不知道哪个列表的长度比较长，因此只有假设nums1的长度要远小于nums2的长度。即使实际情况不是如此，在函数中也要让运行情况如此。

然后遍历长度短的那个列表nums1.将元素取出后nums2中是否包含这个元素，如果不包含则比较nums2中的下一个元素（这里不需要排序，也无所谓元素的大小）。如果包含，则说明nums1取出的这个元素就是交集元素。在nums2中删除这个元素后，继续比较nums1列表的下一个元素。
一直到nums1所有元素都测试完毕为止。这种方法仅适用于nums1比nums2短很多的情况。

4.6.3
1.运行排序求交集
排序求交集的intersect函数的代码如下

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rList=[]
        nums1.sort()
        nums2.sort()
        p1=0 #point for nums1
        p2=0 #point for nums2

        while p1<len(nums1) and p2<len(nums2):
        	if nums1[p1]<nums2[p2]:
        		p1+=1
        	elif nums1[p1]==nums2[p2]:
        		rList.append(nums1[p1])
        		p1+=1
        		p2+=1
        	else:
        		p2+=1
        return rList

代码中第9，10行保证了nums1和nums2是有序的，然后进行比较来获取交集。

2.长短列表求交集法interset函数代码如下：
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rList=[]
        
        if len(nums1)>len(nums2):
        	nums1,nums2=nums2,nums1
        for n in nums1:
            if n in nums2:
                rList.append(n)
                nums2.remove(n)
        return rList

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums.append(nums1[i])
                nums2.remove(nums1[i])
        return(nums)

代码25，26保证了nums1是长度比较短的列表。在运行后发现排序求交集法的运行时间要短一点。这是因为两个列表比较短，长度相近，如果两个列表都比较长，长度悬殊，那么排序法花的时间可能就比较长了，毕竟排序也是需要时间的。

4.7 加一
4.7.1 算法要求
给定一个由int组成的非空数组所表示的非负整数，在该数的基础上+1.
最高位数字存放在数组的首位，数组中每个元素只存储一个数字。
你可以假设除了int 0之外，这个整数不会用零开头。

eg1:
输入【1，2，3】
输出【1，2，4】
解释，输入数组表示数字123

4.7.2解题思路
这是一个简单的数学题，把列表中的数字+1就可以了。唯一需要注意的是进位问题。如果列表最后一位是9，就需要进位了。倒数第二为也是9，就又要向前进一位，以此类推。最极端情况是列表的所有数都是9，进行加一操作后，每一位都需要进位，最后得在列表前面添加一个1.

1.倒序法加一
要知道，在列表的尾巴添加元素很简单，而在列表的头部添加元素可能稍微复杂点。因此可以使用倒序的方法来为列表化的数字进行加一操作。eg digits=【9，9，9，9】为例，999+1=1000，首先要做的是把digits倒序，得到倒叙列表【9，9，9】。虽然倒叙前后列表看似相同，但是不同。
这样就把digits在尾巴+1，在头部的进位插入，变成了digits.reverse（）的头部+1，尾部追加操作。当+1操作完步后，再次把digits倒叙一次就得到了最终的答案。
这道题不用倒叙+1也可以。但是使用倒序会简单方便，更容易理解。有些编程语言插入操作没有追加操作方便。所以使用两次倒序来解答可能适应性更广。

2.转换数字+1
抛开列表这个概念，这道题就是一个数字问题。那么将列表转换成数字困难吗？很明显都不难。因此只需要解决这个三个不难的小问题，这道题也就完成了。
因为列表代表的数字是一个整数，在转换列表时不存在损失精度的问题，所以转换后+1也是不错的方法。

4.7.3解题代码
1.运行倒序法+1

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        flag=True #plus one flag
        for i in range(len(digits)):
        	if flag==True:
        		if digits[i]==9:
        			digits[i]=0
        		else:
        			digits[i]+=1
        			flag=False
        if digits[-1]==0:
        	digits.append(1)
        digits.reverse()
        return digits

第八行，flag是加一标识。当指针指向列表的首位时，执行的是题目中要求的+1操作。指针指向其他位置的时，flag为true是因为列表前面一个数字是9，加法进位+1.加入前面一个数字不是9，就无需进位，flag设置为flase。

2.运行转换数字+1

join()方法语法：

str.join(sequence)
参数
sequence -- 要连接的元素序列。
返回值
返回通过指定字符连接序列中元素后生成的新字符串。
实例
以下实例展示了join()的使用方法：

实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
以上实例输出结果如下：

a-b-c

class Solution(object):
    def plusOne(self, digits): #[1,2,3]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits] #["1","2","3"]
        n=int("".join(digits))  #123
        n+=1 #124
        rList=[int(i) for i in list(str(n))] #使用list（str（n））返回的列表元素是字符，需要利用列表生成式将所有元素转换成数字
        return rList #[1,2,4]

4.8 移动零
4.8.1
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。

eg：
输入【0，1，0，3，12】
输出【1，3，12，0，0】
说明：
1.in-place
2.尽量减少操作次数

4.8.2 解题思路
本题的要求就是将列表中的0移动到列表尾巴。如果不是限制必须在原数组中操作，这道题就非常简单了。重新声明一个数字，将nums中的非零数字追加到新数组中，最后返回新数组就可以了。加上了必须在原数组上操作，那就只能老老实实移动元素了。

1.双指针
本题的正规解法应该是遍历列表，遇到非0，列表下标后移以为遇到0，则将0后面子列表前移1位，继续检查当前下标指针所指数字，防止有相邻两个0的情况，然后把列表尾巴设置为0.
这个方法有个问题，当移动到最后，列表的尾巴有2个以上的0时，它会不停将列表后面的0向前移动1位，继续检查当前下标。当前下标指定数字继续为0，就在此移动列表尾巴的0，陷入死循环。
解决这个问题的方法就是使用双指针：一个指针统计非零的元素，一个指针统计所有使用过的元素。当所有元素使用完毕时非零的元素就排列完毕了。以【0，1，0，3，12】为例。

从图47可以看出，left指针是遇0止步，left统计的为非零。right指针每步进1，统计的是所有元素。当right遍历了所有，说明所有0移动到了末尾。

2.删除追加法
这种方法很典型，简单粗暴，就是遍历列表，遇到0后就在列表删除一个0，然后在尾巴添加一个0。因为python在列表删除某个元素是按照顺序删除的，所以会删除第一个遇到的0，也就是刚才遍历列表时遇到的那个0，循环执行此操作，一直到列表尾巴。
这种操作不完美的地方是，列表尾巴添加的0在遍历列表时会再次被删除添加一遍。sums【3】是0，它被移动了2次（也可以用nums。count（0）先统计出0出现的次数，除非nums0中0大量出现，否则也快不了多少

4.8.3解题代码
1.运用双指针法：
双指针法的moveZeroes函数的代码如下：

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right<len(nums)-1:
        	if nums[left]==0:
        		nums[left:-1]=nums[left+1:]
        		nums[-1]=0
        		right+=1
        	else:
        		left+=1
        		right+=1
        return

2.运行追加删除法
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for n in nums:
        	if n==0:
        		nums.remove(0)
        		nums.append(0)
        return

4.9 两数之后
4.9.1 算法要求
给定一个整数数组nums和一个目标target，请在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，但是你不能重复利用这个数组中相同的元素。

示例：
nums=【2，7，11，15】，target=9

因为nums0+nums1=2+8=9
所以返回【0，1】

4.9.2解题思路
1.两数和常规算法
求两数之后等于目标值，常规的做法是嵌套循环nums列表。用两个for循环，分组取出两个数字之后。然后和target做比较，如果相等，就返回两个数的下标。复杂度o-n平方。nums=【2，7，11，15】，target=9为例。
好处简单明了，坏处是比较费时。

2.两数和简化算法
两数之后和等于target，可以列为numsi+numsj=target。转换一下就可以得到numsi=target-numsj。现在只需要遍历一次nums，确定两数差是否在子列表就可以了。遍历nums【i】，然后定位target-numsi的位置，也就是下标j的值。
这样两次循环简化成了一次。

4.9.3
1.常规

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
        	for j in range(i+1,len(nums)):
        		if nums[i]+nums[j]==target:
        			return [i,j]

2.简化版
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
        	if target-nums[i] in nums[i+1:]: #利用python的in运算，来获取numsj的值
        		j=nums[i+1:].index(target-nums[i]) #利用index函数获取差值在nums[i+1:]中的相对序号j
        	return [i,i+j+1] #返回时通过计算j在列表的绝对序号i+j+1

two sum简化算法先利用python的in运算，来获取numsj的值，然后利用index函数获取差值在nums[i+1:]中的相对序号j，返回时通过计算j在列表的绝对序号i+j+1.相比常规算法，o-n节约时间。

4.10有效的数独
4.10.1 算法要求
判断一个9*9的数独是否有效，只需要根据以下规则验证填入的数字是否有效即可。
·1-9在每一行列出现一次
·1-9在每一个粗实线3*3宫内只能出现一次

这是一个部分填充的有效的数独。数独部分空格已填入了数字，空白格用"."表示。

说明：
·一个有效的数独不一定是可解的
·只需要根据规则验证填入的数字是否有效即可
·给定数独序列之包含1-9和字符"."
·给定数独9*9

4.10.2 解题思路
按照题目要求，只能遍历。首先将9x9的数独按照行列块分解开来。
然后按照行列块将数独分别存入一个二维数组中。其中存入行的数据最好办，将board换个名字就是按行分解的二维数组。以遍历的方式将board的元素存入而为行数组rows的代码如下：
for I in range(9):
	for j in range(9):
		rows[i].append(board[i][j])
存入列的数据稍微麻烦点。board本身就是一个二维数组。每遍历board的一行，而位列数组column是能促成纳入一个元素，其代码如下：

for I in range(9):
	for j in range(9):
		columns[j].append(board[i][j])

存入块是最麻烦的。因为按照块的分布，没有行列那么规律。第0块的数据需要存入到block【0】去。因此blocks【0】=【board【0】【0】，board01，board02，board10，board11，board12，board20，board21，board22】。按照这个规律，可以退出blocks【i//3*3+j//3】=boardij。因此按照块存入数据的代码如下。

for I in range(9):
	for j in range(9):
		blocks[i//3*3+j//3].append(board[i][j])
将board按照行列块存入rows，columns，blocks后，遍历行列块，用比较集合前后的长度就可以得知有没有重复的数字。

4.10.3解题代码

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[[] for i in range(9)] #使用列表推导创建了9个空白的子列表难，将1维列表变成了2维
        columns=[[] for i in range(9)]
        blocks=[[] for i in range(9)]

        for i in range(9):
        	for j in range(9):
        		if board[i][j]==".": #排除空白的位置
        			pass
        		else:
        			rows[i].append(board[i][j])
        			columns[j].append(board[i][j])
        			blocks[i//3*3+j//3].append(board[i][j])
        for B2L in rows,columns,blocks:
        	for subList in B2L:
        		if not len(subList)==len(set(subList)): #用集合后比较长度的方式来判断是否有重复的数组
        			return False
        return True

4.11 旋转图像
4.11.1 算法要求
给定nxn的二维矩阵表示一个图像。
将图像顺时针旋转90度。
in-place

例子1:
matrix=【【1，2，3】，【4，5，6】，【7，8，9】】
原地旋转变为：【【7，4，1】，【8，5，2】，【9，6，3】】

4.11.2 解题思路
这道题还是找规律，将一个二维数组旋转后和原数组比较。得到规律，然后验证这个规律是否正确。首先以3x3二维数组做测试。

以a-ij来表示二维数组的元素。基本上就是将二维数组的行转换为列。稍有不同的是，转换后的列是倒序的。那么这道题只需要简单的行列互换，然后将转换后的二维数组中的数组元素倒序一下就可以了。

4.11.3 解题代码

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
        	for j in range(i+1,len(matrix)):
        		matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
        	matrix[i].reverse()
        return

很简单的行列互换，然后倒序二维数组中的整组元素。


第五章 字符串
字符串在算法中出现的很频繁。在开始练习算法前，要先说明的是在python字符串中是不可变的，这点很重要。以s=“abc”为例子，s中单独的元素是不可修改的，不能直接赋值，比如s【2】=‘b’为s中的元素重新赋值，这是不允许的。也不能用切片，或者其他的方法修改s中元素的值。但是字符串s可以整体重新赋值，比如s=“cba”是允许的。

5.1反转字符串
5.1.1算法要求
编写一个函数，其作用是将输入的字符串翻转过来。输入字符串以char【】给出。in-place，o-1解决问题。
你可以将定数组中所有字符都是ascii码表中的可打印字符。

eg1:
输入[“h”,"i"]
输出["i","h"]

5.1.2解题思路
1.常规解法
按照题目的要求必须原地修改。也就是说，先创建新列表，然后将新列表改名的方法是不行的。先看看列表修改前和修改后有什么联系再说，以s=["s0","s1","s2","s3","s4"]为例子。
可以看出反转字符串就是以中间为轴，交换两边的元素位置。应用到这里，就是s0和s4交换位置，s1和s3交换，s2不变。交换次数为len（s）//2次。比较简单，就是一个交换列表元素的问题。

2.pythonic算法
python内置copy，count，sort，reverse。使用reverse函数。

5.1.3
1.常规代码

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length=len(s)
        if length<2:
        	return
        for i in range(length//2):
        	s[i],s[length-i-1]=s[length-i-1],s[i]
        return

常规算法通过，第7-8行是为了避免列表太短而抛出异常

2.pythonic算法代码

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return

5.2整数反转
5.2.1算法要求
给出一个32位有符号整数，将这个整数上的每位上的数字进行反转。

示例1:
输入 123
输出 321

输入 120
输出 21

假设only存储32位的有符号整数，则范围是[-2^31,2^31-1]。根据这个假设，如果反转后整数溢出就返回0。

5.2.2解题思路
1.数学解法
以x=123为例，最终需要返回的结果是321。如果把123转换成321呢？可以把x除以10，得到的余数是3，也就是所需要结果的第一位。把所得的商12继续除以10，得到余2，也就是所需要的第二位。所得的商是1，还是除以10，得到的余数为1.就是所需结果的第三位。实际就是一个不断取余的过程。
最后将列表中的数取出来，按位数乘以10的幂就得到了被颠倒的正数。

2.字符串解法
字符串解法比较简单，就是把整数字符串化，变成列表。通过列表的reverser函数，或者切片将字符串颠倒。最后把字符串转换成整数。
因为字符串就是一个特殊的列表（不可修改元素，但可以整体重新赋值）。这里把字符串变成列表的目的只是反转，不是修改，所以不需要将字符串完全变成列表，可以用字符串反转赋值。

5.2.3解题代码

1.数学解法代码
#用python3解决range过大问题
class Solution:
    def reverse(self, x: int) -> int:
        rList=[]
        minus=False #false if positve, true if negative

        if x<0:
        	minus=True
        	x=x*(-1) #transform negative to positive

        while x//10 !=0: #将x绝对值倒序加入列表
        	rList.append(str(x%10))
        	x=x//10
        rList.append(x)

        length=len(rList)
        rNum=0
        for i in range(length): #列表还原成数字
        	rNum+=int(rList[i])*pow(10,length-i-1)

        if minus:
        	rNum=rNum*(-1)

        if rNum in range(pow(2,31)*(-1), pow(2,31)-1): #用python3解决range过大问题
        	return rNum
        else:
        	return 0

2.字符串解法代码
class Solution:
	def reverse(self, x: int) -> int:
		tList=list(str(x))
		if tList[0]=="-":
			rNum=int("".join(tList[1:][::-1]))*(-1) #reverse list
		else:
			rNum=int("".join(tList[::-1]))	   #reverse list
		if rNum in range(pow(2,31)*(-1),pow(2,31)-1):
			return rNum
		else:
			return 0

转换为字符串后，使用slice反转字符串重新赋值

5.3字符串中的第一个唯一字符
5.3.1算法要求
给定一个字符串，找到它的第一个不重复的字符，并返回索引。如果不存在，就返回-1.

案例s=“leetcode”
返回0

案例s=“loveleetcode”
返回2

提示：可以假定该字符串只有小写字母。

5.3.2解题思路
1.pythonic算法
怎么确定某个字符在字符串中是不重复的呢？可以用最简单的方法，遍历字符串，看某个字符之前的字符串没有包含这个字符，之后的字符串也没有包含这个字符，就可以确定这个字符在字符串中是唯一的，也就是不重复的字符。以s=“aabcc”为例子。

就是要确定s【i】not in s【：i】 and s【i】not in s【i+1:】。被查找字符既不在字符之前，也不在字符之后。题目要要求是找到一个不重复的字符。到s【2】时已经找到了。中断遍历（循环），返回该字符在字符串中的序列。
这种算法有python特色，其他语言需要一遍遍循环遍历。每个字符都有前后两个字符串。在python中，使用切片来验证是否包含，只需要一次遍历就足够了。

2.哈希算法
在题目的补充设定中规定了字符串只包含小写字母，也就是说字符串中所有的字符总共只有a-z这26个类型，即所有的字符的类型是一个常量，而且这个常量不是很大。可以先统计字符串中每个字符各有多少个。最后遍历字符串。看哪个字符统计后的总数为1.有可能不止一个结果为1，返回第一个被找到的字符即可。那么这个字符为所求。最后返回该字符在字符串中的序列。
在python中可以利用字典的特性。以26个字符为字典的键，遍历字符串，统计字符的个数为键值。
统计所有字符的个数后，再次遍历字符串，看哪个字符在字典中的键值为1.
这样只需要两次遍历字符串，就可以得到唯一字符的位置。

5.3.3解题代码
1.pythonic
查找字符串中第一个唯一字符的常规算法代码如下：

class Solution:
    def firstUniqChar(self, s: str) -> int:
    	if len(s)==1:
    		return 0
    	for i in range(len(s)):
    		if s[i] not in s[i+1:] and s[i] not in s[:i]:
    			return i
    	return -1
利用python切片，可以方便解决很多问题。

2.哈希算法代码
class Solution:
    def firstUniqChar(self, s: str) -> int:
    	#hash算法，26个字母为键的字典
    	words=[chr(i) for i in range(97,123)] #[a-z] 
    	values=[0]*26 #构建重复的list
    	wordsDic=dict(zip(words,values)) #to loop over two or more sequence at the same time, the entries can be paired with the zip() function. {"a"=0,"b"=0 ...}
    	for word in s:
    		wordsDic[word]+=1 	#统计字符串中各个字符的个数
    	for i in range(len(s)):  #再次遍历字符串，通过与字典的对比，找到唯一一个的字符。因为python字典不是有序的，所以在不能直接遍历字典，而是通过遍历字符串来返回第一个返还目标的序列号
    		if wordsDic[s[i]]==1:
    			return i
    	return -1

5.4有效的字母异位词
5.4.1算法要求
给定两个字符串s和t，编写一个函数来判断t是否为s的一个字母异位词

示例1:
输入s=“anagram”，t=“nagaram”
输出：true

输入s=rat t=car
输出 false

说明：假定字符串只包含小写字母
进阶：如果输入字符串包含unicode字符怎么办？你能否调整解法？

5.4.2解题思路
1.常规解法
这一道题的意思是比较两个字符串，如果这两个字符串所包含的字母和字母的个数是一样的返回true。直接比较两个字符串当然不方便，因为字符串不是有序的。幸运的是字符串可以排序。既然如此，那把两个字符串排序后进行比较，就很方便了。输入s=“anagram”，t=“nagaram”。
排序后遍历这两个列表，对比相同序号的元素是否一致。如果不一致，不是有效的字母异位体。

2.进阶算法
如果字符串包含了unicode字符呢？unicode字符虽然也是可以排序的,没必要。可以利用python列表中remove方法的特性。python列表的remove方法可不在乎被删除的元素在什么位置。只要列表中有这个元素，就可以直接删除。
当被删除的列表全部删除，而且没抛出异常，说明是字母异位词。

5.4.3解题代码
1.常规算法代码

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s)!=len(t):
    		return False
    	sList=list(s) #字符串是不变的，无法排序，所以先把字符串转换成列表，再排序
    	sList.sort()
    	tList=list(t)
    	tList.sort()
    	for i in range(len(s)):
    		if sList[i]==tList[i]:
    			continue
    		else:
    			return False
    	return True

2.进阶算法代码
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s)!=len(t):
    		return False
    	sList=list(s)
    	for word in t:
    		try:	#使用try来判断s字符串中是否有相应的字符，如果没有，通过异常处理返回结果。不管是一般字母还是unicode字符，都能处理
    			sList.remove(word)
    		except ValueError as e:
    			return False
    	return True

也可以使用hash算法，字典分别统计两个字符串字母的个数，然后比较两个字典，如果相同时字母异位词。

5.5验证回文字符串
5.5.1算法要求
给定一定字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，我们将空字符串定义为有效的回文串

示例1:
输入："A man, a plan, a canal:panama"
输出：true

5.5.2解题思路
1.常规算法代码如果把字符串中的标点，空格全部去掉，只保留字母和数字，并且剩下的字符串是轴对称的，那么原始字符串就是回文字符串。
因此，常规算法的思路很简单。首先过滤掉不是字母，也不是数字的字符，然后利用python的切片，比较以中轴线为界，字符串后半部分的倒序是否和前半部分相等。或者倒序字符串列表后和原字符串比较，如果相等是回文字符串。以s=“Le,VEL”为例，需要将字符串过滤后再验证。

2.双指针算法：
在解决算法问题时，双指针算法是常用的。如果没有什么头绪，可以优先考虑双指针。在这道题中，把双指针放在头和尾巴。串首指针往后移动，尾指针往前移动。确定指针所指字符是不是字母，是则开始比较，否责跳过该字符，一直找到字母或者退出为止。当两个指针相遇时退出循环。
left,right指针相遇，退出循环，不需要预处理，没有使用额外空间。

5.5.3解题代码
1.常规算法代码
常规算法代码如下：

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	if len(s)<2:
    		return True
    	sList=[]
    	s=s.lower() #所有字符转换成小写字母，避免异常跑出了
    	for word in s: #过滤了需要验证的字符串列表
    		if word.isalnum():
    			sList.append(word)
    	n=len(sList)//2 #确定中轴线为止
    	if sList[:n]==sList[::-1][:n]:
    		return True
    	else:
    		return False

2.双指针算法
class Solution:
    def isPalindrome(self, s: str) -> bool:
    	if len(s)<2:
    		return True
    	s=s.lower()
    	left=0
    	right=len(s)-1
    	while right-left>0:
    		if not s[left].isalnum():
    			left+=1
    			continue
    		if not s[right].isalnum():
    			right-=1
    			continue
    		if s[left]==s[right]:
    			left+=1
    			right-=1
    		else:
    			return False
    	return True

双指针算法是一个通用算法，比常规算法少了一个过滤步骤。

5.6字符串转int
5.6.1算法要求
实现一个字符串转整数函数。首先该函数会根据需要丢弃无用的开头空格字符，直到找到第一个非空字符。当我们寻找到第一个非空字符为正号或者负号时，将该符号与之后尽可能多的连续数组组合起来，作为该int的正负号。加入第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意，该字符串中的第一个非空格字符不是一个有效的整数字符，字符串为空，仅包含空白时，必须要转换
在任何情况下，若函数不能进行有效的转换，则返回0.

提示：假设我们的环境只能存储32位大小的有符号整数，那么其数值范围为[-2^31,2^31-1]，如果超过了这个范围，就返回int_max（2^31-1），或int_min(2^31-1)

输入”42“
输出42

输入” -42“
输出-42

输入"4193 with words"
输出4193

输入“words and 987”
输出0
第一个非空是w，不是数字或正负号，无法转换。

输入：-9128372332
输出：-2147483648
-9128372332超过32bit整数范围，因此返回int_min(-2^31)

5.6.2解题思路
限制条件很多，你会发现，输入的字符串必须符合某种规格才能转换，不符合这个规格的返回0.这个规格就是字符串必须以0开头或者多个空格开头，然后接上0个或者1个+或者-，正负号后面接1个或者多个数字，数字后面有0个或者多个其他字符。如果写成正则大概是:
s='\s'*['+';,';-']?+'\d'{1,}+'.'*
因此需要转换的就是字符串s的第三部分，也就是'\d'{1,}这一部分。最终转换完成后还有一个数值区间测试，转换得到的数字必须在某个数值之间。以s=“-12s3”为例。通过简单几个步骤，就可以得到转换后的数字。

5.6.3解题代码
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if len(s)<1:
        	return 0
        minusFlag=False #假设数字是正整数
        if s[0] in ['+','-']: 
        	if s[0]=='+':   
        		pass
        	else:			#如果负号，改变minusFlag的值
        		minusFlag=True
        	s=s[1:]

        if len(s)<1: #去除正负号后字符串长度
        	return 0
        if not s[0].isdigit(): #符号后非数字
        	return 0

        iList=[]

        for i in range(len(s)):
        	if s[i].isdigit():
        		iList.append(s[i])
        	else:
        		break

        INT_MAX=pow(2,31)-1
        INT_MIN=pow(2,31)*(-1)

        if minusFlag: #测试整数区间
        	num=int("".join(iList))*(-1)
        	if num<INT_MIN:
        		num=pow(2,31)*(-1)
        else:
        	num=int("".join(iList))
        	if num>INT_MAX:
        		num=pow(2,31)-1
        return num


5.7实现strStr()
5.7.1算法要求
给定一个haystack字符串和一个needle字符串，在haystack字符串中出现的第一个位置（从0开始）。如果不存在，就返回-1.

输入 haystack='hello',needle="ll"
输出 2

当needle是空字符串时，我们应该返回什么值呢？
对于本题而言，needle是空字符串时应当返回0.这与c语言的strstr（），以及java的indexOf（）定义相符。

5.7.2解题思路
本题就是查找，与之前的张杰不同的是这道题查找的是字符串，就是在一个字符串中查找子字符串，这里使用最基本的顺序查找法来查找。基本上就是遍历字符串作为subStr的开头，去除与子字符串相同产生长度的subStr，然后和子字符串比较，相同就返回序列值，否则就继续遍历。一般来说在比较字符串和subStr也需要遍历。也就是说时间复杂度是o-n平方。借助python的切片，在比较子字符串和subStr时无需遍历，因此python算法的strStr时间复杂度只有o-n。以字符串haystack=“hello”子字符串为ll为例。
遍历字符串HyStack无序从头到尾遍历，只需要从hystack【0】遍历到hystack【len（haystack）-len（needle）】即可。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
        	return -1
        if needle==haystack:
        	return 0
        length=len(needle)
        pointer=0
      
        while pointer<=(len(haystack)-len(needle)): #pointer指针只需要遍历两个字符串长度的差就够了
        	if haystack[pointer:pointer+length]==needle: #subSTr=haystack[pointer:pointer+length]
        		return pointer
        	else:
        		pointer+=1
        return -1
        
这道题也可以用two pointer来解决。

5.8报数
5.8.1报数要求
报数数列是一个整数数列，按照其中的整数顺序进行报数，得到下一个数。
1 一个一
11 两个一
21 一个二，一个一
1211
111221
给定一个int n，输出报数序列的第n项。
整数序列将表示为一个字符串。

输入1
输出“1”

输入4
输出“1211”

5.8.2解题思路
这一道题从题目的要求上看是没有难度的，简单的读数，是什么数字就是读什么。只要是在前面添加上这个数的总数是多少就行。读n次，用简单的循环就解决了，使用while或者for。例子上n=5，以供统计了5次，为了演示方便，截取第四次的统计1211作为演示。
将被统计列表为rawList=【“1”，“2”，“1”，“1”】，统计列表为countList=【】。首先统计rawList[0]的个数，将结果写入countList中。

将统计结果和被统计元素写入countlist中去，统计结果为pointer+1个，pointer从0开始，统计的元素为1，所以countlist=【1，1】。然后将rowlist中已经统计过的元素抛出。现在rowlist=【2，1，1】，然后继续统计新的rowList【0】，也就是“2”的个数。
第二次统计rowList。rawList【0】元素为2，共有一个。追加到countlist里去。先追加统计个数，再追加元素。countlist=【1，1，1，2】。rawlist排除掉已统计过的元素，新的rawList=【1，1】。进入下一轮统计。
第三轮统计结束，统计的结果是countlist=【1，1，1，2，2，1】。将rawlist重新设置，ralist=countlist，准备下一次统计，这就是一个不断统计的过程。

5.8.3解题代码

class Solution:
    def countAndSay(self, n: int) -> str:
        if n not in range(1,31): #constaints
        	return "the number is error,quit..."
        if n==1:
        	return "1"
        rawStr='1'
        countList=[] #统计个数
        pointer=0

        while n>1:
        	if pointer+1<len(rawStr):
        		if rawStr[pointer]==rawStr[pointer+1]: #相邻两个数字相同时，指针后移一位
        			pointer+=1
        		else: #相邻两个数字不同时
        			countList.append(str(pointer+1)) #个数，因为从下标0开始，所以需要+1
        			countList.append(rawStr[pointer]) #统计rawStr[pointer]这个数字的个数
        			rawStr=rawStr[pointer+1:] #统计完了一个任务，slice后面不同部分字符串，统计下一个不同的数字个数
        			pointer=0 #指针归零，从头开始统计新的字符串
        		continue
        	else: #旧的rawStr统计完毕，设置新的rawStr
        		countList.append(str(pointer+1)) 
        		countList.append(rawStr[pointer])
        		rawStr="".join(countList)
        		countList=[]
        		pointer=0
        	n-=1
        return rawStr
一步一步操作即可。

5.9最长公共前缀
5.9.1算法要求
编写一个函数来查找字符串数组的最长公共前缀。如果不存在公共前缀，就返回空字符串“”。

输入[flower,flow,flight]
输出“fl”

输入：【dog，racecar，car】
输出”“
不窜爱公共前缀
所有输入只包含小写字母a～z。

5.9.2解题思路
求最长公共前缀，只能遍历每个元素，然后每个字母比较下去，所以可以预测这道题必定要使用嵌套循环。也就是说它的时间复杂度至少是o-n平方。另外还要注意，如果输入的列表是空列表或者是只有一个元素的处理方法。以strs=【”flower“，”flow“，”flight“】为例。
以最短元素的长度为界，全部元素前N位字符串放入一个新的列表中去。然后利用python的集合功能确定新列表是否只有一种字符串，如果是就继续下一步，否则返回前一个存入的字符串

5.9.3解题代码

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or "" in strs: #排除特殊情况
        	return ""
        if len(strs)==1:
        	return strs[0]
        publicWordList=[]

        minLength=min([len(st) for st in strs]) #找到最小长度

        for i in range(minLength): #i=0...minLength
        	for word in strs:	
        		publicWordList.append(word[:i+1])
        	if len(set(publicWordList))==1: #determine whether publicWordList has more than one words. i.e. does not share prefix
        		publicWordList=[] #reset publicWordList
        	else:
        		return strs[0][:i] #output the prefix
        return strs[0][:minLength]

6.1链表
算法中最常见的数据结构有链表和tree。相对而言链表简单，从简单的链表开始。
常见链表可以分为单向链表，双向链表，循环链表等。以最简单的单向链表为例，结构上可以分成两部分：数据域，指针域。其中数据域中存放的是链表的值，指针域存放的是一个指针。指向下一个链表，通过指针域，只需要找到头head，就可以遍历整个链表。

6.1删除链表中的节点
6.1.1算法要求
编写一个函数，删除某个链表中给定的节点，你将只被给定要求被删除的节点。
现在有链表head=【4，5，1，9】

输入head【4，5，1，9】
输出：【4，1，9】

·说明：链表至少包含2个节点
·链表所有节点值唯一
·给定节点为非末尾节点并且一定是有效节点
·不要返回任何结果

6.1.2解题思路
链表是数据结构中常用的数据类型。这一道题就是最基本的删除链表节点问题。以链表head=【4，5，1，9】为例，被删除node=5.
从物理上来说，node=5这个节点并没有被删除，只是重新赋值并且重新换了后面的节点，被删除的是node的下级节点。从效果上来看，node=5消失了。

6.1.3解题代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next

这个算法是用下个节点的值代替被删除的节点的value，然后删除下一个节点的方法达到目的的，是一种伪删除（因为删除的不是查到的那个节点）。当然要直接删除被查找到的节点也是可以的（这种删除就是真正的删除查到的节点了）。只是采用这种方法不得不考虑如果被查到的节点就是head的情况 所以用简单的方法吧。

6.2删除链表的倒数第n个节点
6.2.1算法要求
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头节点。

例子：给定一个链表1-2-3-4-5，n=2
删除倒数第二个节点后，链表变成1-2-3-5。

说明：给定的n保证有效
进阶：尝试使用一趟扫描实现

6.2.2解题思路
1.常规算法
按照题目的要求删除倒数第n个节点。那么按照常规的算法应该先统计总共有多少个节点，然后算出倒数第n个节点是正数第几个节点，然后删除这个节点，返回head，原理很简单，eg head=【1，2，3，4，5】，n=2.
常规算法简单，但是需要两次遍历。

2.进阶算法
进阶算法要求只使用一次扫描。定位到倒数第n个节点，使用一个指针，用一次扫描是做不到了，刚才的常规算法是一个指针，两次扫描彩定位了倒数第n个节点。想一次扫描，就只能使用双指针了。
两个指针相隔n个节点，双指针同时移动，相对距离一直不变。当right指针到达链表尾时，left.next就是倒数第n个节点，也就是被删除的节点

6.2.3解题代码
1.常规算法
删除链表倒数第n个节点的常规算法代码为：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer=head
        length=0
        while pointer: #统计链表长度
        	pointer=pointer.next
        	length+=1
        if length==1: #只有一个节点
        	return None

        pointer=head
        if n>=length: #删除第一个节点
        	head.val=head.next.val #删除头部
        	head.next=head.next.next
        else:
        	if n==1: #删除尾巴节点
        		for i in range(length-2):
        			pointer=pointer.next
        		pointer.next=None
        	else: #删除中间节点
        		for i in range(length-n-1):
        			pointer=pointer.next
        		pointer.next=pointer.next.next
        return head

需要考虑多种情况，比如只有一个节点，删除节点是头部，尾巴。

2.进阶算法
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    	if head.next==None: #如果头是空
    		return None

    	left=right=head
    	si=0 #计数器

    	while si<n:
    		si+=1
    		right=right.next #双指针right先走n步

    	if right==None: #如果先走n步的时候，right已经触碰到了底部，证明n>len(列表)
    		head=head.next #删除第一个节点
    		return head
 
    	while right.next!=None: #left和right同时移动直到right.next==none为止
    		left=left.next
    		right=right.next

    	if n==1: #删除最后一个节点
    		left.next=None

    	else: #删除中间的节点
    		left.next=left.next.next
    	return head
虽然使用了两个while，只扫描了一次，经过了一次遍历，时间复杂度是o-n

6.3反转链表
6.3.1反转一个单链表
示例：
输入：1-2-3-4-5-null
输出：5-4-3-2-1-null

进阶：
迭代或递归地反转链表（两种方法）

6.3.2解题思路
1.常规算法
题目并没有要求不利用额外的空间，那么最简单的做法就是给链表重新赋值，也就是反转链表的值。以head=【1，2，3，4，5】为例。

2.进阶算法
如果不想重新为链表赋值，就只有为节点重新指定next了；但是重新指定节点的next，又无法进入下一法节点。如果有两个指针呢？
使用双指针left，right，再配合head，交换两个节点之间的顺序。如图6-11所示。

6.3.3解题代码
1.常规算法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        valList=[]
		pointer=head
		while pointer:
			valList.append(pointer.val)
			pointer=pointer.next

		pointer=head
		while valList:
			pointer.val=valList.pop()
			pointer=pointer.next

		return head

2.进阶算法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	
    	left=right=head #初始化 1>2>3>4>5

    	if head==None: #边界条件none
    		return None

    	if right.next==None: #边界条件：只有一个元素
    		return head

    	else:
    		right=right.next #right先行
    		left.next=None #原来的第一个变成现在的最后一个

    	while right!=None: #开始循环
    		head=right #head变成了right的地方，这里不能写head=head.next，因为head.next只是2，right是2-3-4-5
    		right=right.next #right再往右一步
    		head.next=left #箭头转向
    		left=head #left往右边,这里不能写left=left.next
    	return head

#现在我不理解为什么更新肩头的时候，不能写head=head.next,而要写head=right，否则就会有null ptr error。但是我记住了，以后更新肩头就只有先行的肩头使用right=right.next，其余的都不要用next ptr. 一旦next ptr多了就会给你null ptr error.

6.4合并两个有序链表
6.4.1算法要求
将两个有序链表合并为一个新的有序链表并且返回。新链表是通过拼接给定的两个列表的所有节点组成的。

示例：
输入：1-2-4，1-3-4
输出 1-1-2-3-4-4

6.4.2解题思路
合并两个有序链表，在逻辑上简单。比较11.val和12.val，谁比较小谁就是head.next,然后比较小的节点指向next，一直到两个链表结束。head应该指向哪个链表呢？先比较11.val和12.val？复杂。这里可以将head指向一个fakenode。head的next指向11和12比较小的节点。执行完毕后返回fakenode。next既可以了。以l1=[1,2,4],l2=[1,3,4]为例子。
比较l1.val和l2.val，l1.val比较小，将head。next指向比较小的那个节点l1.head往后移动一位。head。next=l1。l1的指针后移一位。l1=l1.next。如图6-17.比较l1。val和l2.val，明显l2.val比较小，将head。next指向l2，head。next=l2.l2的指针往后移动。继续下一轮比较
当两个链表都比较完毕时，fake链表整合了两条有序列表，返回fake。next即可。head=fake。next

6.4.3解题代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None: #两个链表都是空
        	return None
        fakeNode=ListNode(0)
        head=fakeNode

        while list1!=None or list2!=None: #两条链表遍历完毕
        	if list1==None: #l1遍历完毕
        		head.next=list2
        		list2=list2.next
        		head=head.next
        	elif list2==None: #l2遍历完毕
        		head.next=list1
        		list1=list1.next
        		head=head.next
        	else: #都没遍历完毕
        		if list1.val<=list2.val:
        			head.next=list1
        			list1=list1.next
        			head=head.next
        		else:
        			head.next=list2
        			list2=list2.next
        			head=head.next
        return fakeNode.next

这一道题并没有要求in-place也就是原地整合。实际上有更简单的方法，遍历两条链表，只获取链表的值，加入链表后排序；然后通过链表，重新创建一条新链表。

6.5回文链表
6.5.1算法要求
判断一个链表是否为回文链表
eg1:
输入：1-2
输出：false

eg2:
输入1-2-2-1
输出：true

进阶：
用o-n时间复杂度和o-1空间复杂度解决这个问题。

6.5.2解题思路
如果把回文链表当成图形来看，那么它是一个轴对称图形，和回文字符串类似。因此把回文链表的值放到一个链表中去，这个链表的*倒序*链表必定是和原链表相同的。以head=【1，2，2，1】为例。

6.5.3解题代码
反转链表的代码为：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None:
        	return True
        valList=[]

        while head:
        	valList.append(head.val)
        	head=head.next

        rList=valList[::-1]
        if rList==valList:
        	return True
        else: 
        	return False

6.6环形列表
6.6.1算法要求
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置。如果pos是-1，证明没有环

输入head=【3，2，0，-4】，pos=1
输出：true
解释 链表中有一个环，尾巴连接到第二个节点。

输入head=【1，2】，pos=0
输出：true
解释 链表中有一个环，尾巴连接到第一个节点。

head=【1】。pos=-1
输出：false
链表中没有环

进阶：使用o（1）内存解决此问题

6.6.2解题思路
如果一个链表中有环，使用链表指针指向下一节点（head=head。next）的方式就陷入了死循环。这个链是无穷尽的。可以试试双指针，与前面的题不同的是，这次不是使用left，right指针，而是使用slow，fast指针。以head=【3，2，0，-4】，pos=“-12s3”为例。通过简单几个步骤，就可以得到转换后的数字。
使用快慢指针，快指针每次向前移动2步，慢指针每次向前移动1步。如果两个指针最后都指向None，说明这个链表不是环形。如果快慢指针指向同一个节点，说明是环形的。因为只有在一个环内，fast才能追上slow，否则将继续向前移动。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    	if head==None:
    		return False
    	fast=head
    	slow=head

    	while fast:
    		try:
    			fast=fast.next.next
    			slow=slow.next
    		except: 		#在非环形链表中fast会先达到链表尾巴，slow继续下一步时，fast指针只能抛出异常
    			return False
    		if fast==None or slow==None:
    			return False
    		if fast==slow: #比较指针指向的节点，而不是节点的值。因为链表中可能有相同值
    			return True

第七章 tree
前面一章说的是数据结构中比较简单的链表，这一张即将了解tree。tree分为很多种，通常数据结构说的是二叉树，二叉树像链表的变种，只是链表只有一个指针域，二叉树有两个而已。
7.1二叉树的最大深度
7.1.1算法要求
给定一个二叉树，找出其最大深度
二叉树的深度为根节点到最远也子节点最长路径上的节点树
说明：也子节点是指没有子节点的节点。

eg：给定二叉树【3，9，20，null，null，15，7】
返回它的最大深度3

7.1.2解题思路
一般来说，做有关二叉树的题都是使用递归的。因为递归很容易理解。也不需要二叉树的父子孙节点的关系。因此这里只需要理清root节点的关系。至于其他的节点，使用递归。以二叉树root=【3，9，20，None，None，15，7】为例。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
        	return 0
        else:
        	return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))

制定好规则，然后任其自我递归调用。

7.2验证二叉搜索树
7.2.1算法要求
给定一棵二叉树，判断其是否是一棵有效的二叉搜树
假设一棵二叉搜索树具有如下特征：
·左边小于当前
·右边大于当前
·左子树和右子树都是二叉搜索树

eg1:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

7.2.2解题思路
这一题还是用递归。需要解决，按照题目的定义，rott的值必须大于左边所有节点的值，小于右边所有节点的值。那么可以预测，左边节点的值，深度越深就越小，左边最深节点的left是最小的；右边最深节点的right的值是最大的。那么这个最大值和最小值是多少呢？
在python3定义了最大值，max=sys.maxsize。一天你次这里也可以推算出min=sys.maxsize*（-1）。max和min有了，就可以得出一条结论。在root节点中，所有左边节点的值大于min，右边节点的值小于max。否则root节点必定不是二叉搜索树。以root=【5，1，4，None，None，3，6】为例。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import sys
        min=sys.maxsize*(-1)
        max=sys.maxsize
        return self.validBST(root,min,max) 

    def validBST(self,root,min,max):
    	if root==None:
    		return True
    	if root.val<=min or root.val>=max:
    		return False
    	return self.validBST(root.left,min,root.val) and self.validBST(root.right,root.val,max) #左边小于当前,右边大于当前

这一道题重新定义了一个validBST函数用于递归，避免了干扰。

7.3对称二叉树
7.3.1算法要求
给定一棵二叉树，检查它是否是镜像对称的。
例如，二叉树【1，2，2，3，4，4，3】是对称的。

但是下面这个【1，2，2，null，3，null，3】不是镜像对称的。

7.3.2解题思路
这一道题的考点是对称二叉树，而例子可以看出是轴对称的。假设root。left为L节点，root的right为R节点。所谓的对称就是要求L。right=R。left，and L。left=R。right。好了，对称二叉树的条件已经确定了，只需要设定好规则直接递归就可以了。以root=【1，2，2，3，4，4，3】为例。

7.3.3解题代码
对称二叉树的代码如下：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    	if not root:
    		return True
    	else:
    		return self.symmetricTree(root.left,root.right) #调用辅助函数

    def symmetricTree(self,lNode,rNode): 
    #重新定义被递归的函数。理由是确定一棵树是否对称需要输入两个参数，需要左右两个子节点，原本函数只限定了一个函数
    	if not lNode and not rNode:
    		return True
    	elif lNode and rNode and lNode.val==rNode.val: #判断是否相等
    		return self.symmetricTree(lNode.right,rNode.left) and self.symmetricTree(lNode.left,rNode.right) #再递归左右子
    	else:
    		return False

7.4二叉树的层次遍历
7.4.1算法要求
给定一棵二叉树，返回其按层次遍历的节点值（逐层地，从左到右访问所有节点）。

例如：
给定二叉树【3，9，20，null，null，15，7】
返回层次遍历结果：【【3】，【9，20】，【15，7】】

7.4.2解题思路
这一道题和其他题目有点不一样。其他的题是以节点为单位操作的，而这一道题是以层为单位操作的，树的层数越多，节点就越多，而且对节点值还有顺序的要求。因此，这一道题对节点的递归效果可能没有那么好。换个思路，对层进行迭代。给定二叉树【3，9，20，null，null，15，7】，如图7-10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rList=[]
        subList=[]
        if not root:
        	return rList
        else:
        	cNodeList=[root] #current layer node
        nNodeList=[]

        while True:
        	if cNodeList: #add next layer node to nNodeList
        		node=cNodeList.pop(0)
        		subList.append(node.val)

        		if node.left and node.right:
        			nNodeList.append(node.left)
        			nNodeList.append(node.right)
        		elif node.left:
        			nNodeList.append(node.left)
        		elif node.right:
        			nNodeList.append(node.right)
        		else:
        			pass
        	else:
        		rList.append(subList[:])
        		subList=[]

        		if not nNodeList:
        			break
        		else:
        			cNodeList=nNodeList[:]
        			nNodeList=[]
        return rList

通过对层节点的迭代，遍历整个树的所有节点，一直到next layer的节点是空为止。整个过程可以归纳为：统计下一层所有节点，遍历本层节点，进入下一次，统计下一次所有节点，遍历本层节点。

7.5将有序数组转换成二叉搜索树
7.5.1算法要求
将一个按照升序排列的有序数组转换为一棵高度平衡二叉搜索树。
本题中，一棵二叉搜索树中每个节点的左右两个子树高度差绝对值不超过1.

示例：
给定数组：【-10，3，0，5，9】
可能的答案：【0，-3，9，-10，null，5】

7.5.2解题思路
在平衡二叉树中，root节点的值必定是一个最平衡的值，即不是列表最大的，也不是列表最小的。如果是一个有序列表，那必定是有序列表最中间的那个。如果列表个数为偶数也没关系，只是平衡二叉树左边节点多一个或者右边节点多一个。只要满足这一个条件就够了。剩下的递归即可。以有序数组nums=【-10，3，0，5，9】为例，如图7-13.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
        	return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root

8.排序和搜索设计问题
本章包含了leetcode中的两节：排序和搜索，设计问题。因为这两节的题型比较相近，题目比较少，合并。
8.1合并两个有序数组

8.1合并两个有序数组
给定两个整数数组nums1和nums2，将nums2合并到nums1，使得nums1成为一个有序数组。

说明：初始化nums1和nums2的元素数量为m和n
·假设nums1有足够的空间（大于m+n），来保存nums2中的元素

输入 nums1=【1，2，3，0，0，0】，m=3
nums2=【2，5，6】 n=3
输出：【1，2，2，3，5，6】

8.1.2
解题思路：
1.pythonic算法
这一道题简单地说就是一道排序题，将两个列表合并成一个列表后排序，给一个整数列表排序，以nums1=【1，2，3，0，0，0】，m=3
nums2=【2，5，6】 n=3为例。

所要做的仅仅是合并nums1和nums2，然后使用python的列表sort函数而已。

2.详细算法
pythonic取巧，虽然达到了目的，但是并不清楚是怎么做到的。现在来看详细的算法过程，没错还是排序。将两个列表合并，和插入排序很像。

与正规的插入排序相比，有序数组的插入不是从第二个数开始插入的，可以直接从第二个有序数组的组头开始插入，因为数组是有序的。

8.1.3解题代码

1.pythonic
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
        	nums1[m+i]=nums2[i]
        nums1.sort()
        return

2.详细代码
合并有序数组的详细代码：
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n]=nums2[:n]

        for right in range(m,m+n):
        	target=nums1[right]
        	for left in range(0, right):
        		if target<=nums1[left]:
        			nums1[left+1:right+1]=nums1[left:right] #使用python切片赋值
        			nums1[left]=target
        			break
        return

这道题和链表章节的合并有序链表很相似，也可以参考合并有序链表的算法来做。解法很多，可以参考合并有序链表的解法做。

8.2第一个错误版本
8.2.1算法要求
假设你的产品经理，目前正在带领团队开发新产品，不幸的是产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的。因此错误的版本之后的所有版本都是错误的。
假设n个版本【1，2，。。。n】，你要找出导致之后所有版本出错的第一个错误的版本。可以通过调用 bool isBadversion（version）接口来判断版本号version是否在单元测试中出错。实现一个函数来查找第一个错误的版本嗯。你应该减少对调用api的次数。

eg1
给定n=5，version=4是第一个错误的版本
调用isBadversion（3）=False
isBadversion（4）=True
isBadversion（5）=True
4是第一个错误的版本

8.2.2解题思路
这道题在某个范围内返回一个数。如果猜的数比这个数大就返回True，猜的数比这个数小就返回False。
在一个有序数列中，如果快速找到一个符合条件的数？有比二分查找更方便的方法吗？以n=5为例。

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分法
        left=1
        right=n 
        while left<=n: #注意循环缩进
        	mid=(left+right)//2

        	if isBadVersion(mid): #如果mid是坏的
        		if isBadVersion(mid-1): #如果前面的也是坏的
        			right=mid 			#二分法
        		else:					#如果前面的是好的
        			return mid   #查找结束，mid为所求
        	else:       #如果mid是好的
        		if isBadVersion(mid+1): #如果mid后面一个是坏的
        			return mid+1 #为所求
        		else:  #继续二分法
        			left=mid

8.3数组洗牌
8.3.1算法要求
打乱一个没有重复元素的数组
e.g:
//以数字集合1，2，3初始化数组
int[] nums={1,2,3}
Solution solution=new Solution(nums);

//打乱数组【1，2，3】并返回结果。任何【1，2，3】的排列返回的概率应该相同。
solution.shuffle();

//重设数组到初始状态【1，2，3】
solution.reset();

//随即返回数组【1，2，3】打乱后的结果。
solution.shuffle();

8.3.2解题思路
题目reset函数只要将nums返回就行了。至于shuffle函数，意思就是将nums列表中的元素交换位置，类似于洗牌。以nums=【1，2，3】为例。

class Solution:

    def __init__(self, nums: List[int]):
    	self.nums=nums
        
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
    	import random
    	sList=self.nums[:] #深复制，不影响原来的数组。 不能使用浅复制sList=self.nums，修改后会影响原数组
    	rList=[]

    	while sList:
    		val=random.choice(sList)
    		rList.append(val)
    		sList.remove(val)
    	return rList
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

8.4最小栈
8.4.1算法要求：
设计一个支持push，pop，top操作并能在常数时间内检索到最小元素的栈。
·push（x）：将元素x推入栈
·pop（）：删除栈顶的元素。
·top（）：获取栈顶元素。
·getMin（）：检索栈的最小元素。

示例：
MinStack minStack=new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3)
minStack.getMin(); #return -3
minStack.pop();
minStack.top(); #return 0
minStack.getMin(); #return -2

8.4.2解题思路
在python中，栈只是对列表进行类栈式操作。对栈的push，pop，getMin操作实际上就是对列表的append，pop，min操作。

8.4.3解题代码

class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        try:
        	self.stack.pop()
        except Exception as e: #对空列表的pop，top，getMin操作，需要抛出异常
        	pass

    def top(self) -> int:
        try:
        	x=self.stack[-1]
        except Exception as e: 
        	return None 
        else:
        	return x

    def getMin(self) -> int:
    	try:
    		mi=min(self.stack)
    	except Exception as e:
    		return None
    	else:
    		return mi
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
对空列表的pop，top，getMin操作，需要抛出异常

ch9 动态规划
这一张可能是本章最难理解的章节。动态规划意味着所有的题都是牵一发动全身，解题的答案会随着解题的过程而动。简单的逻辑判断是无法解决问题的。要解决这类题目，需要在所有的动态调节中找到“不动”的条件，然后通过这个“不动”的条件来解答问题。

9.1爬楼梯
假设你正在爬楼梯，需要n阶才能到达楼顶。每次你可以爬1或2个台阶。你有多少个不同的方法可以爬到楼顶。
n是一个正整数

eg1:
输入：2
输出：2
解释两种方法：1+1，2

eg2:输入：3
输出3
解释：1+1+1，1+2，2+1

9.1.2解题思路
假设n个台阶，f（n）返回方法总数。不管怎么爬，第一步只有两种爬法：一种是1个，一种是2个台阶，不管n有多大，如果第一步爬一个台阶，总共有f（n-1）种爬法，如果第一步爬2个台阶，总共有f（n-2）种爬法，那么总共的方法是f（n）=f（n-1）+f（n-2）。这就是动态条件中不动的那部分。
这个推断可以用归纳法试试看。
如果有1个台阶：
f1=1
2个台阶
f2=2
三个台阶1+1+1，1+2，2+1
f（3）=3
四个台阶：
f（4）=5
验证了猜测

9.1.3解题代码
以台阶数为序列号，将对应的方法总数代入一个列表中


def climbStairs(self, n: int) -> int:
    stepList=[1,1,2]
    i=n
    while i>2:
    	stepList.append(stepList[-1]+stepList[-2])
        i-=1
    return stepList[n]
    
if __name__ == '__main__':
	n=5
	print("count need %d step" %climbStairs(n))

先用递归法来解题。将代码修改一下。代入leetcode页面

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
        	return 1
        elif n==2:
        	return 2
        else:
        	return self.climbStairs(n-1)+self.climbStairs(n-2)

可以看出leetcode超时只能修改代码了。观察到规律是fib数列。只需要稍微修改一下就可以了。

class Solution:
    def climbStairs(self, n: int) -> int:
        stepList=[1,1,2]
        i=n
        while i>2:
        	stepList.append(stepList[-1]+stepList[-2])
        	i-=1
        return stepList[n]

这个算法得到的是一个映射的数列，返回数列最后一个元素。

9.2 买卖股票的最佳时机
9.2.1算法要求
给定一个数组，它的第i个元素是一支给定股票第i天的价格。如果你只允许完成一笔交易，设计一个算法计算获得最大利润。

9.2.2解题思路
这道题如果按照常规想法，可能会想到在数列后面找最大的数，然后再最大数之前找最小树，返回差，是错的。price=【9，10，0，9】返回的是1，而不是9.

这道题只交易一次。可以暴力破解。每天交易n次，然后比较一下，得到最大利润那次就够了。以price=【7，1，5，3，6，4】为例。
得出max最大的那个是5.

9.2.3

class Solution(object):
    def maxProfit(self, prices):
    	if len(prices)<2:
    		return 0
    	maxList=[]

    	for j in range(len(prices)-1):
    		for i in range(j+1,len(prices)):
    			maxList.append(prices[i]-prices[j])
    	profit=max(maxList)
    	if profit<0:
    		return 0
    	else:
    		return profit

在较短的列表中双循环没问题，列表长无法通过了，需要重新修改代码。

class Solution(object):
    def maxProfit(self, prices):
    	if len(prices)<1:
    		return 0
    	min_price=prices[0]
    	max_price=0

    	for price in prices:
    		min_price=min(min_price,price)
    		profit=price-min_price
    		max_profit=max(max_profit,profit)
    	return max_profit


9.3最大子序和
9.3.1算法要求
给定一个整数数组，找到一个具有最大和的连续子子数组，返回最大和。
输入【-2，1，-3，4，-1，2，1，-5，4】
输出：6
解释连续数组【4，-1，2，1】的和最大，为6

进阶：
如果实现了o-n，尝试用分而治之

9.3.2
这道题动态规划很简单。就是假设列表中第一个数为最大子胥河，然后逐个将列表后的元素叠加到最大子序和中。如果最大子序和变大了，就修改最大子序和的value，继续往下叠加。如果变小了就放弃最后叠加的数字（必定是负数）。从最后叠加的那个数（负数）之后，重新开始叠加计算最大子序和。最后得到的就是整个列表的最大子序和。以nums=【-2，1，-3，4，-1，2，1，-5，4】为例。

用较大的subsum替代掉maxsun，一直叠加到列表完毕，最后得到的maxsum就是最大子序和。

9.3.3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subCount=0
        maxCount=nums[0] #先假设最大子序和就是列表第一个元素

        for i in range(len(nums)): #for i=[0,...,len(nums)]
        	subCount+=nums[i]
        	if subCount>maxCount:
        		maxCount=subCount  #计算子序和，如果将子序和比假设的最大子序和大，就替代假设的最大子序和
        	if subCount<0: #如果subcount比0小，就放弃这次统计
        		subCount=0
        return maxCount

9.4寻找宝物
9.4.1算法要求
假设你是游戏中的一个专业寻宝人，计划在沿街的房屋中寻宝。每个房屋都藏有一定的宝物，影响你的寻宝的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两个相邻房子在同一晚上被寻宝者找到，寻宝者报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动报警装置能够找到的最高钱。

eg1:
输入：【1，2，3，1】
输出：5-4-3-2-1-null
解释：寻找1号房屋（金额=1），寻找3号（金额=3）最高1+3=4

例子2:
【2，7，9，3，1】
12
解释：寻找1号12，3号9，5号1，最高2+9+1=12

9.4.2解题思路
上题算的是列表中的最大子序和，这题算的是列表最大间隔元素和。假设列表nums只有一个元素，那么最大间隔和就是maxsum=nums【0】。如果nums有2个元素。那么最大间隔元素和就是maxsum=max（nums）。如果3个元素，最大间隔元素和就是max（nums【0】+nums【2】，nums【1】。有点递归的意思。但是在爬楼梯算过了，递归无法通过测试。可以借鉴爬楼梯的解法，重新创建一个数列，只不过不是fib数列。以nums=【2，7，9，3，1】为例。

nums=【2，7，9，3，1】

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
        	return 0

        size=len(nums)
        if size==1:
        	return nums[0]

        dp=[0]*size
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,size):
        	dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[size-1]

CH10
可以使用算法问题来解决数学问题

10.1 fizzbuzz
10.1.1 算法要求
写一个程序，输出从1到n数字的字符串表示
·如果n是3的倍数，输出fizz
·如果n是5的倍数，输出buzz
·如果n是3和5的倍数，输出fizzbuzz

10.1.2解题思路
这道题是基础题。

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rList=[]

        for i in range(1,n+1):
        	if i%3==0 and i%5==0:
        		rList.append("FizzBuzz")
        	elif i%3==0:
        		rList.append("Fizz")
        	elif i%5==0:
        		rList.append("Buzz")
        	else:
        		rList.append(str(i))
        return rList

10.2计算质数
质数又被称为素数，指在一个大于1的自然数中，除了1和本身外，没法被其他自然数整除的数。

10.2.1算法要求
统计所有小于非负数n的质数的数量

eg：输入10
输出4
解释：小于10的质数一共有4个，分别是2，3，5，6

10.2.2解题思路
1.常规算法
根据素数的定义计算，这个算法很简单，把所有数字从1到本身除一遍如果可以被其他自然数整除，就不是质数，排除掉，否则加入质数数列。

import timeit

def countPrimes(n):
	primeList=[]
	for i in range(2,n+1):
		flag=True
		for divNum in range(2,i): #从2到i-1，一个一个除，有余数0，可以确定不是质数，退出循环
			if i%divNum==0:
				flag=False
				break
		if flag:
			primeList.append(i)
	#print(primesList)
	return len(primeList)

if __name__=="__main__":
    print(timeit.timeit("countPrimes(10000)","from __main__ import countPrimes",number=10))
    print(countPrimes(10000))

所需要的时间无法通过检测

2.倍数筛选
根据质数定义，非质数可以分解为两个非1数的乘积。也就是说x=a*b，其中a，b都不能等于0或1。那么a的倍数和b的倍数都不可能是质。

因此，获取质数的方法就很简单了。先把2到n所有数字列出来。然后筛选所有等于n/2的数字的倍数。因为n/2的倍数已经大于n了。

3.Eratosthenes选法

class Solution:
    def countPrimes(self, n: int) -> int:
    	if n<2:
    		return 0
    	prime=[True for _ in range(n)]
    	prime[0]=prime[1]=False

    	for x in range(2,n):
    		if prime[x]==True:
    			for y in range(x*x,n,x): #用2*x开始筛选也可以通过
    				prime[y]=False
    	#print(prime)
    	return prime.count(True)

10.3 3的幂
10.3.1算法要求
给定一个整数，写一个函数来判断是否为3的幂次
eg1
输入：27
输出：true
eg2:
输入0
输出：false
进阶：你能不能不用循环or递归

10.3.2
揭这道题最简单的方法是循环。设定一个循环，获取3的幂，当这个数小于N时，继续获取下一个3的幂。直到大于等于n。如果等于n说明是3的幂，返回true，如果不等于n则返回false。

10.3.3
3的幂解题代码：

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	power3=lambda i:power(3,i)
    	i=0
    	while power3(i)<=n:
    		if power3(i)==n:
    			return True
    		else:
    			i+=1
    	return False

进阶算法要求不使用循环，递归，可以根据对数关系来求解。python中，用import math使用对数一步就可以得到是不是。因为python中math模块计算对数可能有误差，所以可求3的幂可以计算两个数字差绝对值是否小于某个阈值来判断是否相等。

10.4罗马数字转int
10.4.1算法要求
罗马数字包括7个字符
例如2写作II，12写作XII，27写作XXVII，通常情况下小的数字在右边，也有特例，例如4写作IV，1在5左边。同样9表示IX。
给定一个罗马数字，转换成int，输入确保在1～3999范围内。

例子1:
III
3

10.4.2解题思路
罗马数字和int一一对应的，因此第一反应使用python字典。但是题目补充说明中又说了又六种情况是特例。在编程中，一两个特例可以单独列出来，六种太多了。但是六种特例可以通过dict存在。只需要优先配对特例字典，不存在的key再配对罗马字符字典。以s=“MCMXCIV”为例。

class Solution:
    def romanToInt(self, s: str) -> int:
    	romanDic={
    	"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000	
    	}
    	doubleDic={
    		'IV':4,'IX':9,"XL":40,"XC":90,"CD":400,"CM":900
    	}

    	sum=0 #count number
    	i=0 #pointer
    	while i<len(s):
    		try:
    			s[i:i+2]
    		except IndexError as e:
    			sum+=romanDic[s[i]]
    			i+=1
    		else:
    			if s[i:i+2] in doubleDic.keys():
    				sum+=doubleDic[s[i:i+2]]
    				i+=2
    			else:
    				sum+=romanDic[s[i]]
    				i+=1
    	return sum
在检索字典的键时，优先配对两个字符组成的键，也就是6个特例，然后配对单个字符的键。

CH11 其他
不太好分类的放在这里，是比较基本的应用。这类题目对算法的要求不是很高，因为题目简单。

11.1 位1的个数
编写一个函数，输入一个无符号整数，返回二进制表达式中数字位数为1的个数。

例子1
输入0000000000001011
输出3

输入00000100000
输出1

11.1.2
这道题没有难点，唯一要注意的是python3会自动把二进制的数转换成十进制。所以函数参数中虽然输入的是二进制的整数，但是进入函数后还是需要把二进制的参数二进制化。以n=0b00000001011为例（在python3中以0b开头的数字是二进制数）

11.1.3
class Solution:
    def hammingWeight(self, n: int) -> int:
        bList=list(bin(n)) #转换成二进制
        sum=0
        while bList:
        	c=bList.pop()

        	if c=="1":
        		sum+=1
        return sum

方法2:位运算优化
观察这个运算n&n-1。运算结果把n的二进制最低位的1变成0之后的结果。

这样可以利用这个结果加快检查过程，在实际代码中，不断让当前的n和n-1座运算，直到n变成0.因为每次运算会让n的最低位1倍反转，因此运算次数，等于n的二进制中1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
    	sum=0

    	while n:
    		n=n&(n-1)
    		sum+=1
    	return sum

时间复杂度：o-logn，循环次数等于n的二进制位中1的个数，最坏情况下n的二进制位全部是1，需要循环log-n此。
空间复杂度：o-1

11.2汉明距离
11.2.1算法要求
两个整数之间的汉明距离指的是两个数字对应二进制位不同的位置的树木。给出两个整数x，y。计算汉明距离。
例如： 1=0001，4=0100
输出：2

11.2.2解题思路
这道题要求统计二进制不同的数值多少位。将两个数字转换成标准的二进制数字后，遍历就可以了。以x=1，y=4为例。

11.2.3解题代码

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    	xList=list(bin(x))[2::]
    	yList=list(bin(y))[2::]

    	if len(xList)<31:
    		xList=["0"]*(31-len(xList))
    	if len(yList)<31:
        	yList=["0"]*(31-len(yList))

    	n=0
    	for i in range(31):
    		if xList[i]!=yList[i]:
    			n+=1
    	return n




11.3颠倒二进制位
11.3.1算法要求
颠倒给定的32位无符号整数的二进制位
eg1:011
110=6

提示：在某些语言例如java中，没有无符号整数类型，在这种情况下输入和输出被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号还是没符号，内部二进制表现形式一样。
在java中编译器使用二进制补充记法来表示有符号整数。因此在上面的eg2中，输入有符号整数-3，输出有符号整数-1073741825

进阶：如果多次调用这个函数，将如何优化你的算法？

11.3.2解题思路
这一题在二进制数上下功夫，把整数变成二进制后颠倒顺序，再整数，需要注意的是，颠倒前去掉二进制标识位0b。

class Solution:
    def reverseBits(self, n: int) -> int:
        dec2bin=bin(n)
        newBin=dec2bin[::-1][:-2]

        if len(newBin)<32:
        	newBin+="0"*(32-len(newBin))
        newDec=int(newBin,base=2) #转换回整数
        return newDec

方法2:位运算分治（follow-up）
思路：
若要翻转一个二进制串，可以均分为两部分，对每个部分递归反转，然后把左半部分拼接在右半部分后面，完成翻转。由于左右两部分的计算方式是相似的，利用位掩码和位移运算，可以从下往上完成分治。

对于递归最底层，交换所有奇数偶数位：
1.取出所有奇数偶数位
2.把奇数位放在偶数位，偶数移到奇数

类似地，对于倒数第二层，每两位分一组，按组号取出所有，位移。


11.5有效的括号
11.5.1算法要求
给定一个只包括（），{},[]的字符串，判断是否有效
有效必须满足：
·左边括号用相同类型右括号闭合
·左括号必须以正确的顺序闭合

例子1:
输入“（）”
输出 True
输入（】
输出false

11.5.2解题思路
判断哭好的有效性可以用stack。
我们遍历给定的s，当遇到左括号，期望遇到找到右括号。由于右括号需要闭合，因此我们可以把左括号放在栈顶。
当遇到右括号时，需要左括号闭合，此时可以取出栈顶作弊啊括号，并且判断是否为相同类型的括号。如果不是相同类型，或者栈中没有左括号，那么s无效，返回fase。为了快速判断括号类型，我们用hash表存储括号类型。

11.5.3
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1: return False
        dic={
        	"(":")",
        	"[":"]",
        	"}":"{"
        }

        stack=list()

        for i in s:
        	if i in dic: # 1. if it's the left bracket then we append it to the stack
        		stack.append(i)
        	elif len(stack)==0 or d[stack.pop()]!=i: 
        	# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
        		return False
        return len(stack==0) # 3. finally check if the stack still contains unmatched left bracket


11.6缺失数字
11.6.1算法要求
给定一个包含n个数的序列，找出0。。。n中没出现在序列中的那个数

eg1:【3，0，1】
输出2

11.6.2
这道题有陷阱，如何创建那个被比较的列表？第一反应就是range（max（nums））。但是没考虑到nums【0】，也可以先排除这种情况。然后用集合求差集就能得到答案。使用集合一次计算得到答案，缺点是没有遍历快。在这种只有一个差值的情况，还是用集合比较方便。以nums=3，0，1.

11.6.3解题代码

class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        
        	return (set(range(len(nums)+1))-set(nums)).pop()