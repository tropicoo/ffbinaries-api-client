from distutils.core import setup

setup(
    name='ffbinaries-api-client',
    packages=['ffbinaries'],
    version='0.0.1',
    license='MIT',
    description='ffbinaries api client',
    author='tropicoo',
    url='https://github.com/tropicoo/ffbinaries-api',
    download_url='https://github.com/tropicoo/ffbinaries-api-client/archive/0.0.1.tar.gz',
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
