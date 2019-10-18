from distutils.core import setup

from ffbinaries import __version__ as version

setup(
    name='ffbinaries-api-client',
    packages=['ffbinaries'],
    version=version,
    license='MIT',
    description='ffbinaries api client',
    author='tropicoo',
    url='https://github.com/tropicoo/ffbinaries-api',
    keywords=['ffbinaries', 'ffmpeg', 'api'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
