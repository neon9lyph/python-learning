def log(func):
    def wrapper2(*args, **kwargs):
        print("wrapper 收到的位置参数：", args)
        print("wrapper 收到的关键字参数：", kwargs)

        return func(*args, **kwargs)

    return wrapper2


@log
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"


result = greet("小明", greeting="早上好")
print(result)
print(greet.__name__)  # greet
print(greet.__doc__)  # 向指定的人打招呼。

# def log(func):
#     def wrapper(*args, **kwargs):
#         print("开始执行")
#         return func(*args, **kwargs)

#     return wrapper


# @log
# def greet(name):
#     """向指定的人打招呼。"""
#     return f"你好，{name}！"


# print(greet.__name__)  # wrapper
# print(greet.__doc__)  # None


from functools import wraps


def log2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始执行")
        return func(*args, **kwargs)

    return wrapper


@log2
def greet(name):
    """向指定的人打招呼。"""
    return f"你好，{name}！"


print(greet.__name__)  # greet
print(greet.__doc__)  # 向指定的人打招呼。
