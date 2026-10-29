import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv(
    "GOOGLE_CLOUD_LOCATION",
    "europe-west1",
)

BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET", "retail")
BIGQUERY_RAW_TABLE = os.getenv(
    "BIGQUERY_RAW_TABLE",
    "online_retail_raw",
)
BIGQUERY_ANALYTICS_TABLE = os.getenv(
    "BIGQUERY_ANALYTICS_TABLE",
    "daily_sales_by_country",
)
BIGQUERY_LOCATION = os.getenv("BIGQUERY_LOCATION", "EU")

# ML_TARGET = os.getenv("ML_TARGET", "revenue")
# ML_TEST_DAYS = int(os.getenv("ML_TEST_DAYS", "28"))
# ML_RANDOM_STATE = int(os.getenv("ML_RANDOM_STATE", "42"))

DATA_DIR = ROOT_DIR / os.getenv("DATA_DIR", "data")
# ARTIFACT_DIR = ROOT_DIR / os.getenv("ARTIFACT_DIR", "artifacts")


if not PROJECT_ID:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT missing in .env"
    )