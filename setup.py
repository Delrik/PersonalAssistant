from setuptools import setup, find_packages

setup(
    name="personalassistant",
    version="0.1.0",
    author="Project group 12",
    author_email="",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "personalassistant=personalassistant.main:main",
        ],
    },
    install_requires=[
        "prompt-toolkit==3.0.43",
        "rich==13.7.0",
    ],
    python_requires=">=3.6",
)
