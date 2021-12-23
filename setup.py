"""The setuptools setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

# Define your dependencies here
requirements = []
setup_requirements = []

setup(
    author="MaisTODOS",
    author_email="devs@maistodos.com.br",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: Portuguese",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Lib de utilitários para o Django",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="alfred",
    name="alfred4django",
    packages=find_packages(include=["alfred", "alfred.*"]),
    setup_requires=setup_requirements,
    url="https://github.com/MaisTodos/Alfred4Django",
    version="0.0.1",
    zip_safe=False,
)
