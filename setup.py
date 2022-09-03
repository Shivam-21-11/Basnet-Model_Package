from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="BASNET-MODEL",
    version="0.0.1",
    description="BASNET model created using tensorflow.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/FooDemo",
    author="Shivam Singh",
    author_email="Shivamsingh2111@gmail.com",
    keywords="Machine Learning",
    license="MIT",
    packages=["BASNET"],
    install_requires=['tensorflow','numpy','keras'],
    include_package_data=True,
)