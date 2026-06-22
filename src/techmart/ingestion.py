"""Data ingestion for the TechMart pipeline."""

import pandas as pd


def load_orders(path):
    """Load raw TechMart order data from a CSV file."""
    return pd.read_csv(path)
