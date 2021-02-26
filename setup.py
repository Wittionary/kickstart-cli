from setuptools import setup

setup(
    name='kickstart_cli',
    version='0.1',
    py_modules=['kickstart_cli'],
    install_requires=[
        'Click','requests'
    ],
    entry_points='''
        [console_scripts]
        ks=kickstart_cli:cli
    ''',
)