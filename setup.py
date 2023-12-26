from setuptools import setup, find_packages

setup(
    name='newgrounds_dl',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'newgrounds_dl=newgrounds_dl:main',
        ],
    },
    author='Connor',
    description='A Python library for downloading music from Newgrounds.',
)
