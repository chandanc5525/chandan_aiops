import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional


class AIOpsProjectGenerator:
    """
    Project Structure Design: 

    Responsibility:
    - Create project structure from templates
    - Guide users on next steps
    - Keep pipeline logic declarative (DVC-first)
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.package_root = Path(__file__).parent
        self.template_root = self.package_root / "templates" / "aiops_project"

    def create(self, project_name: str, output_dir: Optional[Path] = None) -> None:
        self._validate_project_name(project_name)
        self._validate_templates()

        target_base = output_dir if output_dir else Path.cwd()
        project_path = target_base / project_name

        if project_path.exists():
            raise FileExistsError(f"Directory already exists: {project_path}")

        project_path.mkdir(parents=True)
        self._copy_templates(project_path)
        self._print_success_guide(project_name, project_path)

    def _validate_project_name(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Project name cannot be empty")

        invalid_chars = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']
        for char in invalid_chars:
            if char in name:
                raise ValueError(f"Invalid character in project name: {char}")

    def _validate_templates(self) -> None:
        if not self.template_root.exists():
            raise FileNotFoundError(
                f"Template directory not found: {self.template_root}"
            )

        required = [
            "dvc.yaml",
            "params.yaml",
            "src",
            "data",
            "README.md",
            "pyproject.toml"
        ]

        missing = [
            item for item in required
            if not (self.template_root / item).exists()
        ]

        if missing:
            raise FileNotFoundError(
                f"Missing required template files: {', '.join(missing)}"
            )

    def _copy_templates(self, destination: Path) -> None:
        for item in self.template_root.iterdir():
            dest = destination / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
                if self.verbose:
                    print(f"Created directory: {item.name}")
            else:
                shutil.copy2(item, dest)
                if self.verbose:
                    print(f"Created file: {item.name}")

    def _print_success_guide(self, project_name: str, project_path: Path) -> None:
        print("\nProject created successfully")
        print("-" * 60)
        print(f"Project Name : {project_name}")
        print(f"Location     : {project_path.resolve()}")

        print("\nNext steps to get started")
        print("-" * 60)
        print(f"1. Navigate to your project")
        print(f"   cd {project_name}")

        print("\n2. Create and activate virtual environment")
        print("   python -m venv venv")
        print("   Windows : venv\\Scripts\\activate")
        print("   macOS/Linux : source venv/bin/activate")

        print("\n3. Install project in editable mode")
        print("   pip install -e .")

        print("\n4. Initialize DVC (only once)")
        print("   dvc init")

        print("\n5. Review DVC pipeline definition")
        print("   dvc.yaml        -> pipeline stages (single source of truth)")
        print("   params.yaml     -> pipeline parameters")

        print("\n6. Run the pipeline")
        print("   dvc repro")

        print("\n7. Visualize pipeline DAG")
        print("   dvc dag")

        print("\nImportant notes")
        print("-" * 60)
        print("- Modify pipeline logic only in dvc.yaml")
        print("- Source code lives inside src/")
        print("- Raw data goes into data/raw/")
        print("- Generated models and metrics are tracked by DVC")

        print("\nYou are now ready to build reproducible ML pipelines using chandan-aiops.")


def validate_project(directory: Path) -> None:
    required_dirs = [
        "data/raw",
        "src",
        "models",
        "tests"
    ]

    required_files = [
        "dvc.yaml",
        "params.yaml",
        "pyproject.toml"
    ]

    print(f"\nValidating project at: {directory.resolve()}")
    print("-" * 60)

    errors = False

    for d in required_dirs:
        if (directory / d).exists():
            print(f"OK   directory : {d}")
        else:
            print(f"FAIL directory : {d}")
            errors = True

    for f in required_files:
        if (directory / f).exists():
            print(f"OK   file      : {f}")
        else:
            print(f"FAIL file      : {f}")
            errors = True

    if errors:
        sys.exit(1)

    print("\nProject structure is valid")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="chandan-aiops",
        description=(
            "chandan-aiops is a DVC-first project generator for building "
            "reproducible, production-ready ML pipelines."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Common usage:

  chandan-aiops create my_project
  chandan-aiops create my_project --verbose
  chandan-aiops validate
  chandan-aiops validate path/to/project

After creation:
  cd my_project
  dvc repro
  dvc dag
"""
    )

    subparsers = parser.add_subparsers(dest="command")

    create_cmd = subparsers.add_parser(
        "create",
        help="Create a new AI/ML project"
    )
    create_cmd.add_argument("name", help="Project name")
    create_cmd.add_argument(
        "--output",
        help="Output directory (default: current directory)"
    )
    create_cmd.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    validate_cmd = subparsers.add_parser(
        "validate",
        help="Validate an existing project structure"
    )
    validate_cmd.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Project directory"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "create":
        generator = AIOpsProjectGenerator(verbose=args.verbose)
        generator.create(
            project_name=args.name,
            output_dir=Path(args.output) if args.output else None
        )

    elif args.command == "validate":
        validate_project(Path(args.directory))


if __name__ == "__main__":
    main()
