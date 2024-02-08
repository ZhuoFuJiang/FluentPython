from collections import abc
from keyword import iskeyword


class FrozenJSON:
    """
    一个可读接口，适用属性表示方法访问json类对象
    """
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return self.__data[name]
        else:
            return FrozenJSON(self.__data[name])


if __name__ == "__main__":
    json_data = {"Schedule":
                     {"Schedule": [1, 2, 3, 4]}}
    a = FrozenJSON(json_data)
    print(a.Schedule.Schedule[0])
