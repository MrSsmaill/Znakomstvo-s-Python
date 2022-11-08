# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо сформировать список кортежей вида (tutor, group).

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
def class_list(tutors:list,groups:list)->list:
    classes = []
    for i in range(len(tutors)):
        elem = ()
        if i >= len(groups):
            elem = (tutors[i], None)
        else:
            elem = (tutors[i], groups[i])
        classes.append(elem)
    return classes

print(class_list(tutors,groups))
