import model
import view

dict_group = model.convert_dict()


def menu_start():
    view.menu_print()

    while True:
        point = int(view.menu())
        if point == 1:
            model.create(dict_group, view.last_name(), view.first_name(), view.group())
        elif point == 2:
            id = have_id()
            line_group = model.read(dict_group, id)
            view.read(line_group, id)
        elif point == 3:
            model.updata(dict_group, view.last_name(), view.first_name(), view.group(), have_id())
        elif point == 4:
            model.delete(dict_group, have_id())
        elif point == 5:
            model.write_data(dict_group)
        elif point == 6:
            view.print_with_id(model.with_id())
        elif point == 7:
            view.print_without_id(model.without_id())
        elif point == 8:
            model.write_data(dict_group)
            view.exit()
            exit()
        else:
            view.not_menu()


def have_id(dict_group=dict_group) -> str:
    id = view.id()
    while True:
        if model.id_check(dict_group, id):
            return id
        else:
            view.invalid_id()
