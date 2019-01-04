from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pyreader',
    version='1.0',
    author='Lucian Cooper',
    url='https://github.com/luciancooper/pyreader',
    description='Python File Parser',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python parser',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['pyreader'],
    entry_points={
        'console_scripts': [
            'pyreader = pyreader.__main__:main',
        ]
    },
)
