""" Setup for api-server """
from setuptools import setup, find_namespace_packages

REQUIREMENTS = [
    'importlib-metadata==4.8',
    'jsonschema==3.2.0',
    'PyYaml==6.0',
    'aiohttp==3.7.4.post0'
]

setup(
    name='api-server',
    version='0.0.0.0',
    description='API Server',
    long_description='.',
    url='',
    author='JD',
    author_email='',
    python_requires='>=3.5',
    packages=find_namespace_packages(include=['package.*']),
    namespace_packages=['package'],
    include_package_data=True,
    install_requires=REQUIREMENTS,

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={"console_scripts": ["api-server = package.apiserver.__main__:main"]},
)
