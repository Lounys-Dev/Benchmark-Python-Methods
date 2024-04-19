from json import dump
from random import randint
from timeit import timeit

numbers: list[int] = [randint(0, 1000) for _ in range(100)]

n_range = [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]
data = {"loop_generator": {"x": n_range, "y": []}, "loop_list": {"x": n_range, "y": []}, "map": {"x": n_range, "y": []},
        "list_comprehension": {"x": n_range, "y": []}, "generator": {"x": n_range, "y": []}}


def with_for_loop_generator():
    for num in numbers:
        yield str(num)


def with_for_loop_list():
    to_return = []
    for num in numbers:
        to_return.append(str(num))
    return to_return


def with_map():
    return map(str, numbers)


def with_list_comprehension():
    return [str(x) for x in numbers]


def with_generator():
    return (str(x) for x in numbers)


for r_times in n_range:
    loop_list_time = timeit(with_for_loop_list, number=r_times)
    loop_generator_time = timeit(with_for_loop_generator, number=r_times)
    map_time = timeit(with_map, number=r_times)
    list_comprehension_time = timeit(with_list_comprehension, number=r_times)
    generator_time = timeit(with_generator, number=r_times)
    
    for key, value in zip(("loop_generator", "loop_list", "map", "list_comprehension", "generator"),
                          (loop_generator_time, loop_list_time, map_time, list_comprehension_time, generator_time)):
        data[key]["y"].append(value)

with open("data.json", "w") as f:
    dump(data, f)
