from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='xiru.ws',
      version=version,
      description="Plone Webservices Client",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone webservices',
      author='Fabiano Weimar dos Santos',
      author_email='xiru@xiru.org',
      url='https://github.com/xiru/xiru-ws',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['xiru'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'suds',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
