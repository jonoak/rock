from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rock",
    version="0.0.1",
    author="Jonathan Oakey",
    author_email="jonathandoakey@gmail.com",
    description="rock",
    package_data={'': ['small_rocks.txt']},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonoak/rock.git",
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    py_modules=['rock'],
      scripts=['rock.py'],
    python_requires=">=3.6",
    keywords='rock'
)