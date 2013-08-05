from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='example.dexterityforms',
      version=version,
      description="Examples of forms using plone.directives.form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://plone.org/products/dexterity/documentation/manual/schema-driven-forms',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['example'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.z3cform',
          'plone.directives.form',
      ],
      extras_require={
        'tests': ['collective.testcaselayer',]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )