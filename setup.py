from setuptools import setup

# Todo: Parse this from a proper readme file in the future
description="print-histogram"
long_description = """print-histogram

Pretty print numpy histograms to the console.

"""

setup(name='print-histogram',
    version='0.0.1',
    description=description,
    long_description=long_description,
    url='https://github.com/ast0815/print-histogram',
    author='Lukas Koch',
    author_email='lukas.koch@mailbox.org',
    license='MIT',
    py_modules=['print-histogram'],
    install_requires=[
        'numpy>=1.0.0',
        'six>=1.10.0',
    ],
    extras_require = {
    },
    python_requires='>=2.7',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=True)
