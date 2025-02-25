from setuptools import setup, find_packages
import os
import subprocess
import sys
import warnings

# Importar versión y metadatos desde pysimplesoap
from pysimplesoap import __version__, __author__, __author_email__, __license__

# Convertir README.md a RST para la descripción larga (solo si es necesario)
long_desc = ""
if os.path.exists("README.md") and sys.platform == "linux2":
    try:
        cmd = ["pandoc", "--from=markdown", "--to=rst", "README.md"]
        long_desc = subprocess.check_output(cmd).decode("utf8")
        print("Long DESC", long_desc)
    except Exception as e:
        warnings.warn("Exception when converting the README format: %s" % e)

# Definir un solo paquete
setup(
    name="PySimpleSOAP",
    version=__version__,
    description="Python simple and lightweight SOAP Library",
    long_description=long_desc,
    author=__author__,
    author_email=__author_email__,
    url="http://code.google.com/p/pysimplesoap",
    packages=["pysimplesoap"],
    install_requires=["httplib2"],  # Añadimos dependencias explícitas
    license=__license__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
