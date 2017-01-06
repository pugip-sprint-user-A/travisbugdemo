from setuptools import setup
import io
import os
#from opentaxforms.version import appversion

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README')

setup(
    name='travisdemo',
    version='0.1',
    url='http://github.com/jsaponara/travisdemo/',
    license="Affero GNU General Public License v3",
    author='John Saponara',
    tests_require=['pytest'],
    install_requires=[],
    #scripts = ['script/otf'],
    author_email='john@opentaxforms.org',
    description='demonstrates a possible bug in TravisCI',
    long_description=long_description,
    packages=['travisdemo'],
    package_dir={'travisdemo':
                 'travisdemo'},
    include_package_data=True,
    platforms='any',
    #test_suite='test.test_opentaxforms',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        ],
)
