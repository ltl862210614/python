#! python3
#encoding:utf-8

# 1)访问列表元素
bicycles = ['trek','cannodale','redline','specialized']

print("bicycles:\n%s"%bicycles)

'''
print("print the last element: %s"%bicycles[-1].title())	#访问最后一个元素
print('\n')

print("modify the first")
bicycles[0] = 'suzuki'
print("%s\n"%bicycles)

print("append at the end of the list")
bicycles.append('ducati')
print("%s\n"%bicycles)

print("insert at the index 1")
bicycles.insert(1,'honda')
print("%s\n"%bicycles)

print("delete the second last element")
del bicycles[-2]
print("%s\n"%bicycles)

print("pop index -2:%s",bicycles.pop(-2))	#pop不接参数默认删除最后一个
print("%s\n"%bicycles)

print("remove the 'honda'")
bicycles.remove('honda')
print("%s\n"%bicycles)
'''

# 2)组织列表
print("reverse the list:")
bicycles.reverse()	#反转排序，不是按字母顺序排序
print("%s\n"%bicycles)
print("len get the length of the list")
print(len(bicycles))

print("sorted temporarily by order")
print(sorted(bicycles))
print("%s\n"%bicycles)

print("sort permanently by order")
bicycles.sort()
print("%s\n"%bicycles)

print("sort permanently by reverse order")
bicycles.sort(reverse=True)
print("%s\n"%bicycles)



bubble = [2,1,5,4,6]
bubble[0],bubble[1] = bubble[1],bubble[0]

print(str(bubble[0]) + ' ' + str(bubble[1]))
print(bubble[0],'',bubble[1])
print("%d  %d"%(bubble[0],bubble[1]))


