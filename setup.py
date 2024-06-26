from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='rankchem',
    version='1.2.5',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'rdkit',
        'morfeus-ml',
        'pyvistaqt',
        'numpy',
        'py3Dmol',
        'streamlit',
        'stmol',
        'ipython_genutils'
    ],
    python_requires='>=3.8',
    author='Emma Kappeler, Ludovica Fracassi',
    author_email='emma.kappeler@epfl.ch,ludovica.fracassi@epfl.ch',
    description='RankChem project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fracaludo/RankChem',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    license='MIT',
)
