# Socrata Provider

Airflow provider modules for interacting with Socrata Open Data API. This includes any necessary operators and hooks for utilizing Socrata in Airflow DAGs.

## Installation

To utilize the packages first build the wheel with the below command.

```bash
python setup.py bdist_wheel
```

Then install the .whl file created in the dist folder.

```bash
pip install dist/socrata_provider-1.0.0-py3-none-any.whl
```

The package is now ready for use in Airflow DAGs.
