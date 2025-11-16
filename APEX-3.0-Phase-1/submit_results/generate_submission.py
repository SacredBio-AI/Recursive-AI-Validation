
"""
APEX 3.0 - Submission Generator
Generates files for email submission
"""

import json
import hashlib
import platform
from pathlib import Path
from datetime import datetime

def generate_submission():
    print("=" * 70)
    print("APEX 3.0 - Generating Submission Files")
    print("=" * 70)
    print()
    
    # Load validation results
    results_file = Path('results') / 'validation_output.json'
    
    if not results_file.exists():
        print("❌ ERROR: No validation results found")
        print("Run: python validator_quick_start.py first")
        return
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Generate submission package
    submission = {
        'timestamp': datetime.now().isoformat(),
        'validator_system': {
            'os': platform.system(),
            'python_version': platform.python_version(),
        },
        'validation_results': results,
        'checksum_verification': results['checksum']
    }
    
    # Save submission files
    submit_dir = Path('submit_results')
    
    # 1. Full results
    with open(submit_dir / 'submission.json', 'w') as f:
        json.dump(submission, f, indent=2)
    
    # 2. Hash verification
    result_hash = hashlib.sha256(
        json.dumps(results, sort_keys=True).encode()
    ).hexdigest()
    
    with open(submit_dir / 'verification_hash.txt', 'w') as f:
        f.write(f"APEX 3.0 Validation Hash\n")
        f.write(f"SHA-256: {result_hash}\n")
    
    # 3. System info
    with open(submit_dir / 'system_info.txt', 'w') as f:
        f.write(f"Python: {platform.python_version()}\n")
        f.write(f"OS: {platform.system()} {platform.release()}\n")
        f.write(f"Timestamp: {submission['timestamp']}\n")
    
    print("✓ Generated 3 files in submit_results/:")
    print("  1. submission.json")
    print("  2. verification_hash.txt")
    print("  3. system_info.txt")
    print()
    print("Email these 3 files to: validation@sacredbio.ai")
    print()
    print("=" * 70)

if __name__ == "__main__":
    generate_submission()