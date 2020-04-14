"""Code runner for estimator."""
from abstract import Calculate

def estimator(data):
    """Novelty COVID-19 infections estimator"""
    workings = Calculate(data)
    data = workings.estimator
    return data
