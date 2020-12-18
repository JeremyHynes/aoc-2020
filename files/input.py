
def import_input(file, type=str):
    with open(file) as _f:
        i_file = _f.readlines()

    return [type(line.strip('\n')) for line in i_file]