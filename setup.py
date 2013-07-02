import meme

from setuptools import setup, find_packages


setup(
    name='meme',
    version=meme.__version__,
    description="Use the command line to generate memes on memegenerator.co",
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Games/Entertainment",
    ],
    author="Katy LaVallee",
    author_email="katy@firelightweb.com",
    url="https://github.com/katylava/memepy",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'meme = meme.meme:cli',
        ],
    },
    install_requires=['pyquery', 'requests']
)
