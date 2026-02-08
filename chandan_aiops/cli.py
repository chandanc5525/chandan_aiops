import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional

from src.visualize import show_dvc_pipeline

class AIOpsGenerator:
    """AIOps project generator class with DVC-ready pipeline support."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.package_dir = Path(__file__).parent
        self.template_dir = self.package_dir / "templates" / "aiops_project"

    def validate_template(self) -> bool:
        """Ensure essential template files exist."""
        if not self.template_dir.exists():
            print(f"ERROR: Template directory not found: {self.template_dir}")
            return False

        essential_files = [
            'src/__init__.py',
            'config.py',
            'main.py',
            'pyproject.toml',
            'README.md'
        ]

        missing_files = [f for f in essential_files if not (self.template_dir / f).exists()]
        if missing_files:
            print("ERROR: Missing essential template files:")
            for file in missing_files:
                print(f"  - {file}")
            return False

        return True

    def create_project(self, project_name: str, output_dir: Optional[Path] = None) -> bool:
        """Create a new AIOps project structure."""
        if not self._validate_project_name(project_name):
            return False

        project_path = output_dir / project_name if output_dir else Path.cwd() / project_name
        if project_path.exists():
            print(f"ERROR: Directory '{project_name}' already exists!")
            return False

        if not self.validate_template():
            print("Please check if template files are properly installed.")
            return False

        try:
            project_path.mkdir(parents=True)
            if self.verbose:
                print(f"Creating project '{project_name}' at {project_path}")

            self._copy_templates(project_path)
            self._display_success(project_path, project_name)
            return True
        except Exception as e:
            print(f"ERROR: Failed to create project: {e}")
            if project_path.exists():
                shutil.rmtree(project_path)
            return False

    def _validate_project_name(self, name: str) -> bool:
        if not name.strip():
            print("ERROR: Project name cannot be empty")
            return False

        invalid_chars = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']
        for char in invalid_chars:
            if char in name:
                print(f"ERROR: Project name contains invalid character: '{char}'")
                return False
        return True

    def _copy_templates(self, destination: Path):
        for item in self.template_dir.iterdir():
            dest_item = destination / item.name
            if item.is_dir():
                shutil.copytree(item, dest_item)
                if self.verbose:
                    print(f"  Created directory: {item.name}/")
            else:
                shutil.copy2(item, dest_item)
                if self.verbose:
                    print(f"  Created file: {item.name}")

    def _display_success(self, project_path: Path, project_name: str):
        print(f"\nSUCCESS: Project '{project_name}' created successfully!")
        print(f"Location: {project_path}\n")

        print("Project Structure:")
        print(f"{project_name}/")
        self._print_tree(project_path, prefix="  ")

        print("\nNext Steps:")
        print(f"  1. cd {project_name}")
        print("  2. python -m venv venv")
        print("  3. For Windows: venv\\Scripts\\activate")
        print("     For Mac/Linux: source venv/bin/activate")
        print("  4. pip install -e .")
        print("  5. Add your raw data to data/raw/")
        print("  6. Configure parameters in params.yaml")
        print("  7. Run your pipeline stages using DVC")
        print("     Example: dvc repro")
        print("  8. Visualize pipeline: chandan-aiops visualize\n")

    def _print_tree(self, path: Path, prefix: str = ""):
        items = sorted(path.iterdir())
        for i, item in enumerate(items):
            connector = "└── " if i == len(items) - 1 else "├── "
            if item.is_dir():
                print(f"{prefix}{connector}{item.name}/")
                next_prefix = prefix + ("    " if i == len(items) - 1 else "│   ")
                self._print_tree(item, next_prefix)
            else:
                print(f"{prefix}{connector}{item.name}")


def validate_command(directory: str = ".") -> bool:
    """Validate project structure."""
    project_path = Path(directory)

    required_dirs = ['data/raw', 'src', 'app', 'models', 'tests']
    required_files = ['src/data_ingestion.py', 'src/model_builder.py', 'config.py', 'main.py', 'pyproject.toml']

    print(f"Validating project structure: {project_path}\n")
    issues = []

    for dir_path in required_dirs:
        if (project_path / dir_path).exists():
            print(f"  ✓ {dir_path}/")
        else:
            print(f"  ✗ {dir_path}/")
            issues.append(f"Missing directory: {dir_path}")

    for file_path in required_files:
        if (project_path / file_path).exists():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path}")
            issues.append(f"Missing file: {file_path}")

    if issues:
        print(f"\nFound {len(issues)} issues:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("\nAll checks passed! Project structure is valid.\n")
        return True


def main():
    """Chandan AIOps CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Chandan AIOps - Create AI/ML project structures with DVC-ready pipelines",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  chandan-aiops create my-project          Create new project
  chandan-aiops create my-project -v       Verbose output
  chandan-aiops validate                   Validate current directory
  chandan-aiops validate ./project         Validate specific directory
  chandan-aiops version                    Show version
  chandan-aiops visualize                  Show DVC pipeline DAG
"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument("project_name", help="Name of the project to create")
    create_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    create_parser.add_argument("--output", "-o", help="Output directory (default: current directory)")

    validate_parser = subparsers.add_parser("validate", help="Validate project structure")
    validate_parser.add_argument("directory", nargs="?", default=".", help="Directory to validate")

    subparsers.add_parser("version", help="Show package version")
    subparsers.add_parser("visualize", help="Visualize DVC pipeline DAG")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "create":
        output_dir = Path(args.output) if args.output else None
        generator = AIOpsGenerator(verbose=args.verbose)
        success = generator.create_project(args.project_name, output_dir)
        sys.exit(0 if success else 1)

    elif args.command == "validate":
        success = validate_command(args.directory)
        sys.exit(0 if success else 1)

    elif args.command == "version":
        from chandan_aiops import __version__
        print(f"chandan-aiops version {__version__}")
        sys.exit(0)

    elif args.command == "visualize":
        show_dvc_pipeline()
        sys.exit(0)


if __name__ == "__main__":
    main()
