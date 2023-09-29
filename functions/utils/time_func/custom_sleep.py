from time import perf_counter


def sleep(duration: float, get_now=perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()
