from setuptools import find_packages,setup
from typing import List
E_Dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if E_Dot in requirements:
            requirements.remove(E_Dot)
    return requirements
setup(
    name = 'MLPROJECT',
    version='0.0.1',
    author='Hardik',
    author_email='hardikahuja.bt22cse@pec.edu.in',
    packages = find_packages(),
    install_packages = get_requirements("requirements.txt")
)

