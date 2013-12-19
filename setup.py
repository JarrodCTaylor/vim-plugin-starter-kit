from setuptools import setup, find_packages


setup(
    name="scaffold-vim-plugin",
    version='0.0.1',
    description="",  # TODO
    long_description=file('README.md').read(),
    author="Jarrod C. Taylor",
    author_email="",  # TODO
    url="",  # TODO
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        # TODO https://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    tests_require=file('requirements.txt').read().split('\n'),
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
            'scaffold-vim-plugin = scaffold_vim_plugin.create_plugin_scaffold:create_scaffold'
        ]
    }
)
