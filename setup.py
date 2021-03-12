from setuptools import setup

setup(
    name="GameOfDice",
    version="0.1",
    py_modules=["game"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        gameofdice=game:cli
    """,
)