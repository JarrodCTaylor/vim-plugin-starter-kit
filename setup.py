from setuptools import setup, find_packages


setup(
    name="scaffold-vim-plugin",
    version='0.0.1',
    description="A tool that creates a scafold for Vim plugins to be written in Python.",
    long_description=file('README.md').read(),
    author="Jarrod C. Taylor",
    author_email="jarrod.c.taylor@gmail.com",
    url="http://github.com/JarrodCTaylor/vim-plugin-starter-kit",
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Topic :: Text Editors",
        'Intended Audience :: Developers',
    ],
    tests_require=file('requirements.txt').read().split('\n'),
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
            'scaffold-vim-plugin = scaffold_vim_plugin.create_plugin_scaffold:create_scaffold'
        ]
    }
)
