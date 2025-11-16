"""
APEX 3.0 - Complete Test Runner
Supports multi-seed validation, all test modes, and full reporting
"""

import sys
import json
import argparse
from datetime import datetime
import numpy as np

try:
    from apex_3_0_core import APEX_3_0, APEXConfig
except ImportError:
    print("ERROR: apex_3_0_core module not found")
    print("Ensure apex_3_0_core.cp312-win_amd64.pyd is in the same directory")
    sys.exit(1)


def run_single_seed(seed, config):
    """Run APEX test for a single seed"""
    system = APEX_3_0(config, seed=seed)
    results = system.run_test()
    return results


def run_multi_seed_test(seeds, test_mode="phase_1f", cycles=2000):
    """Run multi-seed validation"""
    config = APEXConfig(test_mode=test_mode, num_cycles=cycles)
    
    all_results = []
    growth_values = []
    
    print(f"\n{'='*60}")
    print(f"APEX 3.0 Multi-Seed Validation - {test_mode.upper()}")
    print(f"Seeds: {seeds}")
    print(f"{'='*60}")
    
    for seed in seeds:
        print(f"\nTesting seed {seed}...")
        system = APEX_3_0(config, seed=seed)
        results = system.run_test()
        all_results.append(results)
        growth_values.append(results['performance']['growth_percent'])
    
    # Calculate summary statistics
    mean = np.mean(growth_values)
    std = np.std(growth_values)
    min_val = np.min(growth_values)
    max_val = np.max(growth_values)
    
    print(f"\n{'='*60}")
    print(f"SUMMARY - {test_mode.upper()}")
    print(f"{'='*60}")
    print(f"Mean Growth:  {mean:.2f}%")
    print(f"Std Dev:      {std:.2f}%")
    print(f"Min Growth:   {min_val:.2f}%")
    print(f"Max Growth:   {max_val:.2f}%")
    print(f"{'='*60}\n")
    
    return {
        'summary': {
            'test_mode': test_mode,
            'mean_growth': float(mean),
            'std_growth': float(std),
            'min_growth': float(min_val),
            'max_growth': float(max_val),
            'num_seeds': len(seeds),
            'seeds': seeds
        },
        'individual_results': all_results
    }


def main():
    parser = argparse.ArgumentParser(
        description='APEX 3.0 - Complete Test Runner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single seed test (quick)
  python apex_runner.py --seed 42
  
  # Multi-seed validation
  python apex_runner.py --seeds 42 123 456
  
  # Different test modes
  python apex_runner.py --seeds 42 123 456 --test-mode phase_1g_aggressive
  python apex_runner.py --seeds 42 123 456 --test-mode phase_1h_extremes
  
  # Save results to file
  python apex_runner.py --seeds 42 123 456 --output my_results.json
  
  # Quick test with fewer cycles
  python apex_runner.py --seed 42 --cycles 500
        """
    )
    
    parser.add_argument('--seed', type=int, default=None,
                       help='Single seed to test (default: 42 if no --seeds specified)')
    parser.add_argument('--seeds', type=int, nargs='+', default=None,
                       help='Multiple seeds for validation (e.g., --seeds 42 123 456)')
    parser.add_argument('--test-mode', type=str, default='phase_1f',
                       choices=['phase_1f', 'phase_1g_aggressive', 'phase_1h_extremes'],
                       help='Test mode: phase_1f (standard), phase_1g_aggressive (stress test), phase_1h_extremes (find ceiling)')
    parser.add_argument('--cycles', type=int, default=2000,
                       help='Number of cycles to run (default: 2000)')
    parser.add_argument('--output', type=str, default=None,
                       help='Output file for results (JSON format)')
    
    args = parser.parse_args()
    
    # Determine what to run
    if args.seeds:
        # Multi-seed validation
        results = run_multi_seed_test(args.seeds, args.test_mode, args.cycles)
    else:
        # Single seed test
        seed = args.seed if args.seed else 42
        config = APEXConfig(test_mode=args.test_mode, num_cycles=args.cycles)
        print(f"\nRunning single seed test: seed={seed}, mode={args.test_mode}, cycles={args.cycles}\n")
        results = run_single_seed(seed, config)
        
        # Print summary
        print(f"\n=== RESULTS ===")
        print(f"Final REI: {results['performance']['final_rei']:.4f}")
        print(f"Growth: {results['performance']['growth_percent']:.2f}%")
        print(f"Status: {results['performance']['status']}")
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✓ Results saved to: {args.output}")
    
    return results


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
