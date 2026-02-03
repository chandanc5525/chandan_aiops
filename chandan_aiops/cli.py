import os
import sys
import shutil
import click
from pathlib import Path

def create_project(project_name):
    """Create a new AIOps project structure"""
    package_dir = Path(__file__).parent.parent
    template_dir = package_dir / "templates" / "aiops_project"
    
    if not template_dir.exists():
        print("Error: Template directory not found!")
        return False
    
    project_path = Path.cwd() / project_name
    
    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists!")
        return False
    
    try:
        shutil.copytree(template_dir, project_path)
        
        # Create .gitkeep files in empty directories
        empty_dirs = [
            'data/raw',
            'data_insights',
            'models',
            'mlruns',
            'logs',
            'research'
        ]
        
        for dir_path in empty_dirs:
            full_path = project_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            gitkeep_file = full_path / ".gitkeep"
            gitkeep_file.touch()
        
        # Update project-specific files
        update_project_files(project_path, project_name)
        
        display_structure(project_path)
        print(f"Success: Created '{project_name}' successfully!")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def update_project_files(project_path, project_name):
    """Update project-specific files with project name"""
    # Update README.md
    readme_path = project_path / "README.md"
    if readme_path.exists():
        content = readme_path.read_text()
        content = content.replace("aiops_project", project_name)
        content = content.replace("AIOps Project", project_name)
        readme_path.write_text(content)
    
    # Update config.py
    config_path = project_path / "config.py"
    if config_path.exists():
        content = config_path.read_text()
        content = content.replace("aiops_project", project_name)
        config_path.write_text(content)
    
    # Update pyproject.toml
    pyproject_path = project_path / "pyproject.toml"
    if pyproject_path.exists():
        content = pyproject_path.read_text()
        content = content.replace("aiops-project", project_name.replace("_", "-"))
        pyproject_path.write_text(content)

def display_structure(project_path):
    """Display the created project structure"""
    print("\nProject Structure Created:")
    print(f"{project_path.name}/")
    
    def print_tree(path, prefix=""):
        items = sorted([item for item in path.iterdir() 
                       if not item.name.startswith('.') or item.name == '.github'])
        
        if not items:
            return
        
        pointers = ["|--"] * (len(items) - 1) + ["`--"]
        
        for pointer, item in zip(pointers, items):
            if item.is_dir():
                print(f"{prefix}{pointer} {item.name}/")
                print_tree(item, prefix + ("    " if pointer == "`--" else "|   "))
            else:
                print(f"{prefix}{pointer} {item.name}")
    
    print_tree(project_path)

def validate_project(directory):
    """Validate AIOps project structure"""
    project_path = Path(directory)
    
    required_files = [
        'src/data_ingestion.py',
        'src/data_preprocessing.py',
        'src/model_builder.py',
        'config.py',
        'main.py',
        'pyproject.toml',
        'README.md',
        'Dockerfile',
        'dvc.yaml'
    ]
    
    required_dirs = [
        'data/raw',
        'src',
        'app',
        'models',
        'tests',
        '.github/workflows'
    ]
    
    print("Validating AIOps project structure...")
    
    issues = []
    
    for dir_path in required_dirs:
        if (project_path / dir_path).exists():
            print(f"  PASS: {dir_path}/")
        else:
            print(f"  FAIL: {dir_path}/")
            issues.append(f"Missing directory: {dir_path}")
    
    for file_path in required_files:
        if (project_path / file_path).exists():
            print(f"  PASS: {file_path}")
        else:
            print(f"  FAIL: {file_path}")
            issues.append(f"Missing file: {file_path}")
    
    if issues:
        print(f"\nFound {len(issues)} issues:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("\nAll checks passed! Project structure is valid.")
        return True

@click.group()
def cli():
    """Chandan AIOps - Create standardized AI/ML project structures"""
    pass

@cli.command()
@click.argument('project_name')
def create(project_name):
    """Create a new AIOps project"""
    success = create_project(project_name)
    if success:
        print("\nNext Steps:")
        print(f"  cd {project_name}")
        print("  python -m venv venv")
        print("  # On Windows: venv\\Scripts\\activate")
        print("  # On Mac/Linux: source venv/bin/activate")
        print("  pip install -e .")
        print("  python main.py")
    else:
        sys.exit(1)

@cli.command()
@click.argument('directory', default='.')
def validate(directory):
    """Validate an existing AIOps project structure"""
    success = validate_project(directory)
    if not success:
        sys.exit(1)

@cli.command()
def version():
    """Show package version"""
    from chandan_aiops import __version__
    print(f"chandan-aiops version {__version__}")

def main():
    cli()

if __name__ == "__main__":
    main()