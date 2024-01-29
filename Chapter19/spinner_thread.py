import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        # -r表示将光标重置到开始
        status = f'\r{char}{msg}'
        print(status, end='', flush=True)
        # wait会阻塞线程，直到内部标记被设置为True
        # 等待time超时后，也会非阻塞，但是不会改变内部标记，除非调用了Event.set
        if done.wait(.1):
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == "__main__":
    main()

