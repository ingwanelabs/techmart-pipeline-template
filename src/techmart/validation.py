"""Data validation for the TechMart pipeline."""


def validate_order(order_id):
    """Check that an order ID is present and non-empty."""
    return bool(order_id)
