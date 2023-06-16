from setuptools import find_packages,setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace ("\n" , " ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
    name='ML_project',
    version='0.0.1',
    author='Aditya Soraganvi',
    author_email='adityasoraganvi32@gmail.com',
    packages=find_packages(),
    install_packages=get_requirements('requirements.txt')
)