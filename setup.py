from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='kundalikuz',
    version='1.3.3',
    packages=['kundalikuz'],
    url='https://github.com/attikusfinch/kundalikuz',
    license='Apache License 2.0',
    author='attikus_finch',
    description='kundalik.com parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'bs4',
        'lxml'
    ],
)
