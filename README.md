# End-to-End MLOps Pipeline: California Housing Price Prediction

An end-to-end Machine Learning Operations (MLOps) project demonstrating how to build, track, version, containerize, and deploy a machine learning application using modern MLOps tools.

The project uses the **California Housing Dataset** to develop a regression model for predicting median house values. It integrates experiment tracking, data version control, model serving, and containerization to establish a reproducible and maintainable machine learning workflow.

## Project Overview

Developing a machine learning model is only one part of an ML engineering workflow. In production environments, models must also be reproducible, their experiments must be tracked, datasets must be versioned, and predictions must be accessible through reliable deployment interfaces.

This project addresses these challenges by implementing an end-to-end MLOps workflow.

### Key Objectives

- Build a machine learning regression pipeline using the California Housing Dataset.
- Track machine learning experiments, parameters, metrics, and model artifacts using MLflow.
- Implement data and pipeline version control using DVC.
- Integrate DVC with DagsHub for remote data and experiment management.
- Develop a REST API for serving machine learning predictions using FastAPI.
- Containerize the application using Docker.
- Use Docker Compose to orchestrate the application environment.
- Establish a reproducible workflow for machine learning experimentation and deployment.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Model development and evaluation |
| Pandas & NumPy | Data processing and manipulation |
| MLflow | Experiment tracking and model management |
| DVC | Dataset and pipeline version control |
| DagsHub | Remote repository and experiment management |
| FastAPI | REST API for model inference |
| Docker | Application containerization |
| Docker Compose | Container orchestration |
| Jupyter Notebook | Exploratory data analysis and experimentation |
| Git & GitHub | Source code version control |

## Project Architecture

The project follows a modular workflow that separates model experimentation, data management, and model serving.

```text
                DATA SOURCE
                     |
                     v
          California Housing Dataset
                     |
                     v
          Data Processing & Preparation
                     |
                     v
             Model Development
                     |
                     v
             Model Evaluation
                     |
                     v
              MLflow Tracking
           (Parameters, Metrics,
             and Artifacts)
                     |
                     v
             Model Management
                     |
                     v
             FastAPI Application
                     |
                     v
             Docker Container
                     |
                     v
              Model Inference
              (REST API)
```

**Data and experiment management:**

- DVC tracks dataset versions and supports reproducibility.
- DagsHub provides remote storage and collaboration for the project.
- MLflow records experiment parameters, evaluation metrics, and model artifacts.

## Repository Structure

```text
Distributed-Computing-System/
│
├── .dvc/                    # DVC configuration and metadata
│
├── api/                     # FastAPI application and model serving
│
├── notebooks/               # Exploratory analysis and ML experiments
│
├── .dvcignore               # Files and directories ignored by DVC
├── .gitignore               # Files and directories ignored by Git
│
├── Dockerfile               # Docker image configuration
├── docker-compose.yml       # Application service orchestration
│
├── data.dvc                 # DVC metadata for tracked data
│
└── requirements.txt         # Python dependencies
```

## Getting Started

Follow these instructions to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/UBGidado/Distributed-Computing-System.git

cd Distributed-Computing-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure DVC and Remote Storage

Initialize DVC if necessary:

```bash
dvc init
```

Configure access to the remote DagsHub repository according to your DVC remote configuration.

Pull the tracked dataset:

```bash
dvc pull
```

*Note: DVC remote access credentials may be required to retrieve the dataset.*

### 5. Run the Application

Build and start the application using Docker Compose:

```bash
docker compose up --build
```

Stop the application:

```bash
docker compose down
```

## Experiment Tracking with MLflow

MLflow is integrated into the project to provide experiment tracking and management.

The experiment tracking workflow allows developers to:

- Record model hyperparameters.
- Track model evaluation metrics.
- Compare different experimental runs.
- Store model artifacts.
- Maintain a history of machine learning experiments.

This makes it easier to understand model performance and reproduce previous experiments.

## Data Version Control with DVC

DVC is used to manage datasets independently of Git's source code versioning.

Instead of committing large datasets directly to GitHub, DVC tracks dataset versions through lightweight metadata files.

The integration with DagsHub provides remote data management and facilitates reproducibility.

Common DVC commands:

```bash
# Check DVC status
dvc status

# Pull tracked data
dvc pull

# Track a dataset
dvc add data/

# Push data to remote storage
dvc push
```

## Model Serving with FastAPI

The `api/` directory contains the model-serving component.

FastAPI provides a RESTful interface through which clients can interact with the trained machine learning model and obtain housing price predictions.

The API separates model inference from the experimentation environment, making the model accessible to external applications.

## Containerization with Docker

Docker is used to package the application and its dependencies into a consistent execution environment.

The project includes:

- `Dockerfile`: Defines the application container environment.
- `docker-compose.yml`: Defines how the application services are configured and executed.

This approach reduces environment-related inconsistencies and makes the application easier to reproduce across different systems.

## Reproducibility

Reproducibility is a central principle of this project.

The combination of Git, DVC, MLflow, and Docker supports:

- Source code versioning.
- Dataset versioning.
- Experiment tracking.
- Model artifact management.
- Consistent application environments.

Together, these tools establish a foundation for a reproducible machine learning lifecycle.

## Future Improvements

Potential extensions to the project include:

- Automated CI/CD pipelines using GitHub Actions.
- Automated model retraining and evaluation.
- Model performance monitoring and data drift detection.
- Automated testing of API endpoints.
- Model registry and production model promotion.
- Cloud deployment and scalable inference infrastructure.

## Author

**Usman Babayo Gidado**

Machine Learning | AI Engineering | MLOps | Data Science

- GitHub: [@UBGidado](https://github.com/UBGidado)

## Acknowledgements

This project was developed as a practical implementation of distributed computing and modern MLOps engineering principles, demonstrating the integration of machine learning development, experiment tracking, data versioning, and containerized deployment.

---

**Project Status:** MLOps implementation / Continuous improvement.
