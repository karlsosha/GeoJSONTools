from setuptools import setup

setup(
    name='geojsontools',
    version='0.1.0',
    py_modules=['geojsontools'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'geojsontools = geojsontools:geojson',
        ]
    }
)