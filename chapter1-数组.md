# chapter1-数组

## 一、基本概念

- **元素（element）** − 存储在数组中的每个项目称为一个元素。

- **索引（index）** − 数组中元素的每个位置都有一个数字索引，用于标识该元素。

  ![image-20251012002654536](https://cdn.jsdelivr.net/gh/losika-888/images@main/image-20251012002654536.png)

- **Attention**：
- 索引从0开始
- size=the number of elements
- 每个element都可以使用索引
- 数组来源的库是array

## 二、数组的操作

![image-20251012002737706](https://cdn.jsdelivr.net/gh/losika-888/images@main/image-20251012002737706.png)

- 数组的来源：

```python
from array import *
arrayName = array(typecode, [Initializers])
#typecode:数组存储数据的类型
#initializers:初始化的样本
```

- 有关typecode的类型代码说明：

  ![](https://cdn.jsdelivr.net/gh/ losika-888/images@master/image-20251012000420696.png)

- 遍历：将所有的数组元素打印出来
- 插入：在给定index处添加一个元素
- 删除：删除对应index处的元素
- 搜索：使用index搜索
- 更新：更新对应index处的元素

```python
#数组的创建和遍历
from array import *

arrayA=([10,20,30,40,50,60])

for i in arrayA:
    print(i)
```

```python
遍历数组元素： 10
遍历数组元素： 20
遍历数组元素： 30
遍历数组元素： 40
遍历数组元素： 50
遍历数组元素： 60
```

```python
#访问
for i in range(6):
  print(arrayA[i])
```

```python
10
20
30
40
50
60
```

```python
#插入：
arrayA.insert(0,5)
arrayA.insert(1,15)
print(arrayA)
#通过以上例子明白insert()方法的插入是前插
```

```python
[5, 15, 10, 20, 30, 40, 50, 60]
```

```python
#删除
arrayA.remove(15)
print(arrayA)
```

```python
[5, 10, 20, 30, 40, 50, 60]
```

```python
#更新：
arrayA[0]=7.5
print(arrayA)
```

```python
[7.5, 10, 20, 30, 40, 50, 
```
