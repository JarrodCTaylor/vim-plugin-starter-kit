from os import path, sep


def assert_files_in_dir(file_names, dir_name):
    for file_name in file_names:
        assert_file_in_dir(file_name, dir_name)


def assert_file_in_dir(file_name, dir_name):
    assert path.isfile(sep.join([dir_name, file_name])), "{} is not in {}".format(file_name, dir_name)


def assert_file_contents_equal(first, second):
    first_data = open(first).read()
    second_data = open(second).read()
    print first_data
    print second_data
    assert first_data == second_data, "'{}' != '{}'".format(first_data, second_data)
