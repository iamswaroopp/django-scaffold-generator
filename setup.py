import os
from pathlib import Path

from setuptools import setup

version = '0.0.1a3'

description = Path(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                'README.md')).read_text(encoding='utf-8').strip()

setup(
    name='django-scaffold-generator',
    packages=['scaffold_generator'],
    version=version,
    license='mit',
    license_files=('LICENSE.txt',),
    description='Ruby on Rails like Scaffolding Provider for Django',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Swaroop P',
    author_email='iamswaroopp@gmail.com',
    url='https://github.com/iamswaroopp/django-scaffold-generator',
    download_url='https://github.com/iamswaroopp/django-scaffold-generator/archive/' + version + '.zip',
    keywords=(
        'django',
        'developement',
        'scaffolding',
        'startapp',
        'python',
    ),
    install_requires=('django',),
    python_requires='>=3.6',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ),
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/iamswaroopp/django-scaffold-generator/issues',
    },
)
