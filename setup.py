from setuptools import setup, find_packages

setup(
    name="lpfx",
    version="0.1.0",
    author="Eetu Mäkinen",
    description="Launchpad FX – interactive LED controller and FX engine",
    license="MIT",
    packages=find_packages(),
    install_requires=["mido", "numpy", "sounddevice", "psutil"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)