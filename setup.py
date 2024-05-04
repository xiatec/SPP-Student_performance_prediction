from setuptools import find_packages, setup


HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    :param file_path:
    :return: the requirements.txt list
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Phil',
    author_email='philstian@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)