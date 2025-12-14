"""
Extract module - Reads raw journal data from JSON source
"""
import json
from pathlib import Path


def extract(filepath="data/raw_journals.json"):
    """
    Extract raw journal entries from JSON file.
    
    Args:
        filepath: Path to the raw journal data
        
    Returns:
        list: Raw journal entries
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✓ Extracted {len(data)} journal entries")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File {filepath} not found")
        return []
    except json.JSONDecodeError:
        print(f"✗ Error: Invalid JSON in {filepath}")
        return []


if __name__ == "__main__":
    # Test extraction
    journals = extract()
    print(f"Sample entry: {journals[0] if journals else 'No data'}")
