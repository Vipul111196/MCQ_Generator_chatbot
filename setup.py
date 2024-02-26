from setuptools import find_packages, setup
import os

def requirements():
    path = os.getcwd()
    requirement_path = os.path.join(path , 'requirements.txt')
    with open(requirement_path) as f:
        requirements = f.read().splitlines()
        requirements.remove(requirements[-1])
        
    return requirements

setup(
    name='mcq_generator',
    version= '0.0.1',
    author='Vipul Tyagi',
    author_email='vipultyagi11.vt@gmail.com',
    packages=find_packages(),
    install_requires = requirements()
)

