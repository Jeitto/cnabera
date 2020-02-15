from setuptools import find_packages, setup

setup(
    name='cnabera',
    url='https://github.com/Jeitto/cnabera',
    author='Jeitto',
    author_email='engenharia@jeitto.com.br',
    packages=find_packages(),
    install_requires=open("requirements/prod.txt").read().splitlines(),
    version='0.0.1',
    description='Biblioteca para gerar arquivos CNAB, obedecendo ao padrão estabelecido pela FEBRABAN',
    long_description=open('README.md').read(),
    tests_require=open("requirements/dev.txt").read().splitlines()[2:],
)
