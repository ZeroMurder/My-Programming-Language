from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lpibydevcoder",
    version="0.0.8",
    packages=find_packages(where="."),  
    include_package_data=True,  
    author="DevCooder",
    author_email="zerowanlord@gmail.com",
    description="My simple and easy programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeroMurder/My-Programming-Language",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)




