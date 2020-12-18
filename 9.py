from files import import_input


def part1(_l: list, preamble: int):
    for i in range(preamble, len(_l)):
        sums = [int(x) + int(y) for x in _l[i-preamble:i] for y in _l[i-preamble:i] if x != y]
        if int(_l[i]) not in sums:
            return int(_l[i])


def part2(_l: list, preamble: int):
    value = part1(_l, preamble)
    for i in range(len(_l)):
        sum = 0
        l2 = []
        for j in range(i, len(_l)):
            sum += int(_l[j])
            l2.append(int(_l[j]))
            if sum == value:
                return min(l2)+max(l2)
            if sum > value:
                break


if __name__ == '__main__':
    i_file = import_input('files/9.txt')
    print(i_file)
    print(part2(i_file, 25))
