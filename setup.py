# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()

with open("requirements.txt","r",encoding="utf-8-sig") as f:
    requirements = [i.strip() for i in f.readlines()]

setup(
    name="MultiEL",
    version="0.2",
    description="Multilingual Entity Linking model by BELA model",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong",
    author_email="wannaphong@yahoo.com",
    url="https://github.com/wannaphong/MultiEL",
    packages=["multiel", "bela"],
    # test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "bela": [
            "conf/*",
            "conf/*/*",
            "conf/*/*/*",
            "data/*",
            "tests/data/*",
        ]
    },
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    keywords=[
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Source": "https://github.com/wannaphong/MultiEL",
        "Bug Reports": "https://github.com/wannaphong/MultiEL/issues",
    },
)
