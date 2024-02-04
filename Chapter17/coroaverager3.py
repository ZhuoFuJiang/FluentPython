from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委托生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()


# 客户端代码，即调用方
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


# 输入报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print("{:2} {:5} averaging {:.2f}{}".format(result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.4],
    'girls;m': [1.6, 1.51, 1.4],
    'boys;kg': [39.0, 40.8, 43.2],
    'boys;m': [1.38, 1.5, 1.32]
}


if __name__ == "__main__":
    main(data)