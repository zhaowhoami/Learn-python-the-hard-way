try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'wenum',
    'url': 'https://github.com/zhaowhoami/Learn-python-the-hard-way',
    'download_url': 'https://github.com/zhaowhoami/Learn-python-the-hard-way/archive/master.zip',
    'author_email': 'xauatxg@126.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
