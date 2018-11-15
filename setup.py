from setuptools import setup

setup(name='schoolloop-python',
      version='1.0',
      description='The unofficial SchoolLoop connector for Python',
      url='http://github.com/hkamran80/schoolloop-python',
      author='H. Kamran',
      author_email='hkamran@unisontech.org',
      license='GPLv3+',
      packages=['sl'],
      install_requires=[
          'bs4', 'requests',
      ],
      zip_safe=False)
