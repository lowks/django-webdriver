import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='django-webdriver',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='Django app to run selenium webdriver tests.',
    long_description=README,
    url='https://github.com/optiflows/django-webdriver',
    author='Valentin Monte',
    author_email='valentin.monte@optiflows.com',
    install_requires=[
        'django>=1.4',
        'selenium>=2.30',
        'django-nose>=1.1',
    ],
    setup_requires=[
        'setuptools_git>=1.0',
    ]
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
