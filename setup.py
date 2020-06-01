from setuptools import find_packages, setup

setup(
    name='chatapp',
    version='1.0',
    author='Barry Molina',
    author_email='bazzaboy@gmail.com',
    packages=['chatapp'],
    include_package_data=True,
    install_requires=['tornado'],
    entry_points={
        'console_scripts': [
            'serve_app = chatapp.chat:main',
        ]
    })
