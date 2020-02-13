if __name__ == '__main__':
    # defaultdict
    from collections import *

    default_dict = defaultdict(int)
    default_dict['key']  # 이렇게 하더라도 default의 값이 들어가게 됨
    # undefined
    try:
        print("something")
    except NameError as e:  # undefined 처리하는 방법
        print(e)
    from collections import deque

    # Queue
    queue = deque()
    queue.append(1)
    queue.append(2)
    print(queue.popleft())
    # OrderedDict 사용자가 넣은 순서를 보장하는 딕셔너리
    d = OrderedDict.fromkeys('adfasd')
    print(d)
    # NamedTuple
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(1, 2)
    point
    # itertools
    # map : f
    map(lambda x: x + 2, range(10))
    # filter : filter
    filter(lambda x: x % 2, range(100))


    def tool(iterable):
        for x in iterable:
            if x < 2:
                yield x
            else:
                break;


    b = tool([1, 2, 3, 4])
    try:
        while True:
            next(b)
    except StopIteration as e:
        print(e)
    from itertools import tee
    # functools'
    from functools import lru_cache


    @lru_cache(maxsize=2)
    def fibo(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        return fibo(n - 1) + fibo(n - 2)


    from functools import partial, wraps


    def f(x, y):
        return x + y


    def decorator(func):
        @wraps
        def wrap(*args, **kwargs):
            print("start")
            func(*args, **kwargs)
            print("end")

        return wrap
