from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='netbone',
    packages=find_packages(),
    version='0.2.2',
    author='Ali Yassin',
    license='MIT',
    author_email='aliyassin4@hotmail.com',
    url='https://gitlab.liris.cnrs.fr/coregraphie/netbone',
    keywords='backbone network',
    description='A python package for extracting network backbones from simple weighted networks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "Cython==0.29.32",
        "igraph==0.10.2",
        "jax",
        "jaxlib",
        "networkx==2.8.8",
        "numpy==1.23.3",
        "opt-einsum==3.3.0",
        "packaging==22.0",
        "pandas==1.5.2",
        "patsy==0.5.3",
        "python-dateutil==2.8.2",
        "pytz==2022.7",
        "scipy==1.9.3",
        "six==1.16.0",
        "statsmodels==0.13.5",
        "tabulate==0.8.9",
        "texttable==1.6.7",
        "python-louvain==0.16",
        "matplotlib==3.6.0",
        "seaborn==0.12.1"
        ],
)
