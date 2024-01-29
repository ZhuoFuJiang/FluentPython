import asyncio
import itertools
import time


def main() -> None:
    # main将会被阻塞
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    # await将阻塞supervisor直到slow返回
    result = await slow()
    # cancel将抛出CancelledError异常
    spinner.cancel()
    return result


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        # -r表示将光标重置到开始
        status = f'\r{char}{msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


async def slow() -> int:
    # 不会阻塞其他协程
    # time.sleep(3)
    await asyncio.sleep(3)
    return 42


if __name__ == "__main__":
    main()
