def read_data(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as data:
        a = data.read().split()
    return a


def write_data(filename: str, string_list: list):
    with open(filename, "a", encoding="utf-8") as data:
        data.write("#".join(string_list))
        data.write('\n')


def export_file(phonebook:str, filename: str):
    data = [el.split('#') for el in read_data(filename)]
    for elem in data:
        write_data(phonebook, elem)

def data_file(record):
    return '\n'.join(record)