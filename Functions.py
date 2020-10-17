def say_hello():
    """注释注释"""
    print("hello")


def sum_2_num(num1, num2):
    result = num1 + num2
    return result


def print_line(char, time):
    print(char * time)


def print_lines(char, time):
    """打印多行分割线

    :param char: 分割线使用的字符
    :param time: 分割线使用的次数
    """
    i = 0
    while i < 5:
        print_line(char, time)
        i += 1


name = "SMY"
