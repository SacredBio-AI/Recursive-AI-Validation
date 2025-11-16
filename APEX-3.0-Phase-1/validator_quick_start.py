"""
APEX 3.0 - Quick Start Validator
Run this to execute validation tests
"""

import sys
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from apex_core import run_validation_suite

def main():
    print("=" * 70)
    print("APEX 3.0 Phase 1 - Validation Runner")
    print("=" * 70)
    print()
    
    print("Running validation suite...")
    results = run_validation_suite()
    
    print("✓ Validation complete")
    print()
    print("Results:")
    print(f"  Input: {results['input']}")
    print(f"  Checksum: {results['checksum']:.6f}")
    print()
    
    # Save results
    output_file = Path('results') / 'validation_output.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✓ Results saved to: {output_file}")
    print()
    print("Next step: python submit_results\\generate_submission.py")
    print("=" * 70)

if __name__ == "__main__":
    main()