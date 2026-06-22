"""Example test to show pytest working.

Copy this pattern when you write your own tests in Module 5.
"""

import pandas as pd
import pytest


@pytest.fixture
def sample_orders():
    """A small sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "customer": ["Ava", "Ben", "Cara"],
        }
    )


def test_sample_orders(sample_orders):
    """Example test - shows pytest passing."""
    assert len(sample_orders) == 3
    assert "order_id" in sample_orders.columns
    assert sample_orders["order_id"].is_unique
