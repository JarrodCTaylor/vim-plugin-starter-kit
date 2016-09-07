from os import makedirs, sep, rename, getcwd
from os.path import dirname, abspath
import shutil


def create_scaffold():
    paths, plugin_name, plugin_type, github_user = get_user_inputs()
    build_scaffold_based_on_template(paths, plugin_type)
    customize_template(paths, plugin_name, plugin_type, github_user)


def get_user_inputs():
    plugin_name = raw_input("Enter the name of your plugin => ")
    github_user = raw_input("Enter your github user name => ")
    file_specific = raw_input("Is this a file specific plugin? (y/n) => ")
    plugin_type = None
    if file_specific in ['y', 'Y']:
        plugin_type = raw_input("What file type is it specific for? => ")
        paths = get_paths(plugin_name, plugin_type)
        return paths, plugin_name, plugin_type, github_user
    paths = get_paths(plugin_name, plugin_type)
    return paths, plugin_name, plugin_type, github_user


def get_paths(plugin_name, plugin_type):
    paths = {}

    paths['current_dir'] = abspath(dirname(__file__))
    paths['new_plugin_path'] = sep.join([getcwd(), plugin_name])
    paths['path_to_templates'] = sep.join([paths['current_dir'], 'templates'])
    paths['template_tests_dir'] = sep.join([paths['path_to_templates'], 'tests', ''])
    paths['new_plugin_tests_dir'] = sep.join([paths['new_plugin_path'], 'plugin', 'tests'])
    paths['template_doc_dir'] = sep.join([paths['path_to_templates'], 'doc', ''])
    paths['new_plugin_doc_dir'] = sep.join([paths['new_plugin_path'], 'doc'])
    paths['template_py_file'] = sep.join([paths['path_to_templates'], 'template.py'])
    paths['plugin_py'] = sep.join([paths['new_plugin_path'], 'plugin', 'template.py'])
    paths['template_vim_file'] = sep.join([paths['path_to_templates'], 'template.vim'])
    paths['plugin_vim'] = sep.join([paths['new_plugin_path'], 'plugin', 'template.vim'])
    paths['template_readme_file'] = sep.join([paths['path_to_templates'], 'README.md'])
    paths['plugin_readme_file'] = sep.join([paths['new_plugin_path'], 'README.md'])
    if plugin_type:
        paths['plugin_vim'] = sep.join([paths['new_plugin_path'], 'ftplugin', plugin_type, 'template.vim'])
        paths['plugin_py'] = sep.join([paths['new_plugin_path'], 'ftplugin', plugin_type, 'template.py'])
        paths['new_plugin_tests_dir'] = sep.join([paths['new_plugin_path'], 'ftplugin', plugin_type, 'tests'])
    return paths


def build_scaffold_based_on_template(paths, plugin_type):
    if plugin_type:
        makedirs(sep.join([paths['new_plugin_path'], 'ftplugin', plugin_type]))
    else:
        makedirs(sep.join([paths['new_plugin_path'], 'plugin']))
    shutil.copytree(paths['template_tests_dir'], paths['new_plugin_tests_dir'])
    shutil.copytree(paths['template_doc_dir'], paths['new_plugin_doc_dir'])
    shutil.copyfile(paths['template_py_file'], paths['plugin_py'])
    shutil.copyfile(paths['template_vim_file'], paths['plugin_vim'])
    shutil.copyfile(paths['template_readme_file'], paths['plugin_readme_file'])


def customize_template(paths, plugin_name, plugin_type, github_user):
    plugin_under = plugin_name.replace("-", "_")
    customize_readme(paths, plugin_name, github_user)
    customize_doc(paths, plugin_name)
    customize_tests(paths, plugin_name, plugin_under)
    customize_py_file(paths, plugin_under)
    customize_vim_file(paths, plugin_under)
    custom_rename(paths, plugin_under, plugin_name, plugin_type)


def custom_rename(paths, plugin_under, plugin_name, plugin_type):
    rename(sep.join([paths['new_plugin_tests_dir'], 'template_tests.py']),
           sep.join([paths['new_plugin_tests_dir'], plugin_under + '_tests.py']))
    rename(sep.join([paths['new_plugin_doc_dir'], 'template.txt']),
           sep.join([paths['new_plugin_doc_dir'], plugin_name + '.txt']))

    if plugin_type:
        new_plugin_path = sep.join([paths['new_plugin_path'], 'ftplugin', plugin_type, plugin_under])
    else:
        new_plugin_path = sep.join([paths['new_plugin_path'], 'plugin', plugin_under])

    rename(paths['plugin_py'], new_plugin_path + '.py')
    rename(paths['plugin_vim'], new_plugin_path + '.vim')


