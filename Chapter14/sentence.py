import re
import reprlib
from collections import abc


# 匹配数字、字母、下划线
RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # def __iter__(self):
    #     pass


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')
    for word in s:
        print(word)

    # Iterable只考虑__iter__方法
    print(issubclass(Sentence, abc.Iterable))
    print(isinstance(s, abc.Iterable))

    it = iter(s)
    print(next(it))
