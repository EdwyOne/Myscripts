#!/usr/bin/python
import os
import re
create_venv = 'python -m venv newvenv'
activate_venv = '.\venv\Scrits\activate'
install_django = 'pip install django'
startproject = 'django-admin startproject project1'
freeze = 'pip freeze'


def main():
    os.system(create_venv)
    os.system(activate_venv)
    os.system(install_django)
    os.system(startproject)
    os.system(freeze)


if __name__ == '__main__':
    main()
