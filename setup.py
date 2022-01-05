import cx_Freeze
executables=[cx_Freeze.Executable('puzzel.py')]
cx_Freeze.setup(
    name='puzzel',
    options={'build_exe':{'packages':['pygame']}},
    executables=executables
)