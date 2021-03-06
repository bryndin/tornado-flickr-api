from setuptools import setup
import re

VERSION_FILE = "tornado_flickrapi/_version.py"
try:
    vers_content = open(VERSION_FILE, "r").read()
    version_str = re.search(r'__version__ = "(.+?)"', vers_content).group(1)
except:
    raise RuntimeError("Could not read version file.")

setup(
    name="tornado-flickrapi",
    version=version_str,
    description="Async Python wrapper for the Flickr API based on Tornado framework",
    author="Dmitriy Bryndin",
    author_email="bryndin@gmail.com",
    url="https://github.com/bryndin/tornado_flickrapi",
    packages=["tornado_flickrapi"],
    install_requires=[
        "oauth",
        "tornado",
    ],
    license="BSD License",
)
