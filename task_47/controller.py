import view
import model


def my_func():
    num_1 = model.parsing(view.data_in())
    op = view.data_op()
    num_2 = model.parsing(view.data_in())
    result=model.calculate(num_1, num_2, op)
    view.my_print(result)
