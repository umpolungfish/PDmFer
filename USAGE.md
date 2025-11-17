# PDmFer Usage Guide

This guide provides detailed instructions and examples for using the PDmFer PDF embedding CLI tool.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd pdmfer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -r requirements.txt
pip install -e .
```

## Core Functionality

### Basic Command Structure
```bash
pdmfer -i <input.pdf> -o <output.pdf> --link "<url>" [options]
```

### Required Options

#### Input & Output
```bash
-i, --input INPUT    Input PDF file path
-o, --output OUTPUT  Output PDF file path
```

#### Link Address
```bash
--link "<url>"        Link address to embed in the PDF (required)
```

### Embedding Options

#### Embed Type
```bash
--link URL
```
- `--link`: URL for download redirect

### Visual Effects

#### Blur Controls
```bash
--blur {None,Low,Medium,High}
```
- `None`: No blur effect applied
- `Low`: Light blur effect
- `Medium`: Moderate blur effect
- `High`: Strong blur effect

### Security Options

#### Password Protection
```bash
--password "secret123"
```
Protects the PDF with a password.

### Content Customization

#### Custom Messages
```bash
--redirect-message "Custom message to display"
```
Add a custom pre-download redirect message.

#### Metadata Options
```bash
--title "Document Title"        # Set PDF title
--author "Author Name"          # Set PDF author
--subject "Document Subject"    # Set PDF subject
--keywords "keyword1,keyword2"  # Set PDF keywords (comma-separated)
```

### Verbose Output
```bash
-v, --verbose
```
Enable verbose output for detailed processing information.

## Complete Examples

### Basic Usage
```bash
# Basic download redirect
pdmfer -i input.pdf -o output.pdf --link "https://example.com"
```

### Visual Effects
```bash
# Add blur effect to PDF content
pdmfer -i input.pdf -o output.pdf --link "https://example.com" --blur High
```

### Security & Customization
```bash
# Full security and customization
pdmfer -i input.pdf -o output.pdf \
  --link "https://example.com" \
  --blur Medium \
  --password "securepassword" \
  --redirect-message "Redirecting to secure content..." \
  --title "Secure Document" \
  --author "Document Author" \
  --subject "Security Document" \
  --keywords "secure,protected,confidential"
```

### Download Redirect
```bash
# Download redirect with custom messaging
pdmfer -i input.pdf -o output.pdf \
  --link "https://example.com/download" \
  --redirect-message "Your download will begin shortly"
```

### Complete Example with All Options
```bash
# Complete example with all available options
pdmfer -i input.pdf -o output.pdf \
  --link "https://example.com/download" \
  --blur Medium \
  --password "secure123" \
  --redirect-message "Download will start shortly" \
  --title "Secure PDF" \
  --author "Author Name" \
  --subject "Document Subject" \
  --keywords "secure,download,pdf" \
  --verbose
```

## Advanced Usage Patterns

### Batch Processing
Process multiple PDFs in a script:
```bash
#!/bin/bash
for pdf in *.pdf; do
  pdmfer -i "$pdf" -o "processed_$pdf" --link "https://example.com"
done
```

### Integration in Scripts
```bash
# Conditionally apply blur based on file size
if [ $(stat -f%z input.pdf) -gt 1000000 ]; then
  pdmfer -i input.pdf -o output.pdf --link "https://example.com" --blur Medium
else
  pdmfer -i input.pdf -o output.pdf --link "https://example.com" --blur Low
fi
```

## Troubleshooting

### Common Issues

1. **Invalid PDF inputs**: Ensure input files are valid PDFs with `.pdf` extension
2. **Link format**: Links must start with `http://` or `https://`
3. **Permissions**: Check write permissions for output directory
4. **JavaScript execution**: PDF viewer must have JavaScript enabled for interactive features

### Verbose Output
Use the `-v` flag to get detailed processing information:
```bash
pdmfer -i input.pdf -o output.pdf --link "https://example.com" -v
```

## Enterprise Usage

### Configuration Files
For complex deployments, create configuration files:
```bash
# Create a config file with common options
echo "--blur Medium --redirect-message 'Processing...' --password 'secure_password'" > pdmfer.conf

# Use config with additional options
pdmfer -i input.pdf -o output.pdf --link "https://example.com" @pdmfer.conf
```

### Security Best Practices
- Use strong passwords for protected documents
- Verify link safety before embedding
- Sanitize metadata inputs to prevent injection attacks