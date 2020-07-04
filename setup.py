import setuptools

setuptools.setup(
    name="simple-equation-solver",
    version="0.1.0",
    author="nilnil47",
    author_email="nilnil47@example.com",
    description="A small example package",
    long_description="aaa",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'sympy'
    ],
    python_requires='>=3.6'
)