# chapter2-列表

## 一、列表的创建

- 关于列表的重要一点是列表中的项目**不必是同一类型**

- 创建列表就像将不同的**逗号分隔**值放在方括号之间一样简单

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
```

- 和字符串一样，列表的索引从0开始，可以进行切片、拼接的操作**（数组无法进行切片和拼接）**

```python
print("list1[0]:",list1[0])
print("list2[0]:",list2[0])
```

```python
gengxinliebiaoxxxxxxxxxx list1[0]: physicslist2[0]: 1
```

- 更新列表使用索引

  ```python
  #更新列表
  print("Value available at list1[2] : ",list1[2])
  list1[2]=2002
  print("New value available at list1[2] :",list1[2])
  ```

```python
Value available at list1[2] :  1997
New value available at list1[2] : 2002
```

- 在列表中添加元素

```python
#添加元素
list1.append(2008)
print(list1)
```

```python
['physics', 'chemistry', 1997, 2000, 2008]
```

- 在列表中删除元素

```python
#删除元素（remove方法）
# list1.remove(2008)
# print("删除元素2008之后的序列：",list1)
#删除元素（del方法）
del list1[4]
print("删除元素2008之后的序列：",list1)
```

- 列表的其他操作

  ![image-20251018141830842](https://cdn.jsdelivr.net/gh/losika-888/images@main/image-20251018141830842.png)