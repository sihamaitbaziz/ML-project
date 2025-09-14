from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'   # <-- fixed here

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Siham',
    author_email='s_aitbaziz@estin.dz',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
