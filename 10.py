from files import import_input


def part1(_l: list, pos: int):
    if pos == max(_l):
        return 0, 1

    if pos + 1 in _l:
        one, three = part1(_l, pos + 1)
        return 1 + one, three
    elif pos + 3 in _l:
        one, three = part1(_l, pos + 3)
        return one, 1 + three
    print('Strange behaviour')
    print(_l, pos)
    return 0, 0


def part2(_l: list):
    _l.append(max(_l) + 3)
    _l.append(0)
    _l = sorted(_l)
    _l = list(reversed(_l))

    # init
    s = {}
    for i in _l:
        count = 1 if i == max(_l) else 0
        if i+1 in s:
            count += s[i+1]
        if i+2 in s:
            count += s[i+2]
        if i+3 in s:
            count += s[i+3]
        s[i] = count
        print(i, count)
    return s[0]


if __name__ == '__main__':
    i_file = import_input('files/10.txt', type=int)
    print(part2(i_file))
