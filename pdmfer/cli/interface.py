import argparse
import sys
from typing import Optional


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="PDmFer - Production-Ready PDF Embedding CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -i input.pdf -o output.pdf --link "https://example.com"
  %(prog)s -i input.pdf -o output.pdf --link "https://example.com" --blur medium
  %(prog)s -i input.pdf -o output.pdf --link "https://example.com" --password "secret123"
        """
    )
    
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Input PDF file path"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Output PDF file path"
    )
    

    
    parser.add_argument(
        "--link",
        type=str,
        required=True,
        help="Link address for the embedded PDF"
    )
    
    parser.add_argument(
        "--blur",
        type=str,
        choices=["None", "Low", "Medium", "High"],
        default="None",
        help="Blur level for the embedded content (default: None)"
    )
    
    parser.add_argument(
        "--password",
        type=str,
        help="Password to protect the document (optional)"
    )
    
    parser.add_argument(
        "--redirect-message",
        type=str,
        help="Custom pre-download redirect message"
    )
    
    parser.add_argument(
        "--title",
        type=str,
        help="Custom title for the PDF metadata"
    )
    
    parser.add_argument(
        "--author",
        type=str,
        help="Custom author for the PDF metadata"
    )
    
    parser.add_argument(
        "--subject",
        type=str,
        help="Custom subject for the PDF metadata"
    )
    
    parser.add_argument(
        "--keywords",
        type=str,
        help="Custom keywords for the PDF metadata (comma-separated)"
    )
    

    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    return parser.parse_args()


def main_cli():
    try:
        args = parse_arguments()
        

            
        from pdmfer.core.processor import PDFProcessor
        
        processor = PDFProcessor(
            input_path=args.input,
            output_path=args.output,
            link=args.link,
            blur=args.blur,
            password=args.password,
            redirect_message=args.redirect_message,
            title=args.title,
            author=args.author,
            subject=args.subject,
            keywords=args.keywords,
            verbose=args.verbose
        )
        
        success = processor.process()
        
        if success:
            print(f"Successfully processed PDF: {args.input} -> {args.output}")
        else:
            print("PDF processing failed", file=sys.stderr)
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main_cli()