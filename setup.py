import io
from setuptools import setup, find_packages

requirements = ["requests", "click"]

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

pkg = "ipgeocache"
setup(
    name=pkg,
    version="0.1.3",
    url="https://github.com/seanbreckenridge/ipgeocache",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description=("""A small cache layer for IP geolocation info"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=[pkg]),
    package_data={pkg: ["py.typed"]},
    install_requires=requirements,
    keywords="ip cache geolocate",
    entry_points={"console_scripts": ["ipgeocache = ipgeocache.__main__:main"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
