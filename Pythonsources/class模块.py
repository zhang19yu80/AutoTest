#
# class Role:
#     def __init__(self,name,role,weapon,life_value=100,money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money= money
#
#     def got_shot(self):
#         self.life_value -= 50
#         print("%s:ah...,I got shot..."% self.name)
#
#     def buy_gun(self, gun_name):
#         print("%s just bought %s" % (self.name,gun_name) )
#
#
#
#
# r1 = Role('ZhangYu','Police','AK47')
# r1.buy_gun('M24')


class Date(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

t = Date(23,10,2018)
print(t)
