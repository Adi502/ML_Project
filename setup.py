from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
'''
    The function `get_requirements` reads a file and returns a list of requirements by removing any new
    line characters and a specific string from the list.
    
    :param file_path: The `file_path` parameter is the path to the file that contains the list of
    requirements. In this case, it is set to `'requirements.txt'`, which means that the function will
    read the requirements from a file named `requirements.txt`
    :type file_path: str
    :return: a list of requirements.
'''
def get_requirements(file_path:str)->List[str]:
    
    #this function will return the list of requirements
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='ML_project',
version='0.0.1',
author='Aditya Soraganvi',
author_email='adityasoraganvi32@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)