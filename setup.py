## This setup.py will be responsible in creating my machine learning application as a package, 
## so that we can install package in my projects or use it. And even deploy pypy and from that anyone
## can use this application and use it

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(     ## This can be like a metadata information about the entire project
    name= 'ML_Projects',
    version= '0.0.1',
    author= 'Aaryan',
    author_email= 'aaryangupta13@gmail.com',
    packages= find_packages(), # Whenever find_packages() is running, it will go and see to each folder if it contains __init__.py
    install_requires= get_requirements('requirements.txt')
)