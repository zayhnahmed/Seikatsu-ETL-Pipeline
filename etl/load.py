"""
Load module - Persists processed data to storage layer
"""
import json
from pathlib import Path


def load(data, output_file="data/processed_journals.json"):
    """
    Load processed journal entries to JSON storage.
    
    In production, this would insert into PostgreSQL/vector DB.
    For this demo, we simulate by writing to a processed file.
    
    Args:
        data: List of processed journal entries
        output_file: Path to output file
    """
    try:
        # Ensure output directory exists
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        
        # Write processed data
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Loaded {len(data)} journal entries to {output_file}")
        
        # Display summary statistics
        if data:
            total_words = sum(entry.get("word_count", 0) for entry in data)
            avg_words = total_words / len(data) if data else 0
            
            print(f"\nSummary Statistics:")
            print(f"  Total entries: {len(data)}")
            print(f"  Total words: {total_words}")
            print(f"  Avg words/entry: {avg_words:.1f}")
            
            # Category distribution
            categories = {}
            for entry in data:
                cat = entry.get("category", "General")
                categories[cat] = categories.get(cat, 0) + 1
            
            print(f"\nCategory Distribution:")
            for cat, count in sorted(categories.items()):
                print(f"  {cat}: {count}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return False


if __name__ == "__main__":
    # Test loading
    sample = [{
        "user_id": 1,
        "text_normalized": "test entry",
        "word_count": 2,
        "category": "Test"
    }]
    
    load(sample, "data/test_output.json")
