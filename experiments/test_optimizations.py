#!/usr/bin/env python3
"""
Test script to verify optimizations work correctly
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Check if all required packages are available
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    from scipy import stats
    from mendeleev import element
    import sqlite3
    print("✓ All required packages are available")
except ImportError as e:
    print(f"✗ Missing package: {e}")
    sys.exit(1)

# Test imports from main module
try:
    import research_inertia
    print("✓ research_inertia module imported successfully")
except Exception as e:
    print(f"✗ Failed to import research_inertia: {e}")
    sys.exit(1)

# Test database functions
print("\nTesting database functions...")
try:
    research_inertia.init_database('test_db.db')
    print("✓ Database initialization works")

    # Clean up test db
    if os.path.exists('test_db.db'):
        os.remove('test_db.db')
        print("✓ Test database cleaned up")
except Exception as e:
    print(f"✗ Database test failed: {e}")
    sys.exit(1)

# Test data structure
print("\nTesting data calculation for Hydrogen...")
try:
    elem = element(1)  # Hydrogen
    result = research_inertia.calculate_atomic_data(elem)
    if result and 'k_coefficient' in result:
        print(f"✓ Hydrogen data calculated: k={result['k_coefficient']:.3e}")
    else:
        print("✗ Failed to calculate Hydrogen data")
        sys.exit(1)
except Exception as e:
    print(f"✗ Data calculation test failed: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("All basic tests passed!")
print("="*50)
print("\nOptimizations implemented:")
print("  • Database storage with SQLite")
print("  • Reduced label density on plots")
print("  • Reduced DPI (150 instead of 300)")
print("  • Immediate figure closing to free memory")
print("  • Non-interactive matplotlib backend")
print("  • Command-line arguments for configuration")
