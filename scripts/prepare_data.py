
from pathlib import Path
import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT_DIR / "data" / "Online Retail.xlsx"
OUTPUT_PATH = ROOT_DIR / "data" / "online_retail.csv"


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Fichier source introuvable : {INPUT_PATH}"
        )

    logger.info("Reading Excel file...")
    df = pd.read_excel(
        INPUT_PATH,
        engine="openpyxl",
    )

    logger.info("Dimensions : %s lignes, %s colonnes", *df.shape)
    logger.info("Colonnes : %s", list(df.columns))

    # IDs should be strings: some bille id start by the letter C.
    df["InvoiceNo"] = df["InvoiceNo"].astype("string")
    df["StockCode"] = df["StockCode"].astype("string")
    df["CustomerID"] = df["CustomerID"].astype("Int64").astype("string")

    # Preserve date format
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    logger.info("CSV writing...")
    df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8",
        date_format="%Y-%m-%d %H:%M:%S",
    )

    logger.info("CSV created : %s", OUTPUT_PATH)
    logger.info("Size : %.2f Mo", OUTPUT_PATH.stat().st_size / 1_000_000)


if __name__ == "__main__":
    main()
