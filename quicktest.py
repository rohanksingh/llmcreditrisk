#!/usr/bin/env python3
"""Quick test to verify Python environment"""

print("\nTesting Python Environment...\n")

import sys
print(f"Python version: {sys.version.split()[0]}")

packages = {'pandas': None, 'numpy': None}

for package in packages:
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'unknown')
        print(f"OK {package}: {version}")
        packages[package] = True
    except ImportError:
        print(f"MISSING {package}: NOT INSTALLED")
        packages[package] = False

try:
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(f"OK NumPy computation: mean([1,2,3,4,5]) = {arr.mean()}")
except:
    print("ERROR: NumPy test failed")

try:
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(f"OK Pandas DataFrame: {df.shape[0]} rows x {df.shape[1]} columns")
except:
    print("ERROR: Pandas test failed")

print("\n" + "="*60)
if all(packages.values()):
    print("SUCCESS: All tests passed! You're ready to run the examples.")
else:
    print("WARNING: Some packages are missing. Install with:")
    print("   pip install pandas numpy")
print("="*60 + "\n")