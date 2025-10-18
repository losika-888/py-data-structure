from array import *

arrayA=([10,20,30,40,50,60])

#遍历
for i in arrayA:
    print("遍历数组元素：",i)

#访问
for i in range(6):
  print(arrayA[i])

#插入：
arrayA.insert(0,5)
arrayA.insert(1,15)
print(arrayA)
#通过以上例子明白insert()方法的插入是前插

#删除
arrayA.remove(15)
print(arrayA)

#更新：
arrayA[0]=7.5
print(arrayA)

