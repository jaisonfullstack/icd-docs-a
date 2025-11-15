#!/usr/bin/env python3
"""
Convert Markdown to Word document using pypandoc
"""
import pypandoc
import os

# Input and output file paths
input_file = '/home/user/icd-docs-a/JUL_SINTECE_Integration_Control_Document.md'
output_file = '/home/user/icd-docs-a/JUL_SINTECE_Integration_Control_Document.docx'

try:
    # Ensure pandoc is available
    pypandoc.ensure_pandoc_installed()

    # Convert markdown to docx
    print(f"Converting {input_file} to {output_file}...")
    output = pypandoc.convert_file(
        input_file,
        'docx',
        outputfile=output_file,
        extra_args=[
            '--standalone',
            '--toc',  # Add table of contents
            '--number-sections'  # Number sections
        ]
    )

    print(f"✓ Successfully converted to Word document: {output_file}")
    print(f"  File size: {os.path.getsize(output_file)} bytes")

except Exception as e:
    print(f"✗ Error during conversion: {str(e)}")
    exit(1)
