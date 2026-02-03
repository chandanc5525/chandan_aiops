from setuptools import setup, find_packages
import os

# Read version from __init__.py
def get_version():
    """Read version from package"""
    version_file = os.path.join(os.path.dirname(__file__), "chandan_aiops", "__init__.py")
    with open(version_file, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "1.1.0"

# Read README for long description
def get_long_description():
    """Read README file"""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as fh:
            return fh.read()
    return "Create AI/ML project structures with one command"

setup(
    # Basic package information
    name="chandan-aiops",
    version=get_version(),
    author="Chandan",
    author_email="your.email@example.com",  # Update with your email
    
    # Description
    description="Create complete AI/ML project structures with one command",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    
    # Project URLs
    url="https://github.com/yourusername/chandan_aiops",  # Update with your repo
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/chandan_aiops/issues",
        "Documentation": "https://github.com/yourusername/chandan_aiops#readme",
        "Source Code": "https://github.com/yourusername/chandan_aiops",
    },
    
    # Package discovery
    packages=find_packages(),
    
    # Include template files
    package_data={
        'chandan_aiops': ['templates/**/*', 'templates/*'],
    },
    include_package_data=True,
    
    # CLI commands - MULTIPLE ENTRY POINTS FOR RELIABILITY
    entry_points={
        'console_scripts': [
            'aiops-create=chandan_aiops.cli:main',
            'chandan-aiops=chandan_aiops.cli:main',  # Alternative command
        ],
    },
    
    # Also include as scripts for maximum compatibility
    scripts=[],  # Can add .py files here if needed
    
    # Dependencies
    install_requires=[
        "click>=8.0.0",
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
        ],
    },
    
    # Python version requirements
    python_requires=">=3.7",
    
    # Package classification (helps PyPI search)
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    
    # Keywords for search
    keywords=[
        "mlops", 
        "aiops", 
        "machine-learning", 
        "ai", 
        "template", 
        "project-structure",
        "scaffold",
        "boilerplate",
    ],
    
    # License
    license="MIT",
    
    # Additional metadata
    platforms=["any"],
)

# Print build information (for debugging)
if __name__ == "__main__":
    print(f"Building chandan-aiops version {get_version()}")
    print(f"Long description length: {len(get_long_description())} chars")