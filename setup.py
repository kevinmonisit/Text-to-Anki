import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="TextToAnki",
    version="1.0.0",
    description="Add questions to Anki en masse",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinmonisit/Text-to-Anki",
    author="Kevin M",
    # author_email="info@realpython.com",
    license="MIT",
    # classifiers=[
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    # ],
    packages=["text2anki"],
    include_package_data=True,
    # install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "text2anki=text2anki.__main__:main",
        ]
    },
)