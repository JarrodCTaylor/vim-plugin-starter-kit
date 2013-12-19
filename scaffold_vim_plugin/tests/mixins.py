from . import assertions
from os import sep, path


class ScaffoldTestMixin(object):

    def test_creates_directory_for_new_plugin(self):
        self.assertTrue(path.isdir(self.test_new_plugin_dir))

    def test_creates_readme(self):
        assertions.assert_file_in_dir('README.md', self.test_new_plugin_dir)

    def test_creates_tests(self):
        assertions.assert_files_in_dir(["__init__.py", "vim_tests_tests.py"], self.tests_dir)

    def test_creates_plugin_files(self):
        assertions.assert_files_in_dir(["vim_tests.py", "vim_tests.vim"], self.plugin_dir)

    def test_creates_doc_dir(self):
        self.assertTrue(path.isdir(self.doc_dir))

    def test_creates_txt_file_in_docs_dir(self):
        assertions.assert_file_in_dir('vim-tests.txt', self.doc_dir)

    def test_txt_doc_file_is_correct(self):
        assertions.assert_file_contents_equal(
            sep.join([self.source_dir, "custom_docs", "vim-tests.txt"]),
            sep.join([self.doc_dir, "vim-tests.txt"]))

    def test_test_file_is_correct(self):
        assertions.assert_file_contents_equal(
            sep.join([self.source_dir, "custom_docs", "vim_tests_tests.py"]),
            sep.join([self.plugin_dir, "tests", "vim_tests_tests.py"]))

    def test_plugin_python_file_is_correct(self):
        assertions.assert_file_contents_equal(
            sep.join([self.source_dir, "custom_docs", "vim_tests.py"]),
            sep.join([self.plugin_dir, "vim_tests.py"]))

    def test_readme_file_is_correct(self):
        assertions.assert_file_contents_equal(
            sep.join([self.source_dir, "custom_docs", "README.md"]),
            sep.join([self.test_new_plugin_dir, "README.md"]))
