def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    asdf
    asdf
    asdf
    """
    print("my first python function! {}".format(param1))

my_func(param1='bencyn')
# types
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"
result = addNum("2",'3')
print(result)
