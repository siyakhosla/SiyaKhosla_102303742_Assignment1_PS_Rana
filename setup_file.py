from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Topsis-siyakhosla-102303742",
    version="0.2",
    author="Siya Khosla",
    description="TOPSIS implementation using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    license="MIT",
)
