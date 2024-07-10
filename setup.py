#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup, find_packages

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yolo',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/yourusername/your_project_name',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tinygrad @ git+https://github.com/tinygrad/tinygrad.git'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
