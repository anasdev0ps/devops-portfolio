#!/usr/bin/env python3
"""
PDF Generation Utility for Job Assistant Hub
Converts responsive HTML resumes to print-ready PDFs using WeasyPrint.
"""
import sys
import os
from pathlib import Path
import weasyprint

def convert_html_to_pdf(html_path: str, pdf_path: str):
    html_file = Path(html_path)
    if not html_file.exists():
        print(f"Error: HTML file '{html_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    pdf_file = Path(pdf_path)
    pdf_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Rendering '{html_path}' -> '{pdf_path}'...")
    html = weasyprint.HTML(filename=str(html_file), base_url=str(html_file.parent))
    html.write_pdf(target=str(pdf_file), presentational_hints=True)
    print(f"Successfully created: {pdf_path} ({pdf_file.stat().st_size} bytes)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_pdf.py <input.html> <output.pdf>")
        sys.exit(1)
    convert_html_to_pdf(sys.argv[1], sys.argv[2])
