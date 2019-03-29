import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="console_functions",
    version="0.0.8",
    author="Christian Blandford",
    author_email="christianblandford@me.com",
    description="Some functions for easily printing pretty text to a terminal shell in python.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/christianblandford/Python-Shell-Functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "termcolor >= 1.1.0",
        "pick >= 0.6.4"
    ],
)
