class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print('为%s办理学员注册手续'%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,sta_obj):
        print('为%s办理雇佣手续'%sta_obj.name)
        self.staffs.append(sta_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass
        # if 'salary' and 'course' in kwargs:
        #     print('''
        #     ---- Info of teacher：%s ----
        #     Name: %s
        #     Age: %s
        #     Sex: %s
        #     Salary: %s
        #     Course: %s
        #     '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
        #
        # elif 'stu_id' and 'grade' in kwargs:
        #     print('''
        #     ---- Info of student：%s ----
        #     Name: %s
        #     Age: %s
        #     Sex: %s
        #     Stu_id: %s
        #     Grade: %s
        #     '''%(self.name,self.name,self.age,self.sex,stu_id,grade))
        #
        # else:
        #     print('输入参数不对。')

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- Info of teacher：%s ----
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('%s is teaching course %s'%(self.name,self.course))

class Student (SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade


    def tell(self):
        print('''
        ---- Info of student：%s ----
        Name: %s
        Age: %s
        Sex: %s
        Stu_id: %s
        Grade: %s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print('%s has paid tuition for $%s'%(self.name,amount))

class Course(object):
    def __init__(self,course,time):
        self.course = course
        self.time = time


# school = School('长郡开福中学','芙蓉北路')
# t1 = Teacher('黄老师',23,'女',30000,'语文')
# t2 = Teacher('周老师',29,'男',40000,'物理')
#
# s1 = Student('章鱼',18,'男',4000,'语文')
# s2 = Student('银鱼',28,'女',3000,'英语')
#
#
# s1.tell()
#
# school.enroll(s1)
# school.enroll(s2)
# school.hire(t1)
# school.hire(t2)
#
# print(school.students)
# print(school.staffs)
#
# school.staffs[0].teach()
#
#
# for stu in school.students:
#     stu.pay_tuition(4000)