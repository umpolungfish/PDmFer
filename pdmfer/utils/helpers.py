import os
import re
from typing import Optional


def validate_url(url: str) -> bool:
    if not url:
        return False
    
    url_pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return url_pattern.match(url) is not None


def validate_pdf_path(path: str) -> bool:
    return path.lower().endswith('.pdf') and os.path.exists(path)


def sanitize_filename(filename: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def format_keywords(keywords: str) -> str:
    if not keywords:
        return ""
    
    keyword_list = [kw.strip() for kw in keywords.split(',')]
    return ','.join(keyword_list)


def get_file_size_mb(filepath: str) -> float:
    if not os.path.exists(filepath):
        return 0.0
    
    size_bytes = os.path.getsize(filepath)
    size_mb = size_bytes / (1024 * 1024)
    return round(size_mb, 2)


def create_backup_path(filepath: str) -> str:
    name, ext = os.path.splitext(filepath)
    return f"{name}.bak{ext}"