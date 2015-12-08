import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='pexpass',
    version='0.0.1',
    description='Allow automation in entering password at prompt for ssh and scp. Not a recommended substitute for ssh keys but sometimes necessary.',
    author=u'Neville Kadwa',
    author_email='neville  kadwa com',
    license='Apache-2.0',
    py_modules=['pexpass'],
    scripts=['bin/pexpass'],
    url='http://github.com/kadwanev/pexpass',
    license='BSD licence, see LICENCE.txt',
#    long_description=open('README.txt').read(),
#    zip_safe=False,
)
