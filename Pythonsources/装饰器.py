import time


def timer(func):
    def calc(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('You have take %s seconds for run %s'%(end_time - start_time, func))
    return calc


@timer
def test1():
    time.sleep(2)
    print('running testing1...')


@timer # test2 = calc(test2)
def test2(name,age):
    time.sleep(2)
    print('running testing2...,you name is %s, old years is %s'%(name,age))


print(test1())
test2('ZhangYu',38)

# username = 'Yu'
# password = 123
#
# def auth(auth_type):
#     def outwapperw(func):
#         def wapperw (*args,**kwargs):
#             if auth_type == 'local':
#                 un = input('your name is:').strip()
#                 pw = int(input('your pw is:').strip())
#                 if username == un and password == pw:
#                     print('your sign up.')
#                     func(*args,**kwargs)
#                 else:
#                     print('Username or password your typed invalid!')
#
#             else:
#                 print('You are using ldap.')
#         return wapperw
#     return outwapperw
#
# def index():
#     print('welcome to index page.')
#
# @auth(auth_type = 'local')
# def home():
#     print('welcome to home page.')
# @auth(auth_type = 'ldap')
# def bbs():
#     print('welcome to bbs page')
#
# index()
# home()
# bbs()