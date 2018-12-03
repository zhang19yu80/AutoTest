import pymysql

# # name = input('请输入姓名：')
# # id1 = input('请输入ID：')
#
# sql = 'insert into zy_users values(0,'Zhang Yu','A9993E364706816ABA3E25717850C26C9CD0D89D')'
# # params = [name,id1]
#
# myconnect = mysqlclass('58.20.17.84',3306,'sdadmin','sdadmin','rent_car_822')
# result1 = myconnect.actionsql(sql)
#
# if len(result1) == 0:
#     print('没有查询到任何数据。')
#
# else:
#     print(result1)



conn = pymysql.connect(
    host='58.20.17.84',
    port=3306,
    user='sdadmin',
    passwd='sdadmin',
    db='rent_car_822',
    charset='utf8'
)
son = conn.cursor()
# son.execute("INSERT INTO z_students (id,name,gender,birthday,note) values('0','Qui','0','2018-5-9','dfedsddfdf')")
# print('成功插入',son.rowcount,'条数据')
# conn.commit()
# son.close()
# conn.close()
# name = input('请输入用户名：')
# cursor = connect.cursor()

sql = "insert into zy_users values(0,'Zhang Yu','A9993E364706816ABA3E25717850C26C9CD0D89D')"
# data = (0,'Zhang Yu','A9993E364706816ABA3E25717850C26C9CD0D89D')

son.execute(sql)
conn.commit()
print('成功插入', son.rowcount,'调数据')


# import logging
#
# def use_logging(func):
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()
#     return wrapper
#
# @use_logging
# def foo():
#     print('i am foo')
#
# foo()









# from enum import Enum, unique
#
# Gender = Enum('gender',('Male', 'Female'))
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, w_value):
#         self._width = w_value
#
#     @property
#     def height(self):
#         return self._height
#
#     @width.setter
#     def height(self, h_value):
#         self._height = h_value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
#
#
#
# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1


# L = list(filter(lambda x: x % 2 ==1, range(1,20)))
# print(L)

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
#
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#
# def createCounter():
#     n = 0
#     def counter():
#         nonlocal n
#         n += 1
#         return n
#     return counter
#
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
#
# f1 = count()
# f1()

# recode = input('请输入你想要检查的字符：')
# dicts = {}
# for i in recode:
#     if i in dicts:
#         dicts[i] += 1
#     else: = 1
# print(dicts)
#         dicts[i]


# print('=' * 30)
# print('学生管理系统'.center(20,'*'))
# print('输入 1 ： 增加学生名字')
# print('输入 2 ： 查找学生名字')
# print('输入 3 ： 修改学生名字')
# print('输入 4 ： 删除学生名字')
# print('输入 5 ： 查看学生名字')
# print('输入 6 ： 退出')
# print('=' * 30)
#
# adminsystem = []
#
# while True:
#     try:
#         action = int(input('请输入数字以进行相关操作'))
#
#     except ValueError as e:
#         print('未输入数字而无法继续,错误码：',e)
#         print('=' * 30)
#
#     else:
#
#         if action == 1:
#             Newname = input('请输入新增同学的名字：')
#             adminsystem.append(Newname)
#             print('=' * 30)
#
#         elif action == 2:
#             Foundname = input('请输入要查找同学的名字：')
#             if Foundname in adminsystem:
#                 print('找到该同学了。')
#                 print('=' * 30)
#             else:
#                 print('未到该同学。')
#                 print('=' * 30)
#
#         elif action == 3:
#             Modifyname = input('请输入要修改同学的名字：')
#             if Modifyname in adminsystem:
#                 x = adminsystem.index(Modifyname)
#                 adminsystem.remove(Modifyname)
#                 NewModifyname = input('请输入新的名字：')
#                 adminsystem.insert(x,NewModifyname)
#                 print('=' * 30)
#             else:
#                 print('未找到该同学，无法修改他。')
#                 print('=' * 30)
#
#         elif action == 4:
#             Deletename = input('请输入要删除同学的名字：')
#             if Deletename in adminsystem:
#                 adminsystem.remove(Deletename)
#                 print('=' * 30)
#             else:
#                 print('未找到该同学，无法删除他。')
#                 print('=' * 30)
#
#         elif action == 5:
#             if len(adminsystem) == 0:
#                 print('还未录入任何学生。')
#                 print('=' * 30)
#             else:
#                 print('已登记学生：', adminsystem)
#                 print('=' * 30)
#
#         elif action == 6:
#             break
#
#         else:
#             print('请输入1到6之间的数字来选择相应操作。')
#             print('=' * 30)






# L1 = list(filter(lambda x: x % 2 == 1,range(1,20)))

# def createCounter():
#     s = 0
#     def counter():
#         nonlocal s
#         s = s + 1
#         return s
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5




# def Caps_list(numbers):
#     s = []
#     for n in numbers:
#         n = n[0].upper() + n[1:].lower()
#         s.append(n)
#     return s
#
# l = ['hELlo','WELL','good']
# l1 =Caps_list(l)
#
# for n in l1:
#     print(n)


# def print_lol(the_list):
#      for item in the_list:
#          if isinstance(item,list):
#              print_lol(item)
#          else:
#              print(item)

# name = [1,2,'e',[3,4,['w','t']]]
# print_lol(name)



# def normalize(name):
#     name=name[0].upper()+name[1:].lower()
#     return name
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('生成器返回值：', e)
#         break







# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     else:
#         Min = Max = L[0]
#         for i in L:
#             if i <= Min:
#                 Min = i
#             if i >= Max:
#                 Max = i
#
#         return (Min, Max)
#
# print(findMinAndMax([1,8,5,3]))


# def trim(s):
#     while s[:1] == ' ':
#        s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s

#
# def product(*number):#这个方法接受一个或多个可变参数，并求它们的乘积
#     if not isinstance(number, (int, float,tuple)):
#         raise TypeError('请输入整数或浮点数的值！')
#     elif len(number) < 1:
#         raise TypeError('请输入一个值！')
#     else:
#         sum = 1
#         for n in number:
#             sum = sum * n
#         return sum
#
# def check_produce(): #验证上面这个方法的可靠性
#     if product(5) != 5:
#         print('测试失败!')
#     elif product(5, 6) != 30:
#         print('测试失败!')
#     elif product(5, 6, 7) != 210:
#         print('测试失败!')
#     elif product(5, 6, 7, 9) != 1890:
#         print('测试失败!')
#     else:
#         try:
#             product()
#             print('测试失败!')
#         except TypeError:
#             print('长度测试通过!')
#         finally:
#             try:
#                 product('x','y')
#                 print('ceshishibai')
#             except TypeError:
#                 print('非数字测试通过!')
#
#     print('祝贺，整个业务逻辑测试通过！！！')
#
# check_produce()



