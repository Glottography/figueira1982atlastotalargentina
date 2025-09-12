from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_figueira1982atlastotalargentina',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_figueira1982atlastotalargentina'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'figueira1982atlastotalargentina=cldfbench_figueira1982atlastotalargentina:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
