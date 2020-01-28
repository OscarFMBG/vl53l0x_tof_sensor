from setuptools import setup, find_packages
setup(
    name="vl53l0x",
    version="1.0",
    packages=find_packages(),

    # Project uses markdown, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        "docutils>=0.3",
        "smbus",
    ],

    package_data={
        # If any package contains *.txt or *.md files, include them:
        "": ["*.txt", "*.md"],
    },

    # metadata to display on PyPI
    author="Oscar Butler-Aldridge",
    author_email="oscarb@protonmail.com",
    keywords="hello world example examples",
    url="https://github.com/OscarFMBG/vl53l0x_tof_sensor",   # project home page, if any
    project_urls={
        "Source Code": "https://github.com/OscarFMBG/vl53l0x_tof_sensor",
    },
)
