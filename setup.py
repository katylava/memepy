import meme

from setuptools import setup, find_packages


setup(
    name='meme',
    version=meme.__version__,
    description="Use the command line to generate memes on memegenerator.co",
    long_description=open('README.rst').read(),
    author="Katy LaVallee",
    author_email="katy@firelightweb.com",
    url="https://github.com/katylava/memepy",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'meme = meme.meme:cli',
        ],
    },
    install_requires=['pyquery', 'requests']
)
