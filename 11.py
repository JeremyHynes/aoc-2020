from files import import_input


def is_occupied(_l, x, y, i, j):
    if x+i < 0 or y+j < 0 or x+i >= len(_l) or y+j >= len(_l[0]):
        return False

    if _l[x+i][y+j] == '.':
        if i > 0:
            if j > 0:
                return is_occupied(_l, x, y, i+1, j+1)
            elif j < 0:
                return is_occupied(_l, x, y, i+1, j-1)
            return is_occupied(_l, x, y, i+1, j)
        elif i < 0:
            if j > 0:
                return is_occupied(_l, x, y, i-1, j+1)
            elif j < 0:
                return is_occupied(_l, x, y, i-1, j-1)
            return is_occupied(_l, x, y, i-1, j)
        elif j > 0:
            return is_occupied(_l, x, y, i, j+1)
        elif j < 0:
            return is_occupied(_l, x, y, i, j-1)

    return _l[x+i][y+j] == '#'


def count_direction2(_l: list, pos: (int, int), direction: str):
    count = 0
    number_dir = 5
    if direction == 't':
        for i in range(min(number_dir, pos[0])):
            if is_occupied(_l, i, pos[1]):
                count += 1
            else:
                count = 0
        return count

    if direction == 'b':
        for i in range(min(number_dir, len(_l) - pos[0]-1)):
            if is_occupied(_l, i+pos[0]+1, pos[1]):
                count += 1
            else:
                count = 0
        return count

    if direction == 'l':
        for i in range(min(number_dir, pos[1])):
            if is_occupied(_l, pos[0], i):
                count += 1
            else:
                count = 0
        return count

    if direction == 'r':
        for i in range(min(number_dir, len(_l[pos[0]]) - pos[1] -1)):
            if is_occupied(_l, pos[0], i+pos[1]+1):
                count += 1
            else:
                count = 0
        return count

    if direction == 'tr':
        for i in range(min(number_dir, len(_l[pos[0]]) - pos[1])):
            if is_occupied(_l, pos[0]-i, pos[1]+i):
                count += 1
            else:
                count = 0
        return count

    if direction == 'br':
        for i in range(min(number_dir, len(_l) - pos[0], len(_l[pos[0]]) - pos[1])):
            if is_occupied(_l, pos[0]+i, pos[1]+i):
                count += 1
            else:
                count = 0
        return count

    if direction == 'tl':
        for i in range(min(number_dir, pos[0], pos[1])):
            if is_occupied(_l, pos[0]-i, pos[1]-i):
                count += 1
            else:
                count = 0
        return count

    if direction == 'bl':
        for i in range(min(number_dir, len(_l) - pos[0], pos[1])):
            if is_occupied(_l, pos[0]+i, pos[1]-i):
                count += 1
            else:
                count = 0
        return count


def count_direction(_l: list, pos_x: int, pos_y: int):
    count = [is_occupied(_l, pos_x, pos_y, i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
    c = 0
    for i in count:
        c += 1 if i else 0
    return c


def part1(_l: list):

    directions = ['t', 'tr', 'r', 'br', 'b', 'bl', 'l', 'tl']

    l2 = _l.copy()
    for i in range(len(_l)):
        for j in range(len(_l[i])):
            if _l[i][j] == '.':
                continue
            if count_direction(_l, i, j) >= 6:
                    l2[i] = l2[i][:j] + 'L' + l2[i][j+1:]
            elif count_direction(_l, i, j) == 0 and _l[i][j] == 'L':
                l2[i] = l2[i][:j] + '#' + l2[i][j+1:]

    return l2


def pprint(content: list):
    [print(i) for i in content]
    print()


if __name__ == '__main__':
    i_file = import_input('files/11.txt')

    r = part1(i_file)
    r2 = part1(r)
    i = 0
    while True:
        i += 1

        r = r2
        r2 = part1(r)

        # pprint(r2)

        if r == r2:
            count = 0
            for line in r:
                for char in line:
                    if char == '#':
                        count += 1
            print(count)
            break

        if i >= 1000:
            break