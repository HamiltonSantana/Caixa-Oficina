import cx_Freeze
import sys
#import matplotlib
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Sr. Picolo\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Sr. Picolo\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

includes      = []
include_files = [r"C:\\Users\\Sr. Picolo\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tcl86t.dll", \
                 r"C:\\Users\\Sr. Picolo\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tk86t.dll"]

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("caixa.py", base=base)]

cx_Freeze.setup(
    name = "SGS",
    options = {"build_exe": {"includes":includes, "include_files": include_files}},
    version = "0.1",
    description = "Cadastro de clientes Oficina",
    executables = executables
    )