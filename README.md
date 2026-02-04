## chandan-aiops

Chandan-AIOps is a Python command-line tool that generates production-ready AI/ML project structures using industry-standard MLOps practices.

It enables data scientists and ML engineers to bootstrap scalable, reproducible machine learning projects with a single command—eliminating repetitive setup work and enforcing best practices from day one.

---

## Key Capabilities

1. One-command generation of complete AI/ML project scaffolding

2. Opinionated yet extensible project layout aligned with real-world MLOps workflows

- Built-in support for:

1. MLflow experiment tracking

2. DVC-based data and model versioning

3. FastAPI inference services

4. CI/CD via GitHub Actions

5. Project structure validation utilities

6. Designed for local development, experimentation, and production deployment

---

```
Installation Guide:

Step1: pip install chandan-aiops
Step2: python -m chandan_aiops.cli create <ProjectTitle>
       # Windows Command Prompt:
         doskey aiops-create=python -m chandan_aiops.cli $*
       # Windows PowerShell:
         function aiops-create { python -m chandan_aiops.cli @args }
       # Mac/Linux:
         alias aiops-create="python -m chandan_aiops.cli"
Step3: Designed Folder Structure

my-ai-project/
├── data/                  # Data management
│   ├── raw/               # Raw, immutable data
│   └── processed/         # Processed data
├── data_insights/         # EDA reports and analysis
├── models/                # Trained model storage
├── mlruns/                # MLflow experiment tracking
├── logs/                  # Application logs
├── research/              # Jupyter notebooks
├── src/                   # Source code (your ML pipeline)
│   ├── data_ingestion.py  # Data loading module
│   ├── data_preprocessing.py  # Data cleaning
│   ├── model_builder.py   # Model training
│   ├── model_evaluator.py # Model evaluation
│   ├── model_predictor.py # Prediction module
│   └── logger.py          # Logging configuration
├── app/                   # Web application (FastAPI)
│   ├── main.py           # FastAPI app
│   ├── schemas.py        # Pydantic models
│   ├── service.py        # Business logic
│   ├── templates/        # HTML templates
│   └── static/           # CSS/JS assets
├── tests/                 # Test files
├── config.py             # Configuration settings
├── main.py               # Main pipeline entry point
├── Dockerfile           # Container configuration
├── dvc.yaml             # Data version control
├── .dvcignore           # DVC ignore patterns
├── .github/             # CI/CD workflows
│   └── workflows/
│       └── ci.yml       # GitHub Actions pipeline
├── pyproject.toml       # Dependencies and metadata
└── README.md            # Project documentation

```
---

Note:

## **Validate Project Structure:**

- Validate current directory

python -m chandan_aiops.cli validate

- Validate specific project

python -m chandan_aiops.cli validate ./my-project

## **Version Package:**

python -m chandan_aiops.cli version

---

## **Package and Source Code:**

- PyPI Package: https://pypi.org/project/chandan-aiops/1.4.0/

- Source Code: https://github.com/chandanc5525/chandan_aiops

---

License

MIT License

---