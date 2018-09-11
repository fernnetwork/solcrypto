from setuptools import setup, find_packages

setup(name='solcrypto',
    version='0.0.1',
    url='https://github.com/jchen86/solcrypto',
    packages=['pysolcrypto'],
    install_requires=[
      'py_ecc',
      'pysha3',
      'bitcoin',
      'future'
    ]
)
