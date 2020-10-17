"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(

    name='Metodos',
    version='1.0.0',
    description='Paquete con metodos Tarea 3',
    author='Carlos_Joseph_Adrian_Emmanuel', 
    packages=['Metodos'],
    python_requires='>=3',
    install_requires=['tabulate', 'playsound', 'opencv-constrib-python', 'pillow', 'argparse' ],
    entry_points={
        'console_scripts': [
           'Tarea3=Tarea3:Main',
        ],
     },

)
