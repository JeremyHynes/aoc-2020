from files import import_input


def part_1(file: list, acc: int, save: list, pos: int):
    if pos < 0 or pos >= len(file):
        raise ValueError(acc)

    save.append(pos)

    action, value = file[pos].split(' ')
    if action == 'acc':
        return part_1(file, eval(f'{acc}{value}'), save, pos + 1)

    elif action == 'jmp':
        next_pos = eval(f'{pos}{value}')
        if next_pos in save:
            return acc
        return part_1(file, acc, save, next_pos)

    elif action == 'nop':
        if pos + 1 in save:
            return acc
        return part_1(file, acc, save, pos + 1)
    else:
        raise ValueError(f'Unknown action {action}')


def part_2(file: list):
    for i in range(len(file)):
        if 'nop' in file[i]:
            _l = file.copy()
            _l[i] = _l[i].replace('nop', 'jmp')
            try:
                part_1(_l, 0, [], 0)
            except Exception as err:
                return err
        elif 'jmp' in file[i]:
            _l = file.copy()
            _l[i] = _l[i].replace('jmp', 'nop')
            try:
                part_1(_l, 0, [], 0)
            except Exception as err:
                return err


if __name__ == '__main__':
    i_file = import_input('files/8_bis.txt')
    print(part_2(i_file))
