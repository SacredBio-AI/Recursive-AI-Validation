#!/usr/bin/env python3
"""
Pre-flight Python version check for APEX 3.0 validation.
Run this BEFORE setting up virtual environment.
"""

import sys
import platform

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 12

def check_version():
    """Check if Python version is exactly 3.12.x"""
    
    current_major = sys.version_info.major
    current_minor = sys.version_info.minor
    current_micro = sys.version_info.micro
    
    print("=" * 70)
    print("APEX 3.0 - Python Version Pre-Flight Check")
    print("=" * 70)
    print()
    
    print(f"Current Python: {current_major}.{current_minor}.{current_micro}")
    print(f"Required: {REQUIRED_MAJOR}.{REQUIRED_MINOR}.x (exactly)")
    print()
    
    # Check major and minor version
    if current_major != REQUIRED_MAJOR or current_minor != REQUIRED_MINOR:
        print("❌ VERSION CHECK FAILED")
        print()
        print(f"You are using Python {current_major}.{current_minor}.{current_micro}")
        print(f"You MUST use Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}.x")
        print()
        print("Why this is required:")
        print("  • Different Python versions produce different results")
        print("  • Validation requires exact deterministic reproducibility")
        print("  • Only Python 3.12.x will match expected cryptographic hashes")
        print()
        print("How to install Python 3.12.x:")
        print()
        print("  Option 1 - Direct Download:")
        print("    Visit: https://www.python.org/downloads/")
        print("    Download: Python 3.12.7 (or latest 3.12.x)")
        print()
        print("  Option 2 - pyenv (recommended):")
        print("    pyenv install 3.12.7")
        print("    pyenv local 3.12.7")
        print()
        print("  Option 3 - conda:")
        print("    conda create -n apex-validation python=3.12")
        print("    conda activate apex-validation")
        print()
        print("After installing, run this check again:")
        print("    python3 check_python_version.py")
        print()
        print("=" * 70)
        sys.exit(1)
    
    # Version is correct
    print("✓ Python 3.12.x detected")
    print("✓ Version check PASSED")
    print()
    
    # Additional system info
    print("System Information:")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  Architecture: {platform.machine()}")
    print(f"  Python implementation: {platform.python_implementation()}")
    print()
    
    print("✓ You may proceed with validation setup")
    print()
    print("Next steps:")
    print("  1. Create virtual environment: python -m venv venv")
    print("  2. Activate it: venv\\Scripts\\activate")
    print("  3. Verify venv Python: python --version  (must show 3.12.x)")
    print("  4. Install dependencies: pip install -r requirements.txt")
    print("  5. Run validation: python validator_quick_start.py")
    print()
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    check_version()