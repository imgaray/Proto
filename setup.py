from setuptools import setup

setup(name='proto',
      version='0.1',
      description='a project solution builder',
      url='http://github.com/imgaray/Proto',
      author='Ignacio Garay',
      author_email='imgarayojeda@gmail.com',
      license='MIT',
      packages=['proto'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
