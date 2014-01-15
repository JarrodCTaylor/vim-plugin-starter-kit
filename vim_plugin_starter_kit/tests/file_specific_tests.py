import unittest
import tempfile
import mock
from os import sep
from os.path import dirname, abspath
import shutil
from ..create_plugin_scaffold import create_scaffold
from .mixins import ScaffoldTestMixin


class ScaffoldNonFileSpecificTests(ScaffoldTestMixin, unittest.TestCase):

    def setUp(self):
        self.current_dir = tempfile.mkdtemp()
        self.source_dir = abspath(dirname(__file__))
        self.test_new_plugin_dir = sep.join([self.current_dir, 'vim-tests'])
        self.plugin_dir = sep.join([self.test_new_plugin_dir, "ftplugin", "python"])
        self.tests_dir = sep.join([self.plugin_dir, 'tests'])
        self.doc_dir = sep.join([self.test_new_plugin_dir, "doc"])

        with mock.patch('vim_plugin_starter_kit.create_plugin_scaffold.getcwd', return_value=self.current_dir):
            with mock.patch('__builtin__.raw_input', side_effect=['vim-tests', 'JarrodCTaylor', 'y', 'python']):
                create_scaffold()

    def tearDown(self):
        try:
            shutil.rmtree(sep.join([self.current_dir, "vim-tests"]))
        except:
            pass