def customize_readme(paths, plugin_name, github_user):
    params = (github_user, plugin_name)
    readme_contents = get_file_contents(paths['plugin_readme_file'])
    readme_contents[0] = "# {0}\n".format(plugin_name)
    readme_contents[1] = "\n"
    readme_contents[7] = "  - `git clone https://github.com/{0}/{1} ~/.vim/bundle/{1}`\n".format(*params)
    readme_contents[9] = "  - Add `Bundle 'https://github.com/{0}/{1}'` to .vimrc\n".format(*params)
    readme_contents[12] = "  - Add `NeoBundle 'https://github.com/{0}/{1}'` to .vimrc\n".format(*params)
    readme_contents[15] = "  - Add `Plug 'https://github.com/{0}/{1}'` to .vimrc\n".format(*params)
    write_to_file(readme_contents, paths['plugin_readme_file'])


def customize_doc(paths, plugin_name):
    doc_file_path = sep.join([paths['new_plugin_doc_dir'], 'template.txt'])
    doc_contents = get_file_contents(doc_file_path)
    doc_contents[0] = "*{}.txt* ".format(plugin_name) + " ".join(doc_contents[0].split(" ")[1:])
    doc_contents[3] = "CONTENTS {0}*{1}*\n".format(" " * (68 - len(plugin_name)), plugin_name)
    doc_contents[5] = "    1. Intro {0} |{1}-intro|\n".format("." * (57 - len(plugin_name)), plugin_name)
    doc_contents[6] = "    2. Requirements {0} |{1}-requirements|\n".format("." * (43 - len(plugin_name)), plugin_name)
    doc_contents[7] = "    3. Usage {0} |{1}-usage|\n".format("." * (57 - len(plugin_name)), plugin_name)
    doc_contents[8] = "    4. Licence {0} |{1}-licence|\n".format("." * (53 - len(plugin_name)), plugin_name)
    doc_contents[10] = "1. Intro{0}*{1}-intro*\n".format(" " * (63 - len(plugin_name)), plugin_name)
    doc_contents[14] = "2. Requirements{0}*{1}-requirements*\n".format(" " * (49 - len(plugin_name)), plugin_name)
    doc_contents[18] = "3. Usage{0}*{1}-usage*\n".format(" " * (63 - len(plugin_name)), plugin_name)
    doc_contents[22] = "4. Licence{0}*{1}-licence*\n".format(" " * (59 - len(plugin_name)), plugin_name)
    write_to_file(doc_contents, doc_file_path)


def customize_tests(paths, plugin_name, plugin_under):
    plugin_camel = "".join([word.title() for word in plugin_name.split("-")])
    tests_file_path = sep.join([paths['new_plugin_tests_dir'], 'template_tests.py'])
    tests_contents = get_file_contents(tests_file_path)
    tests_contents[1] = "import {} as sut\n".format(plugin_under)
    tests_contents[5] = "class {}Tests(unittest.TestCase):\n".format(plugin_camel)
    tests_contents[8] = "        result = sut.{}_example()\n".format(plugin_under)
    write_to_file(tests_contents, tests_file_path)


def customize_py_file(paths, plugin_under):
    py_file_contents = get_file_contents(paths['plugin_py'])
    py_file_contents[0] = "def {}_example():\n".format(plugin_under)
    write_to_file(py_file_contents, paths['plugin_py'])


def customize_vim_file(paths, plugin_under):
    vim_file_contents = get_file_contents(paths['plugin_vim'])
    vim_file_contents[13] = "from {} import {}_example\n".format(plugin_under, plugin_under)
    vim_file_contents[16] = "    print({}_example())\n".format(plugin_under)
    write_to_file(vim_file_contents, paths['plugin_vim'])


def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def write_to_file(data, file_path):
    with open(file_path, 'w') as f:
        for line in data:
            f.write(line)

if __name__ == "__main__":
    create_scaffold()
