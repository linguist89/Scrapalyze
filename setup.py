import setuptools

"""
with open("README.md", "r") as fh:
    long_description = fh.read()
"""

setuptools.setup(
    name="Scrapalyze", # Replace with your own username
    version="0.0.1",
    author="Stephan Smuts",
    author_email="smuts1989@gmail.com",
    description="A package that makes scraping webpages easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)