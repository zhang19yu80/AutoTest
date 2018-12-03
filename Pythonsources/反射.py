def setff(self):
    print('%s加入了'%self.name)

class test123(object):
    def __init__(self,name):
        self.name = name

    def eat(self,wupin):
        print('%s在吃%s'%(self.name,wupin))


d = test123('XYZ')
user = input('请输入：').strip()

if hasattr(d,user):
    f = getattr(d,user)
    f('四八八')

else:
    setattr(d,user,setff)
    g = getattr(d,user)
    g(d)






