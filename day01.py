def get_frequency(numbers):
    return sum(numbers)


def get_dejavu(numbers):
    frequencies = {0}
    frequency = 0

    while True:
        for n in numbers:
            frequency += n
            if frequency in frequencies:
                return frequency
            frequencies.add(frequency)


if __name__ == "__main__":
    data = [int(line.strip()) for line in open("day01.txt", "r")]

    print('resulting frequency:', get_frequency(data))
    print('dejavu frequency:', get_dejavu(data))

    # part 1
    assert get_frequency([+1, +1, +1]) == 3
    assert get_frequency([+1, +1, -2]) == 0
    assert get_frequency([-1, -2, -3]) == -6

    # part 2
    assert get_dejavu([+1, -1]) == 0
    assert get_dejavu([+3, +3, +4, -2, -4]) == 10
    assert get_dejavu([-6, +3, +8, +5, -6]) == 5
    assert get_dejavu([+7, +7, -2, -7, -4]) == 14

