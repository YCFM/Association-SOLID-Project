from interfaces.ui_interface import UIInterface
from pathlib import Path

class WebUI(UIInterface):
    """Web implementation of UI interface - generates HTML output."""
    
    def __init__(self, output_file="output.html"):
        self.output_file = output_file
        self.html_content = []
    
    def display_event_details(self, event_details: str):
        """Add event details to HTML content."""
        self.html_content.append(f"<h2>Event Details</h2>")
        self.html_content.append(f"<p>{event_details}</p>")
    
    def display_transactions(self, transactions):
        """Add transactions to HTML content."""
        self.html_content.append(f"<h2>Transactions</h2>")
        self.html_content.append("<ul>")
        if isinstance(transactions, list):
            for transaction in transactions:
                self.html_content.append(f"<li>{transaction}</li>")
        else:
            self.html_content.append(f"<li>{transactions}</li>")
        self.html_content.append("</ul>")
    
    def display_message(self, message: str):
        """Add a message to HTML content."""
        self.html_content.append(f"<p>{message}</p>")
    
    def show_results(self, event_details: str, transactions):
        """Generate and save HTML file with all results."""
        html = [
            '<!doctype html>',
            '<html><head><meta charset="utf-8"><title>Association Management</title>',
            '<style>',
            'body{padding:24px;background:#0b1220;color:#e2e8f0;font-family:Arial, sans-serif;}',
            'h1{color:#f8fafc;} h2{margin-top:24px;color:#93c5fd;}',
            'ul{list-style-type:none;padding:0;}',
            'li{padding:8px;margin:4px 0;background:#111827;border-left:3px solid #93c5fd;}',
            'p{line-height:1.6;}',
            '</style></head><body>',
            '<h1>Sports Association Management System</h1>'
        ]
        
        html.extend(self.html_content)
        html.extend(['</body></html>'])
        
        Path(self.output_file).write_text("\n".join(html), encoding="utf-8")
        print(f"✅ Web output generated: {self.output_file}")
