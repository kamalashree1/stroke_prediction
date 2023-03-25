from setuptools import find_packages,setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''this function returns a list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n','')for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements



setup(
    name='stroke_prediction',
    version='0.0.1',
    author='Kamalashree',
    author_email='kamalashree.sudhakar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)