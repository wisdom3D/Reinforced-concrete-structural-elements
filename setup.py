from cx_Freeze import setup, Executable
setup(
    name="AneeLumiere",
    version="2021",
    description="calcul de batiments en béton armé",
    executables=[Executable("annee_lumiere.py")]

)

