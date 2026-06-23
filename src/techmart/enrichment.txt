"""Enrichment functions for TechMart order data."""
import pandas as pd
import numpy as np


def flag_high_value(df,threshold=500):
    """Flag orders above the threshold as high value."""
    df = df.copy()
    df['high_value'] = df['price'] > threshold
    return df

def add_price_category(df):
    """Categorise each order as budget, mid-range, or premium."""
    df = df.copy()
    def get_category(price):
        if price<100:
            return 'budget'
        elif price<500:
            return 'mid'
        return 'premium'
    df['price_category'] = df['price'].apply(get_category)
    return df
