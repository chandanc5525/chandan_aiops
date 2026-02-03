import os

PROJECT_STRUCTURE = [
    # package
    "chandan_aiops/__init__.py",
    "chandan_aiops/cli.py",

    # templates
    "templates/aiops_project/data/raw/.gitkeep",
    "templates/aiops_project/data_insights/.gitkeep",
    "templates/aiops_project/models/.gitkeep",
    "templates/aiops_project/mlruns/.gitkeep",
    "templates/aiops_project/logs/.gitkeep",
    "templates/aiops_project/research/.gitkeep",

    # src
    "templates/aiops_project/src/__init__.py",
    "templates/aiops_project/src/data_ingestion.py",
    "templates/aiops_project/src/data_preprocessing.py",
    "templates/aiops_project/src/model_builder.py",
    "templates/aiops_project/src/model_evaluator.py",
    "templates/aiops_project/src/model_predictor.py",
    "templates/aiops_project/src/logger.py",

    # app
    "templates/aiops_project/app/__init__.py",
    "templates/aiops_project/app/main.py",
    "templates/aiops_project/app/schemas.py",
    "templates/aiops_project/app/service.py",
    "templates/aiops_project/app/templates/index.html",
    "templates/aiops_project/app/static/style.css",

    # tests
    "templates/aiops_project/tests/test_pipeline.py",

    # config & root files
    "templates/aiops_project/config.py",
    "templates/aiops_project/main.py",
    "templates/aiops_project/Dockerfile",
    "templates/aiops_project/dvc.yaml",
    "templates/aiops_project/.dvcignore",
    "templates/aiops_project/pyproject.toml",
    "templates/aiops_project/README.md",

    # github actions
    "templates/aiops_project/.github/workflows/ci.yml",

    # root level files
    "setup.py",
    "README.md",
    "LICENSE",
    ".gitignore",
]

def create_structure():
    for path in PROJECT_STRUCTURE:
        directory = os.path.dirname(path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        if not os.path.exists(path):
            with open(path, "w") as f:
                pass

    print("Project template created successfully!")

if __name__ == "__main__":
    create_structure()
