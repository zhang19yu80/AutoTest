class ZYException(Exception):
    def __init__(self,mess):
        self.message = mess

    # def __str__(self):
    #     return 'rrew'

try:
    raise ZYException('半天不来电！')
except ZYException as e:
    print(e)
