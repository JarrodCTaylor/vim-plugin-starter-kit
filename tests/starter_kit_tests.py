import unittest
import mock
from os import sep, path
from os.path import dirname, abspath
from inspect import currentframe, getfile
import shutil
from create_plugin_scaffold import create_scaffold


class ScaffoldTest(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree("/home/jrock/Dropbox/vim-plugin-starter-kit/vim-tests/")

    def test_create_scaffold_non_file_specific(self):
        test_new_plugin_dir = sep.join([dirname(dirname(abspath(getfile(currentframe())))), 'vim-tests', ''])
        current_dir = dirname(abspath(getfile(currentframe())))
        with mock.patch('__builtin__.raw_input', side_effect=['vim-tests', 'n']):
            create_scaffold()
            self.assertTrue(path.isdir(test_new_plugin_dir))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "plugin/tests/vim_tests_tests.py"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "plugin/tests/__init__.py"])))
            self.assertTrue(path.isdir(sep.join([test_new_plugin_dir, "doc"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "doc/vim-tests.txt"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "plugin", "vim_tests.py"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "plugin", "vim_tests.vim"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "README.md"])))
            self.assertEqual(open(current_dir + "/custom_docs/vim-tests.txt").read(),
                             open(test_new_plugin_dir + "/doc/vim-tests.txt").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests_tests.py").read(),
                             open(test_new_plugin_dir + "/plugin/tests/vim_tests_tests.py").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests.py").read(),
                             open(test_new_plugin_dir + "/plugin/vim_tests.py").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests.vim").read(),
                             open(test_new_plugin_dir + "/plugin/vim_tests.vim").read())

    def test_create_scaffold_file_specific(self):
        test_new_plugin_dir = sep.join([dirname(dirname(abspath(getfile(currentframe())))), 'vim-tests', ''])
        current_dir = dirname(abspath(getfile(currentframe())))
        with mock.patch('__builtin__.raw_input', side_effect=['vim-tests', 'y', 'python']):
            create_scaffold()
            self.assertTrue(path.isdir(test_new_plugin_dir))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "ftplugin/python/tests/vim_tests_tests.py"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "ftplugin/python/tests/__init__.py"])))
            self.assertTrue(path.isdir(sep.join([test_new_plugin_dir, "doc"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "doc/vim-tests.txt"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "ftplugin", "python", "vim_tests.py"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "ftplugin", "python", "vim_tests.vim"])))
            self.assertTrue(path.isfile(sep.join([test_new_plugin_dir, "README.md"])))
            self.assertEqual(open(current_dir + "/custom_docs/vim-tests.txt").read(),
                             open(test_new_plugin_dir + "/doc/vim-tests.txt").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests_tests.py").read(),
                             open(test_new_plugin_dir + "/ftplugin/python/tests/vim_tests_tests.py").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests.py").read(),
                             open(test_new_plugin_dir + "/ftplugin/python/vim_tests.py").read())
            self.assertEqual(open(current_dir + "/custom_docs/vim_tests.vim").read(),
                             open(test_new_plugin_dir + "/ftplugin/python/vim_tests.vim").read())
