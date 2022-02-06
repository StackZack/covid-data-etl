from setuptools import setup
import pathlib
import os

parent_dir = pathlib.Path(__file__).parent
README = os.path.join(parent_dir, "README.md")

setup(
    name="socrata-provider",
    version="1.0.0",
    description="""Airflow provider modules for interacting
        with Socrata Open Data API""",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["hooks", "operators"],
    install_requires=["apache-airflow", "pandas"]
)
