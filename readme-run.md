# JUL SINTECE Integration Control Document - PDF Generation

## 📖 Overview
This document provides instructions for generating a professional PDF from the JUL SINTECE Integration Control Document with proper formatting, headers, footers, and clickable table of contents.

## 🔧 Prerequisites
Before generating the PDF, ensure you have the following installed:

### Node.js and npm
```bash
# Check if Node.js is installed
node --version

# Check if npm is installed
npm --version
```

### md-to-pdf Package
```bash
# Install md-to-pdf globally (recommended)
npm install -g md-to-pdf

# OR install locally in project directory
npm install md-to-pdf
```

## 📄 Files Required
- `JUL_SINTECE_Integration_Control_Document.md` - Main documentation file
- `.md2pdf.json` - PDF configuration file with styling and layout settings

## 🚀 PDF Generation Commands

### Primary Command (Recommended)
```bash
npx md-to-pdf JUL_SINTECE_Integration_Control_Document.md --config-file .md2pdf.json
```

### Alternative Commands
```bash
# Using global installation
md-to-pdf JUL_SINTECE_Integration_Control_Document.md --config-file .md2pdf.json

# Using local installation
./node_modules/.bin/md-to-pdf JUL_SINTECE_Integration_Control_Document.md --config-file .md2pdf.json

# Without explicit config file (uses .md2pdf.json automatically)
npx md-to-pdf JUL_SINTECE_Integration_Control_Document.md
```

## ✨ Generated PDF Features

### 📋 Table of Contents
- **Clickable navigation** - Direct links to all sections and subsections
- **Borderless design** - Clean, professional appearance
- **Full-width layout** - Utilizes entire page width
- **Hierarchical indentation**:
  - Main sections: No indentation
  - Subsections: 30px left padding
  - Sub-subsections: 50px left padding

### 📄 Headers & Footers
- **Header**: JUL SINTECE Integration Control Document - CNCA Certificate Process
- **Footer**: 
  - Left: Abu Dhabi Ports - Confidential
  - Right: Page X of Y (dynamic page numbers)
  - Center: Generated on [Date]

### 🎨 Professional Styling
- **Abu Dhabi Ports branding** with corporate color scheme (#2E5BBA)
- **Typography**: Segoe UI font family for readability
- **A4 format** with 30mm/20mm margins
- **Syntax highlighting** for code blocks
- **Responsive tables** with borders for data presentation

## 📊 Output Details
- **File**: `JUL_SINTECE_Integration_Control_Document.pdf`
- **Size**: ~4.2MB
- **Pages**: 100+ pages with comprehensive API documentation
- **Format**: A4 with professional layout

## 🔍 Verification
After generation, verify the PDF includes:
- [ ] Clickable table of contents with proper navigation
- [ ] Headers and footers on all pages
- [ ] Page numbers displayed correctly
- [ ] All API sections with JSON samples
- [ ] Professional Abu Dhabi Ports formatting

## 🛠️ Troubleshooting

### Common Issues
1. **Command not found**: Install md-to-pdf using npm
2. **Config file not found**: Ensure `.md2pdf.json` is in the same directory
3. **Missing headers/footers**: Use the `--config-file` parameter explicitly

### Debug Commands
```bash
# Check file existence
ls -la JUL_SINTECE_Integration_Control_Document.md .md2pdf.json

# Verify npm packages
npm list md-to-pdf

# Generate with verbose output
npx md-to-pdf JUL_SINTECE_Integration_Control_Document.md --config-file .md2pdf.json --verbose
```

## 📝 Notes
- The configuration file (`.md2pdf.json`) contains all styling, layout, and formatting rules
- Page numbers and navigation links are automatically generated
- The PDF maintains all formatting from the Markdown source with enhanced visual presentation
- Generated PDF is suitable for official Abu Dhabi Ports documentation standards

## 📞 Support
For issues with PDF generation or formatting, verify:
1. All source files are present and readable
2. Node.js and npm are properly installed
3. md-to-pdf package is available
4. Configuration file syntax is valid JSON

---
**Generated**: November 13, 2025  
**Author**: Linoy Pappachan Malakkaran  
**Organization**: Abu Dhabi Ports