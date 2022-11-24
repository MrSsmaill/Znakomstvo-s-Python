import csv


def create(dict_group: dict, last_name: str, first_name: str, group: str) -> dict:
    id = id_save()
    dict_group.fromkeys(id)
    dict_group[id] = {'last_name': last_name, 'first_name': first_name, 'group': group}
    return dict_group


def read(dict_group: dict, id: str) -> str:
    line = ', '.join(list(dict_group[id].values()))
    return line


def delete(dict_group: dict, id: str) -> dict:
    dict_group.pop(id)
    return dict_group


def updata(dict_group: dict, last_name: str, first_name: str, group: str, id: str) -> dict:
    dict_group[id] = {'last_name': last_name, 'first_name': first_name, 'group': group}
    return dict_group


def convert_list(dict_group: dict) -> list:
    id_dict = {}
    id_list = []
    for i in range(1, len(dict_group) + 1):
        id_dict[str(i)] = ({'ID': str(i)})
        id_dict[str(i)].update(dict_group[str(i)])
        id_list.append(id_dict.setdefault(str(i)))
    return id_list


def write_data(dict_group: dict):
    list_group = convert_list(dict_group)
    with open('group.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(list_group[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in list_group:
            writer.writerow(d)


def id_check(dict_group: dict, id: str):
    return True if id in dict_group else not False


def id_save() -> str:
    with open('ID.txt', 'r+', encoding='utf-8') as data:
        id = data.read()
        data.seek(0)
        next_id = str(int(id) + 1)
        data.write(next_id)
    return id


def convert_dict():
    with open('group.csv') as f:
        reader = csv.DictReader(f)
        dict_group = {}
        for row in reader:
            id = str(row.setdefault('ID'))
            dict_group.fromkeys(id)
            dict_group[id] = {'last_name': row.setdefault('last_name'),
                              'first_name': row.setdefault('first_name'),
                              'group': row.setdefault('group')}
    return dict_group


def without_id() -> str:
    lines = ''
    with open('group.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_line = list(row.values())
            list_line.pop(0)
            line = ', '.join(list_line)
            lines += line + '\n'
    return lines


def with_id() -> str:
    lines = ''
    with open('group.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_line = list(row.values())
            line = ', '.join(list_line)
            lines += line + '\n'
    return lines
