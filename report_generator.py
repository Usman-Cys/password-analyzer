import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Dict, Any

class ReportGenerator:
    """Generates visual and data reports."""

    def __init__(self, verbose: bool = False):
        self.console = Console()
        self.verbose = verbose

    def format_time(self, seconds: float) -> str:
        """Helper to format large time values."""
        if seconds < 1: return "Instantly"
        if seconds < 60: return f"{int(seconds)} seconds"
        if seconds < 3600: return f"{int(seconds/60)} minutes"
        if seconds < 86400: return f"{int(seconds/3600)} hours"
        if seconds < 31536000: return f"{int(seconds/86400)} days"
        return f"{int(seconds/31536000)} years"

    def generate_cli_report(self, data: Dict[str, Any]):
        """Prints a colored report to terminal."""
        color = "green" if data['score'] > 70 else "yellow" if data['score'] > 40 else "red"
        
        table = Table(title="Password Analysis Result", show_header=False)
        table.add_row("Password", "*" * len(data['password']))
        table.add_row("Strength", f"[{color}]{data['label']}[/{color}]")
        table.add_row("Entropy", f"{data['entropy']} bits")
        table.add_row("Score", f"{data['score']}/100")
        
        self.console.print(table)

        crack_table = Table(title="Time to Crack Estimates", box=None)
        crack_table.add_column("Attack Type", style="cyan")
        crack_table.add_column("Time Estimate", style="magenta")
        crack_table.add_row("Online (100 guesses/sec)", self.format_time(data['crack_times']['online']))
        crack_table.add_row("Offline (10B guesses/sec)", self.format_time(data['crack_times']['offline']))
        
        self.console.print(crack_table)

        if data['findings']:
            self.console.print(Panel("\n".join(f"• {f}" for f in data['findings']), title="Security Warnings", border_style="red"))

    def export_json(self, data: Any, filename: str):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
