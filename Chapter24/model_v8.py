import abc
import collections


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        name = cls.__name__
        index = cls.__counter
        cls.__counter += 1
        self.storage_name = '_{}#{}'.format(name, index)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        return


class Quantity(Validated):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        return value


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("value not be empty or blank")
        return value


class EntityMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = "_{}#{}".format(type_name, key)
                cls._field_names.append(key)


class Entity(metaclass=EntityMeta):

    @classmethod
    def field_names(cls):
        for name in cls._field_names:
            yield name
