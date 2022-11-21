import view
import model


def menu():
    value = view.action()
    name_1 = view.name_phonebook()
    if value == 'wr':
        record_wr = view.data()
        model.write_data(name_1, record_wr)
    elif value == 'rd':
        record_rd = model.read_data(name_1)
        view.data_in_file(model.data_file(record_rd))
    elif value == 'ex':
        name_2 = view.file_name()
        model.export_file(name_1,name_2)

