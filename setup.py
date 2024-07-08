from setuptools import setup, find_packages

setup(
    name='fastpbkdf2',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'fastpbkdf2': ['_fastpbkdf2.pyd'],
    },
    install_requires=[],
    author='Daniel Calvo',
    author_email='daniel.calvo@orain.io',
    description='fastpbkdf2 Windows',
    url='https://https://github.com/Orain-Technologies/fastpbkdf2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
