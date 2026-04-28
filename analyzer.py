import argparse
import sys
import logging
from entropy_engine import EntropyEngine
from dictionary_check import DictionaryCheck
from report_generator import ReportGenerator

def analyze_password(password: str, dict_checker: DictionaryCheck):
    engine = EntropyEngine()
    entropy = engine.calculate_entropy(password)
    findings = dict_checker.check_patterns(password)
    
    # Calculate score
    score = min(100, (entropy / 128) * 100)
    if dict_checker.is_common(password):
        score = score * 0.2
        findings.append("CRITICAL: Password found in common wordlist!")
    
    score = int(score - (len(findings) * 5))
    score = max(0, min(100, score))

    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    label = labels[min(4, score // 20)]

    # Crack time estimation
    pool_size = 2**(entropy/len(password)) if len(password) > 0 else 0
    guesses = 2**entropy
    
    return {
        "password": password,
        "entropy": entropy,
        "score": score,
        "label": label,
        "findings": findings,
        "crack_times": {
            "online": guesses / 100,
            "offline": guesses / 10**10
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer")
    parser.add_argument("-p", "--password", help="Single password to check")
    parser.add_argument("-f", "--file", help="Batch file for analysis")
    parser.add_argument("-j", "--json", help="Export result to JSON file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detailed output")
    
    args = parser.parse_args()
    
    dict_checker = DictionaryCheck("data/common_passwords.txt")
    reporter = ReportGenerator(verbose=args.verbose)

    if args.password:
        result = analyze_password(args.password, dict_checker)
        reporter.generate_cli_report(result)
        if args.json:
            reporter.export_json(result, args.json)
    elif args.file:
        # Batch processing logic would go here
        print("Batch processing not implemented in this snippet.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
