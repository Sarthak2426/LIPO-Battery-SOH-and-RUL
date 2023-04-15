from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this funtion will return the list of the requirements  
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
        



setup(
    
    name="LIPO batter life prediction",
    version="0.0.1",
    author="Sarthak",
    author_email="sarthak.jindal.21cse@bmu.edu.in",
    packages=find_packages(),
    include_requires=get_requirements('requirements.txt'),
    
)
