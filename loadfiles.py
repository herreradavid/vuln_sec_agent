import os
from pathlib import Path


def read_files(directory_path, exclude_dirs=None):
    """
    Recursively reads text from files in a directory (including subdirectories),
    excluding any specified in 'exclude_dirs', and returns their contents as a list of strings.
    """
    if exclude_dirs is None:
        exclude_dirs = ['test']  # Default to excluding 'test' directories
    text_contents = []
    text_length = 0

    for path in Path(directory_path).rglob('*.go'):
        # Check if path is in an excluded directory
        if any(excluded_dir in path.parts for excluded_dir in exclude_dirs):
            continue  # Skip files in excluded directories
        with open(path) as file:
            content = f'{{"file"="{path}", "content"=\'{file.read()}\' }}'
            text_length += len(content)
            text_contents.append(content)
    return text_length, text_contents


def preprocess_text(texts):
    """
    Basic preprocessing of the text data.
    """
    processed_texts = []
    for text in texts:
        processed_text = text.strip()
        processed_texts.append(processed_text)
    return processed_texts


def read_files_v2(directory_path, exclude_dirs=None):
    """
    Recursively reads text from files in a directory (including subdirectories),
    excluding any specified in 'exclude_dirs', and returns their contents as a list of strings.
    """
    if exclude_dirs is None:
        exclude_dirs = ['test']  # Default to excluding 'test' directories
    text_contents = []
    text_length = 0

    for path in Path(directory_path).rglob('*.go'):
        # Check if path is in an excluded directory
        if any(excluded_dir in path.parts for excluded_dir in exclude_dirs):
            continue  # Skip files in excluded directories
        with open(path) as file:
            content = f'{{"file"="{path}", "content"=```{file.read()}``` }}'
            text_length += len(content)
            text_contents.append(content)
    return text_length, text_contents
