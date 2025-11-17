# FINAL IMPROVED PANDOC COMMAND FOR WORD CONVERSION

## For Windows Command Line (use this one):
pandoc JUL_SINTECE_Integration_Control_Document.md -o JUL_SINTECE_Integration_Control_Document.docx --reference-doc=reference_with_borders.docx --toc --toc-depth=3 --syntax-highlighting --wrap=preserve -f markdown+pipe_tables+grid_tables

## Alternative with table styling:
pandoc JUL_SINTECE_Integration_Control_Document.md -o JUL_SINTECE_Integration_Control_Document.docx --reference-doc=reference_with_borders.docx --toc --toc-depth=3 --syntax-highlighting --wrap=preserve -f markdown+pipe_tables+grid_tables+table_captions

## What was fixed:

### 1. Error Codes Formatting:
- Added blank lines after "**Error Codes:**" headers
- Added double spaces at the end of each error code line for proper line breaks in Word
- This ensures error codes display on separate lines instead of running together

### 2. Table Formatting:
- Enhanced CSS styling with stronger border definitions
- Added !important declarations to force border display
- Added special @media print rules for better pandoc conversion
- Used black borders instead of gray for better visibility
- Added alternating row colors for better readability

### 3. Pandoc Command Improvements:
- Replaced deprecated --highlight-style with --syntax-highlighting
- Added --wrap=preserve to maintain formatting
- Added -f markdown+pipe_tables+grid_tables for better table processing
- Used explicit table format support

## Usage:
Run the command from the directory containing your markdown file:

```bash
pandoc JUL_SINTECE_Integration_Control_Document.md -o JUL_SINTECE_Integration_Control_Document.docx --reference-doc=reference_with_borders.docx --toc --toc-depth=3 --syntax-highlighting --wrap=preserve -f markdown+pipe_tables+grid_tables
```

This should now generate a Word document with:
✓ Properly formatted tables with all borders visible
✓ Error codes displaying on separate lines
✓ Proper table of contents
✓ Better overall formatting