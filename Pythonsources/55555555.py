def test(n):
    if isinstance(n,bool):
        if n == True:
            print('ok')

        elif n == False:
            print('not OK')

    else:
        print('No known parameter!')


test(False)

# def test(n):
#     if type(n) == int:
#         print('Please input True or False to choose.')
#
#     elif type(n) == bool:
#         if n == True:
#             print('ok')
#
#         elif n == False:
#             print('not OK')
#
#     else:
#         print('No known parameter!')
#
#
# test(True)