import os
from pathlib import Path

from setuptools import setup
from setuptools import setup, find_packages

version = '0.0.0'

description = Path(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                'README.md')).read_text(encoding='utf-8').strip()

setup(
    name='django-scaffold-generator',
    packages=find_packages('.', include=['scaffold_generator','scaffold_generator.*']),
    package_data={'scaffold_generator': ['templates/scaffold_generator/*.template','templates/scaffold_generator/components/*.template', 'templates/scaffold_generator/api/*.template']},

    version=version,
    license='mit',
    license_files=['LICENSE.txt',],
    description='Ruby on Rails like Scaffolding Provider for Django',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Swaroop P',
    author_email='iamswaroopp@gmail.com',
    url='https://github.com/iamswaroopp/django-scaffold-generator',
    download_url='https://github.com/iamswaroopp/django-scaffold-generator/archive/' + version + '.zip',
    keywords=[
        'django',
        'developement',
        'scaffold_generator',
        'startapp',
        'rapid','rad','rapid application development'
        'python',
    ],
    install_requires=['django',],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/iamswaroopp/django-scaffold-generator/issues',
    },
    include_package_data=True,
)
