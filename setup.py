from setuptools import setup, find_packages

# Read README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chandan-aiops",
    version="0.1.0",
    author="Chandan",
    author_email="your.email@example.com",
    description="Generate AI/ML Ops project structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chandan_aiops",
    
    packages=find_packages(),
    
    # Include template files
    package_data={
        'chandan_aiops': ['templates/**/*'],
    },
    include_package_data=True,
    
    # CLI command
    entry_points={
        'console_scripts': [
            'aiops-create=chandan_aiops.cli:create',
        ],
    },
    
    # Dependencies
    install_requires=[
        "click>=8.0.0",
    ],
    
    python_requires=">=3.7",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    keywords="mlops ai machine-learning template",
)