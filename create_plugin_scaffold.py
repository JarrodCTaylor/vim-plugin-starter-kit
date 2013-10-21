from os import makedirs, sep, rename
from os.path import dirname, abspath
from inspect import currentframe, getfile
import shutil


def create_scaffold():
    paths, plugin_name, plugin_type = get_user_inputs()
    build_scaffold_based_on_template(paths, plugin_type)
    customize_template(paths, plugin_name, plugin_type)


def get_user_inputs():
    plugin_name = raw_input("Enter the name of your plugin => ")
    file_specific = raw_input("Is this is file specific plugin? (y/n) => ")
    plugin_type = None
    paths = get_paths(plugin_name, plugin_type)
    if file_specific in ['y', 'Y']:
        plugin_type = raw_input("What file type is it specific for? => ")
        paths = get_paths(plugin_name, plugin_type)
        return paths, plugin_name, plugin_type
    return paths, plugin_name, plugin_type


def get_paths(plugin_name, plugin_type):
    paths = {}
    paths['current_dir'] = dirname(abspath(getfile(currentframe())))
    paths['path_to_new_plugin'] = "{}/{}/".format(paths['current_dir'], plugin_name)
    paths['path_to_templates'] = "{}/templates".format(paths['current_dir'])
    paths['template_tests_dir'] = sep.join([paths['path_to_templates'], 'tests', ''])
    paths['new_plugin_tests_dir'] = sep.join([paths['current_dir'], plugin_name, 'plugin', 'tests'])
    paths['template_doc_dir'] = sep.join([paths['path_to_templates'], 'doc', ''])
    paths['new_plugin_doc_dir'] = sep.join([paths['current_dir'], plugin_name, 'doc'])
    paths['template_py_file'] = sep.join([paths['path_to_templates'], 'template.py'])
    paths['plugin_py_file'] = sep.join([paths['path_to_new_plugin'], 'plugin', 'template.py'])
    paths['template_vim_file'] = sep.join([paths['path_to_templates'], 'template.vim'])
    paths['plugin_vim_file'] = sep.join([paths['path_to_new_plugin'], 'plugin', 'template.vim'])
    paths['template_readme_file'] = sep.join([paths['path_to_templates'], 'README.md'])
    paths['plugin_readme_file'] = sep.join([paths['path_to_new_plugin'], 'README.md'])
    if plugin_type:
        paths['plugin_vim_file'] = sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type, 'template.vim'])
        paths['plugin_py_file'] = sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type, 'template.py'])
        paths['new_plugin_tests_dir'] = sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type, 'tests'])
    return paths


def build_scaffold_based_on_template(paths, plugin_type):
    makedirs("{}/".format(paths['path_to_new_plugin']))
    if plugin_type:
        makedirs("{}/".format(sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type])))
    shutil.copytree(paths['template_tests_dir'], paths['new_plugin_tests_dir'])
    shutil.copytree(paths['template_doc_dir'], paths['new_plugin_doc_dir'])
    shutil.copyfile(paths['template_py_file'], paths['plugin_py_file'])
    shutil.copyfile(paths['template_vim_file'], paths['plugin_vim_file'])
    shutil.copyfile(paths['template_readme_file'], paths['plugin_readme_file'])


def customize_template(paths, plugin_name, plugin_type):
    plugin_underscored = plugin_name.replace("-", "_")
    customize_readme(paths, plugin_name)
    customize_doc(paths, plugin_name)
    customize_tests(paths, plugin_name, plugin_underscored)
    customize_py_file(paths, plugin_underscored)
    customize_vim_file(paths, plugin_underscored)
    rename(sep.join([paths['new_plugin_tests_dir'], 'template_tests.py']),
           sep.join([paths['new_plugin_tests_dir'], plugin_underscored + '_tests.py']))
    rename(sep.join([paths['new_plugin_doc_dir'], 'template.txt']),
           sep.join([paths['new_plugin_doc_dir'], plugin_name + '.txt']))
    if plugin_type:
        rename(paths['plugin_py_file'],
               sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type, plugin_underscored + '.py']))
        rename(paths['plugin_vim_file'],
               sep.join([paths['path_to_new_plugin'], 'ftplugin', plugin_type, plugin_underscored + '.vim']))
    else:
        rename(paths['plugin_py_file'],
               sep.join([paths['path_to_new_plugin'], 'plugin', plugin_underscored + '.py']))
        rename(paths['plugin_vim_file'],
               sep.join([paths['path_to_new_plugin'], 'plugin', plugin_underscored + '.vim']))


