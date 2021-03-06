import os

if os.name == 'nt':
    IS_WIN = True
else:
    IS_WIN = False


if IS_WIN:
    VIRTUALENV_CMD = "env\\Scripts\\activate"
    VIRTUALENV_INSTALL_MSG = """\
Note that virtualenv must work with Python 3!

You could do:
py -3 -m pip install virtualenv
"""
else:
    VIRTUALENV_CMD = "source env/bin/activate"
    VIRTUALENV_INSTALL_MSG = """\
For example on Ubuntu you could do
    > [sudo] apt install virtualenv
Or use Pip:
    > [sudo] pip install virtualenv
"""
