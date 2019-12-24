if __name__ == '__main__':
    import datetime as dt
    import my_python_library as my_py

    dt_time = dt.datetime.now()

    print(dt_time)
    my_py.utils1.my_func1()
    my_py.my_func2()

    my_py.my_func_class.print_my_name()

