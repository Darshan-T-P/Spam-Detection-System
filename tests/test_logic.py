import pandas as pd
import pytest
from src.preprocess import preprocess

def test_preprocess_basic():
    # Create a dummy dataframe
    data = {
        'Content ': [' This is a test ', ' Another comment '],
        'Class': [0, 1]
    }
    df = pd.DataFrame(data)
    
    # Run preprocess
    X, y = preprocess(df)
    
    # Assertions
    assert len(X) == 2
    assert len(y) == 2
    assert 'content' in df.columns
    assert 'class' in df.columns

def test_preprocess_missing_values():
    # Create a dummy dataframe with a missing value
    data = {
        'Content ': [' This is a test ', None],
        'Class': [0, 1]
    }
    df = pd.DataFrame(data)
    
    # Run preprocess
    X, y = preprocess(df)
    
    # Assertions (dropna should remove one row)
    assert len(X) == 1
    assert len(y) == 1
