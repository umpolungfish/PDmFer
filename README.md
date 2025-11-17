# PDmFer - Production-Ready PDF Embedding CLI Tool

PDmFer is an enterprise-grade command-line tool for embedding interactive elements into PDF documents. It allows you to embed JavaScript functionality or download redirects, add blur effects, password protection, custom metadata, and more.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Options Overview](#options-overview)
- [Examples](#examples)
- [Advanced Usage](#advanced-usage)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Support](#support)

## Features

- **Input & Output Options**: Specify input PDF and output PDF paths
- **Embedding Options**: DownloadRedirect for creating download redirects
- **Link Integration**: Add custom link addresses to your PDFs
- **Blur Effects**: Apply None, Low, Medium, or High blur levels to content
- **Password Protection**: Secure your documents with passwords
- **Custom Messages**: Add pre-download redirect messages
- **Metadata Support**: Set Title, Author, Subject, and Keywords
- **Enterprise-Grade**: Built for production environments with robust error handling
- **Visual Customization**: Apply blur effects to content for privacy or presentation
- **Security Controls**: Password protection and metadata customization
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pdmfer
   ```

2. **Create and activate virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Quick Start

Get started with PDmFer in seconds:

```bash
# Basic download redirect
pdmfer -i input.pdf -o output.pdf --link "https://example.com"

# With blur and password
pdmfer -i input.pdf -o output.pdf --link "https://example.com" --blur Medium --password "secure123"
```

## Usage

```bash
pdmfer -i input.pdf -o output.pdf --link "https://example.com" [options...]
```

### Options Overview

| Option | Description | Values | Default |
|--------|-------------|---------|---------|
| `-i, --input` | Input PDF file path | File path | Required |
| `-o, --output` | Output PDF file path | File path | Required |
| `--link` | Link address for the embedded PDF | URL string | Required |
| `--blur` | Blur level | `None`, `Low`, `Medium`, `High` | `None` |
| `--password` | Password to protect document | Password string | None |
| `--redirect-message` | Custom pre-download message | Text string | None |
| `--title` | Custom title for PDF metadata | Text string | None |
| `--author` | Custom author for PDF metadata | Text string | None |
| `--subject` | Custom subject for PDF metadata | Text string | None |
| `--keywords` | Custom keywords for PDF metadata | Comma-separated text | None |
| `-v, --verbose` | Enable verbose output | Flag | Disabled |

## Examples

### Basic Examples

```bash
# Basic download redirect
pdmfer -i input.pdf -o output.pdf --link "https://example.com"

# Download redirect
pdmfer -i input.pdf -o output.pdf --link "https://example.com/download"

# With blur effect
pdmfer -i input.pdf -o output.pdf --link "https://example.com" --blur High

# With password protection
pdmfer -i input.pdf -o output.pdf --link "https://example.com" --password "secret123"

# Complete example with all options
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

### Advanced Examples

```bash
# Complete customization
pdmfer -i input.pdf -o output.pdf \
  --link "https://example.com" \
  --blur Medium \
  --password "securepassword123" \
  --redirect-message "Accessing secure content..." \
  --title "Secure Document" \
  --author "John Doe" \
  --subject "Confidential Report" \
  --keywords "secure,confidential,report"
```

### Enterprise Examples

```bash
# Batch processing script example
find . -name "*.pdf" -exec pdmfer -i {} -o processed_{} --link "https://secure.example.com" --blur Low \;

# Process confidential document
pdmfer -i confidential.pdf -o secure_confidential.pdf \
  --link "https://internal.example.com/access" \
  --blur High \
  --password "enterprise_secret" \
  --redirect-message "Accessing restricted content. Authentication required." \
  --title "Confidential Document" \
  --author "Corporate Security Team" \
  --subject "Internal Use Only" \
  --keywords "confidential,restricted,secure,corporate"
```

## Advanced Usage



### Blur Effects Explained

- `None`: No blur effect applied - original content preserved
- `Low`: Subtle blur for mild privacy or aesthetic effect
- `Medium`: Moderate blur for general obfuscation
- `High`: Strong blur for maximum privacy or visual effect

Blur effects work by converting PDF content to images and applying Gaussian blur filters.

### Metadata Customization

Custom metadata improves document organization and searchability:

- **Title**: Document name in PDF viewers and file systems
- **Author**: Creator attribution
- **Subject**: Brief description of content
- **Keywords**: Comma-separated tags for search and categorization

## Security Considerations

### Password Protection
- Uses AES-128 encryption for PDF security
- Protects against unauthorized access
- Compatible with standard PDF viewers

### JavaScript Security
- All JavaScript is embedded within the PDF
- Execution requires JavaScript-enabled viewer
- Follows PDF security standards

### Link Validation
- All links must use full URL format (http:// or https://)
- Links are validated before PDF creation

## Troubleshooting

### Common Issues

1. **"Error: Input file does not exist"**
   - Verify the file path is correct
   - Ensure the input file has a `.pdf` extension

2. **"Error: Link must start with http:// or https://"**
   - Ensure your link uses the proper protocol
   - Example: `https://example.com` not `example.com`

3. **JavaScript features not working**
   - Check that your PDF viewer has JavaScript enabled
   - Some viewers disable JavaScript for security reasons

4. **PDF appears corrupted**
   - Ensure all required options are provided
   - Check file permissions for input and output directories

### Verbose Mode
Use the `-v` flag for detailed output:
```bash
pdmfer -i input.pdf -o output.pdf --link "https://example.com" -v
```

### Support
If you encounter issues not covered here, please contact support or open an issue in the repository.

## Performance

PDmFer is designed for high-performance processing:
- Efficient memory usage for large PDFs
- Optimized processing algorithms
- Multi-library approach for feature compatibility

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.

### Contributing
- Fork the repository
- Create a feature branch
- Submit a pull request
- Ensure all tests pass

### Versioning
PDmFer uses semantic versioning (Major.Minor.Patch). Updates that change functionality will increment the major version.

### Changelog
- v1.0.0: Initial release with core functionality
- Enhanced blur algorithms for better visual effects
- Improved JavaScript embedding for PDF interaction
- Support for custom metadata fields
- Password protection with AES encryption