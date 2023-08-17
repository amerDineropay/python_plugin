from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="dineropay",
    version="0.0.1",
    description="Providing Dinero Pay services",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amerDineropay/python_plugin/tree/main",
    author="Dineropay",
    author_email="support@dineropay.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires=">=3.10",
)
