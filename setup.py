from setuptools import setup


setup(
    name='cldfbench_bowern_and_atkinson2012',
    py_modules=['cldfbench_bowern_and_atkinson2012'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bowern_and_atkinson2012=cldfbench_bowern_and_atkinson2012:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
