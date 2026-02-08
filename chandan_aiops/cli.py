import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional


class AIOpsGenerator:
    """AIOps project generator with DVC-ready pipelines."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.package_dir = Path(__file__).parent
        self.template_dir = self.package_dir / "templates" / "aiops_project"

    def validate_template(self) -> bool:
        if not self.template_dir.exists():
            print(f"ERROR: Template directory not found: {self.template_dir}")
            return False

        essential_files = [
            "src/__init__.py",
            "main.py",
            "pyproject.toml",
            "README.md",
            "params.yaml",
        ]

        missing = [
            f for f in essential_files
            if not (self.template_dir / f).exists()
        ]

        if missing:
            print("ERROR: Missing essential template files:")
            for f in missing:
                print(f"  - {f}")
            return False

        return True

    def create_project(self, project_name: str, output_dir: Optional[Path] = None) -> bool:
        if not project_name.strip():
            print("ERROR: Project name cannot be empty")
            return False

        project_path = output_dir / project_name if output_dir else Path.cwd() / project_name

        if project_path.exists():
            print(f"ERROR: Directory '{project_name}' already exists")
            return False

        if not self.validate_template():
            return False

        try:
            project_path.mkdir(parents=True)
            self._copy_templates(project_path)
            self._display_success(project_path, project_name)
            return True
        except Exception as e:
            shutil.rmtree(project_path, ignore_errors=True)
            print(f"ERROR: {e}")
            return False

    def _copy_templates(self, destination: Path):
        for item in self.template_dir.iterdir():
            target = destination / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)

    def _display_success(self, project_path: Path, project_name: str):
        print(f"\nSUCCESS: Project '{project_name}' created")
        print(f"Location: {project_path}\n")

        print("Next steps:")
        print(f"  cd {project_name}")
        print("  python -m venv venv")
        print("  source venv/bin/activate  (Windows: venv\\Scripts\\activate)")
        print("  pip install -e .")
        print("  dvc repro")
        print("  chandan-aiops visualize\n")


def validate_command(directory: str = ".") -> bool:
    base = Path(directory)
    required = [
        "src",
        "data/raw",
        "models",
        "params.yaml",
        "dvc.yaml",
    ]

    errors = False
    for path in required:
        if not (base / path).exists():
            print(f"Missing: {path}")
            errors = True

    if errors:
        return False

    print("Project structure is valid")
    return True


def visualize_pipeline():
    try:
        from subprocess import run
        run(["dvc", "dag"], check=True)
    except Exception:
        print("ERROR: DVC not initialized or dvc.yaml not found")


def main():
    parser = argparse.ArgumentParser(
        description="Chandan AIOps – MLOps project generator with DVC pipelines"
    )

    sub = parser.add_subparsers(dest="command")

    create = sub.add_parser("create")
    create.add_argument("name")
    create.add_argument("-o", "--output")
    create.add_argument("-v", "--verbose", action="store_true")

    validate = sub.add_parser("validate")
    validate.add_argument("directory", nargs="?", default=".")

    sub.add_parser("version")
    sub.add_parser("visualize")

    args = parser.parse_args()

    if args.command == "create":
        gen = AIOpsGenerator(verbose=args.verbose)
        out = Path(args.output) if args.output else None
        sys.exit(0 if gen.create_project(args.name, out) else 1)

    if args.command == "validate":
        sys.exit(0 if validate_command(args.directory) else 1)

    if args.command == "version":
        from chandan_aiops import __version__
        print(__version__)
        return

    if args.command == "visualize":
        visualize_pipeline()
        return

    parser.print_help()


# REQUIRED FOR PYPI / WINDOWS / CONSOLE SCRIPTS
def app():
    main()


if __name__ == "__main__":
    main()
