# PDF Generation Commands

## Convert Markdown to PDF

### Command to generate PDF from markdown file:

```bash
# Step 1: Convert markdown to HTML
pandoc jul_system_architecture_updated.md -o jul_system_architecture_updated.html --standalone

# Step 2: Convert HTML to PDF using Chrome headless
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless --disable-gpu --print-to-pdf="/c/temp/system_architecture_report.pdf" --print-to-pdf-no-header "$(pwd)/jul_system_architecture_updated.html"

# Step 3: Copy PDF to current directory with proper filename
cp /c/temp/system_architecture_report.pdf "./jul_system_architecture_updated.pdf"

# Step 4: Clean up temporary HTML file
rm jul_system_architecture_updated.html
```

### One-liner command:
```bash
pandoc jul_system_architecture_updated.md -o jul_system_architecture_updated.html --standalone && "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless --disable-gpu --print-to-pdf="/c/temp/system_architecture_report.pdf" --print-to-pdf-no-header "$(pwd)/jul_system_architecture_updated.html" && cp /c/temp/system_architecture_report.pdf "./jul_system_architecture_updated.pdf" && rm jul_system_architecture_updated.html
```

## Prerequisites

- **Pandoc**: Must be installed for markdown to HTML conversion
- **Google Chrome**: Must be installed for HTML to PDF conversion
- **Temp directory**: Ensure `/c/temp/` directory exists

## Notes

- The command creates a high-quality PDF with proper formatting
- All diagrams and code blocks are preserved
- The PDF maintains the original document structure
- If permission issues occur, try using a different temporary directory

## Usage

1. Navigate to the UserManagement directory
2. Run the one-liner command above
3. The PDF will be generated as `jul_system_architecture_updated.pdf`