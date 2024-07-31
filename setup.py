"""Script for pygrin module."""
import re
import os
import os.path
import platform
import urllib.request
from setuptools import setup, find_packages
from zipfile import ZipFile

project = 'vtspython'

system = platform.system()

def download_and_extract(url, extract_to='vtspython/dlls'):
    os.makedirs(extract_to, exist_ok=True)
    zip_path, _ = urllib.request.urlretrieve(url)
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def get_init_property(prop):
    """Return property from __init__.py."""
    here = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.join(here, project, '__init__.py')
    regex = r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop)
    with open(file_name, 'r', encoding='utf-8') as file:
        result = re.search(regex, file.read())
    return result.group(1)


def get_contents(filename):
    """Return contents of filename relative to the location of this file."""
    here = os.path.abspath(os.path.dirname(__file__))
    fn = os.path.join(here, filename)
    with open(fn, 'r', encoding='utf-8') as f:
        contents = f.read()
    return contents


if system == 'Linux':
    dll_url = 'https://github.com/VirtualPhotonics/Vts.Scripting.Python/releases/download/Version_11.0/VTS_Scripting_v11.0.0_Linux_x64.zip'
elif system == 'Darwin':  # macOS
    dll_url = 'https://github.com/VirtualPhotonics/Vts.Scripting.Python/releases/download/Version_11.0/VTS_Scripting_v11.0.0_Mac_x64.zip'
else:
    raise RuntimeError(f"Unsupported platform: {system}")


download_and_extract(dll_url)


setup(
    name=project,
    long_description=get_contents('README.rst'),
    long_description_content_type='text/x-rst',
    version=get_init_property('__version__'),
    author=get_init_property('__author__'),
    author_email=get_init_property('__email__'),
    license=get_init_property('__license__'),
    url=get_init_property('__url__')
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pythonnet',
    ],
    package_data={
        'vtspython': ['dlls/*.dll'],
    },
    entry_points={
        'console_scripts': [
            'vts = vtspython.vts:main',
        ],
    },
)
