"""Run the TechMart pipeline."""
import sys

from techmart.cleaning import remove_duplicates
from techmart.ingestion import load_orders
from techmart.validation import validate_order


def run(path):
    df = load_orders(path)
    df = df[df["order_id"].apply(validate_order)]
    df = remove_duplicates(df)
    print(f"Pipeline complete: {len(df)} orders processed.")
    return df


if __name__ == "__main__":
    run(sys.argv[1])
