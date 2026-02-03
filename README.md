## Chandan-AIOps 🚀

One-Command AI/ML Project Structure Generator
Create complete, production-ready AI/ML project structures instantly. Perfect for data scientists and ML engineers who want to follow best practices from day one.

---

```
Installation Guide:

Step1: pip install chandan-aiops
Step2: python -m chandan_aiops.cli <ProjectTitle>
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

- PyPI Package: https://pypi.org/project/chandan-aiops/

- Source Code: https://github.com/chandanc5525/chandan_aiops

---