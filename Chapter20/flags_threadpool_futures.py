from concurrent import futures

from flags import save_flag, get_flag, main


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        todo: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            todo.append(future)
            print(f"Scheduled for {cc}: {future}")
        # as_completed完成一个就yield future
        for count, future in enumerate(futures.as_completed(todo), 1):
            res: str = future.result()
            print(f"{future} result: {res!r}")
    return count


if __name__ == "__main__":
    main(download_many)
