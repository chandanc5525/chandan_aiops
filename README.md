# chandan-aiops

[![PyPI version](https://img.shields.io/pypi/v/chandan-aiops)](https://pypi.org/project/chandan-aiops/)
[![Python Versions](https://img.shields.io/pypi/pyversions/chandan-aiops)](https://pypi.org/project/chandan-aiops/)
[![License](https://img.shields.io/pypi/l/chandan-aiops)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/chandanc5525/chandan_aiops/ci.yml)](https://github.com/chandanc5525/chandan_aiops/actions)
[![Downloads](https://img.shields.io/pypi/dm/chandan-aiops)](https://pypi.org/project/chandan-aiops/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000)](https://black.readthedocs.io/en/stable/)

---

## Overview

**chandan-aiops** is an enterprise-ready MLOps automation platform that standardizes and accelerates the entire machine learning lifecycle. It provides a CLI-driven framework for generating production-grade AI project templates with built-in data versioning, experiment tracking, and pipeline orchestration.

This tool transforms scattered ML code into organized, reproducible, and deployable projects by enforcing industry best practices from day one. It's designed for teams that value consistency, collaboration, and production readiness in their machine learning workflows.

chandan-aiops is designed for:
- Machine Learning Engineers
- Data Scientists
- MLOps & Platform Engineers
- Technical team leads managing ML projects
- Educators teaching production ML workflows

---

## Why Choose chandan-aiops

Most ML projects struggle not with model building, but with operational challenges:
- Inconsistent project structures across teams
- Missing or ad-hoc data versioning
- Hard-coded configurations scattered throughout code
- No standardized pipeline management
- Difficult handoff between experimentation and production

chandan-aiops solves these challenges by providing a **unified, opinionated framework** that:
- Treats data, models, and experiments as versioned artifacts
- Separates configuration from code logic
- Provides clear pipeline visualization and dependencies
- Standardizes project layouts across teams and organizations

Unlike piecemeal solutions, chandan-aiops delivers a **complete MLOps foundation** that scales from individual data scientists to enterprise teams.

---

## Key Features

### **Instant Project Scaffolding**
Generate complete, production-ready ML projects with a single CLI command. All necessary components—data pipelines, model training, evaluation, and serving—are pre-structured and connected.

### **Data-Centric Workflow Management**
Built-in DVC integration ensures every dataset, intermediate result, and trained model is automatically versioned and reproducible. Track lineage from raw data to final predictions.

### **Centralized Configuration System**
All project parameters live in structured YAML files, enabling easy experimentation, parameter sweeping, and configuration management across different environments.

### **Pipeline Visualization & Transparency**
Automatic dependency graph generation shows exactly how data flows through preprocessing, training, and evaluation stages—no hidden connections or "magic" dependencies.

### **Production-Ready Architecture**
Every generated project includes Docker configurations, CI/CD workflows, monitoring setups, and API serving templates, ensuring smooth transition from experimentation to deployment.

### **Modular & Extensible Design**
Clean separation between data processing, model training, and evaluation components allows easy swapping of algorithms, data sources, or evaluation metrics.

---

## Installation

Install from PyPI:

```bash
pip install chandan-aiops

---

```
Step1 : Verify installation:

chandan-aiops --version

Step2 : View Help Function

chandan-aiops --help

Step3 : Create a new production-ready project: 

chandan-aiops create <Project_Name>

Step4 : Project Structure Design 

<Project_Name>/
├── data/                  # Version-controlled datasets
│   ├── raw/               # Immutable source data
│   └── processed/         # Cleaned, transformed data
├── data_insights/         # EDA reports and visualizations
├── models/                # Versioned model artifacts
├── mlruns/                # MLflow experiment tracking
├── logs/                  # Structured application logs
├── research/              # Exploratory notebooks
├── src/                   # Production ML pipeline code
│   ├── data_ingestion.py  # Data loading and validation
│   ├── data_preprocessing.py  # Feature engineering
│   ├── model_builder.py   # Training and validation
│   ├── model_evaluator.py # Performance metrics
│   ├── model_predictor.py # Inference and serving
│   └── logger.py          # Centralized logging
├── app/                   # Deployment and serving
│   ├── main.py           # FastAPI application
│   ├── schemas.py        # API request/response models
│   ├── service.py        # Business logic layer
│   ├── templates/        # Web interface (optional)
│   └── static/           # Frontend assets
├── tests/                 # Comprehensive test suite
├── params.yaml           # Centralized parameters
├── dvc.yaml              # Data pipeline definitions
├── .dvcignore            # DVC ignore patterns
├── Dockerfile           # Container configuration
├── .github/             # CI/CD automation
│   └── workflows/
│       └── ci.yml       # Testing and deployment
├── pyproject.toml       # Python dependencies
├── main.py              # Pipeline entry point
└── README.md            # Project documentation


Step5 : Pipeline Visualization  {Typical Workflow}

- Initialize DVC:

dvc init

- Run the full pipeline:

dvc repro

- Track data and artifacts:

dvc add data/raw

git add data/raw.dvc dvc.lock

git commit -m "Track raw data"


- View pipeline structure:

dvc dag

```

---

## CLI Commands:

chandan-aiops create <project_name>     Create a new AI/ML project

chandan-aiops validate [directory]     Validate project structure

chandan-aiops version                  Show installed version

chandan-aiops --help                   Display full CLI documentation

---

```
| Feature              | Kedro    | chandan-aiops |
| -------------------- | -------- | ------------- |
| Pipeline abstraction | Yes      | Yes (via DVC) |
| DAG visualization    | Yes      | Yes           |
| Parameter files      | Yes      | Yes           |
| Data versioning      | Limited  | Native (DVC)  |
| Model versioning     | External | Native        |
| MLOps focus          | Partial  | First-class   |
| CLI scaffolding      | Yes      | Yes           |
```
---

Author

Chandan Chaudhari

PyPI Package: https://pypi.org/project/chandan-aiops/1.5.0/

Source Code: https://github.com/chandanc5525/chandan_aiops