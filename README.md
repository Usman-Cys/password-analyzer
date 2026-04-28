# Password Strength Analyzer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready CLI tool to analyze password strength using Shannon Entropy, pattern detection, and dictionary checks.

## Features
- **Entropy Calculation**: Shannon entropy in bits.
- **Pattern Detection**: Keyboard walks, repeats, and sequences.
- **Dictionary Checks**: Matches against common passwords and leetspeak substitutions.
- **Scoring**: Qualitative strength levels and time-to-crack estimates.
- **Reporting**: Beautiful CLI output and JSON exports.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python analyzer.py -p "MyP@ssw0rd123"
```
