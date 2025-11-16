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

# word conversion

```
 pandoc JUL_SINTECE_Integration_Control_Document.md -o JUL_SINTECE_Integration_Control_Document_test.docx --reference-doc=reference_with_borders.docx --toc --toc-depth=3 --highlight-style=tango --wrap=preserve -f markdown+pipe_tables+grid_tables
```