def customize_readme(paths, plugin_name):
    readme_contents = get_file_contents(paths['plugin_readme_file'])
    readme_contents[0] = "# {0}\n".format(plugin_name)
    readme_contents[1] = "\n"
    write_to_file(readme_contents, paths['plugin_readme_file'])


def customize_doc(paths, plugin_name):
    doc_file_path = sep.join([paths['new_plugin_doc_dir'], 'template.txt'])
    doc_contents = get_file_contents(doc_file_path)
    doc_contents[0] = "*{}.txt* ".format(plugin_name) + " ".join(doc_contents[0].split(" ")[1:])
    doc_contents[3] = "CONTENTS {0}*{1}*\n".format(" " * (68 - len(plugin_name)), plugin_name)
    doc_contents[5] = "    1. Intro {0} |{1}-intro|\n".format("." * (57 - len(plugin_name)), plugin_name)
    doc_contents[6] = "    2. Installation {0} |{1}-installation|\n".format("." * (43 - len(plugin_name)), plugin_name)
    doc_contents[7] = "    3. Requirements {0} |{1}-requirements|\n".format("." * (43 - len(plugin_name)), plugin_name)
    doc_contents[8] = "    4. Usage {0} |{1}-usage|\n".format("." * (57 - len(plugin_name)), plugin_name)
    doc_contents[9] = "    5. Licence {0} |{1}-licence|\n".format("." * (53 - len(plugin_name)), plugin_name)
    doc_contents[11] = "1. Intro{0}*{1}-intro*\n".format(" " * (63 - len(plugin_name)), plugin_name)
    doc_contents[15] = "2. Installation{0}*{1}-installation*\n".format(" " * (49 - len(plugin_name)), plugin_name)
    doc_contents[19] = "3. Requirements{0}*{1}-requirements*\n".format(" " * (49 - len(plugin_name)), plugin_name)
    doc_contents[23] = "4. Usage{0}*{1}-usage*\n".format(" " * (63 - len(plugin_name)), plugin_name)
    doc_contents[27] = "5. Licence{0}*{1}-licence*\n".format(" " * (59 - len(plugin_name)), plugin_name)
    write_to_file(doc_contents, doc_file_path)


def customize_tests(paths, plugin_name, plugin_underscored):
    plugin_camel = "".join([word.title() for word in plugin_name.split("-")])
    tests_file_path = sep.join([paths['new_plugin_tests_dir'], 'template_tests.py'])
    tests_contents = get_file_contents(tests_file_path)
    tests_contents[1] = "import {} as sut\n".format(plugin_underscored)
    tests_contents[4] = "class {}Tests(unittest.TestCase):\n".format(plugin_camel)
    tests_contents[7] = "        result = sut.{}_example()\n".format(plugin_underscored)
    write_to_file(tests_contents, tests_file_path)


def customize_py_file(paths, plugin_underscored):
    py_file_contents = get_file_contents(paths['plugin_py_file'])
    py_file_contents[0] = "def {}_example():\n".format(plugin_underscored)
    write_to_file(py_file_contents, paths['plugin_py_file'])


def customize_vim_file(paths, plugin_underscored):
    vim_file_contents = get_file_contents(paths['plugin_vim_file'])
    vim_file_contents[13] = "from {} import {}_example\n".format(plugin_underscored, plugin_underscored)
    vim_file_contents[16] = "    print({}_example())\n".format(plugin_underscored)
    write_to_file(vim_file_contents, paths['plugin_vim_file'])


def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def write_to_file(data, file_path):
    with open(file_path, 'w') as f:
        for line in data:
            f.write(line)

if __name__ == "__main__":
    create_scaffold()
