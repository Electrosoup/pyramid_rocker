from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyramid_rocker',
      version=version,
      description="Allows Pyramid Resources to Be Updated from a Webbrowser",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Pyramid Python Chrome',
      author='Simon Oram',
      author_email='simon@electrosoup.co.uk',
      url='http://github.com/Electrosoup',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
