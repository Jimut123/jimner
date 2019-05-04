import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jimner",
    version="1.1",
    author="Jimut Bahan Pal",
    author_email="jimutbahanpal@yahoo.com",
    description="A banner generating library for UNIX, LINUX, MAC-OS and WINDOWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jimut123/jimner",
    install_requires=['json'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
