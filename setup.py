import os
from setuptools import setup, find_packages
import sys


name='KPConv'
version='0.0.0'

exts = [
   'KPConv_radius_neighbors @ file://localhost/' + os.path.join(os.path.abspath(os.path.dirname(__file__)), "cpp_wrappers", "cpp_neighbors").replace('\\', '/'),
   'KPConv_grid_subsampling @ file://localhost/' + os.path.join(os.path.abspath(os.path.dirname(__file__)), "cpp_wrappers", "cpp_subsampling").replace('\\', '/')
]

setup(
    name=name,
    packages=find_packages(),
    version=version,
    namespace_packages=['KPConv'],
    install_requires=[
        'numpy',
        'sklearn',
        'pyaml',
        'torch>=1.10.2',
        'torchvision>=0.11.3',
        'torchaudio>=0.10.2'
    ] + exts,
    python_requires='>=3.9'
)
