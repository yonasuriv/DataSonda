from setuptools import setup, find_packages

setup(
    name='sysdd',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Example dependency
        'pandas',  # Another example
    ],
    author='Your Name',
    description='A sample Python package for sysdd',
    url='https://github.com/yourusername/sysdd',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
