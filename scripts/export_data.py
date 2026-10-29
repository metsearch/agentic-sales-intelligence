import logging

from google.cloud import bigquery

from sales_intelligence.config import (
    PROJECT_ID,
    BIGQUERY_DATASET,
    BIGQUERY_ANALYTICS_TABLE,
    BIGQUERY_LOCATION,
    DATA_DIR,
)

logger = logging.getLogger(__name__)

OUTPUT_PATH = DATA_DIR / "daily_sales_by_country.csv"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    client = bigquery.Client(project=PROJECT_ID)

    table_id = (
        f"{PROJECT_ID}.{BIGQUERY_DATASET}."
        f"{BIGQUERY_ANALYTICS_TABLE}"
    )

    query = f"""
        SELECT
            sales_date,
            country,
            revenue,
            units_sold,
            line_count,
            invoice_count
        FROM `{table_id}`
        ORDER BY country, sales_date
    """

    logger.info("Exporting %s", table_id)

    df = client.query(
        query,
        location=BIGQUERY_LOCATION,
    ).to_dataframe()

    if df.empty:
        raise ValueError("The BigQuery analytical table is empty.")

    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    logger.info("Exportation complete : %s lines", len(df))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()