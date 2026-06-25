from setuptools import setup

setup(
    name="sulfor-code",
    version="1.0.0",
    description="Sulfor Code — intelligent terminal AI assistant by @lavateam_IR",
    py_modules=["sulfor"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            # `sulfor run` works because main() handles the 'run' arg
            "sulfor=sulfor:main",
        ],
    },
)
