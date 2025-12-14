"""
Transform module - Cleans and normalizes journal data
"""
from datetime import datetime


def transform(journals):
    """
    Transform raw journal entries into clean, normalized format.
    
    Transformations applied:
    - Strip whitespace from text
    - Normalize text to lowercase
    - Parse timestamps
    - Extract key fields
    - Add word count metric
    
    Args:
        journals: List of raw journal entries
        
    Returns:
        list: Cleaned and normalized journal entries
    """
    cleaned = []
    
    for entry in journals:
        try:
            # Clean and normalize text
            cleaned_text = entry["text"].strip()
            normalized_text = cleaned_text.lower()
            
            # Calculate basic metrics
            word_count = len(cleaned_text.split())
            
            # Parse timestamp
            timestamp = datetime.fromisoformat(entry["timestamp"].replace('Z', '+00:00'))
            
            cleaned_entry = {
                "user_id": entry["user_id"],
                "timestamp": timestamp.isoformat(),
                "date": timestamp.date().isoformat(),
                "text_original": cleaned_text,
                "text_normalized": normalized_text,
                "word_count": word_count,
                "mood": entry.get("mood", "neutral"),
                "category": entry.get("category", "General")
            }
            
            cleaned.append(cleaned_entry)
            
        except Exception as e:
            print(f"✗ Error transforming entry: {e}")
            continue
    
    print(f"✓ Transformed {len(cleaned)} journal entries")
    return cleaned


if __name__ == "__main__":
    # Test transformation
    sample = [{
        "user_id": 1,
        "timestamp": "2024-12-01T08:30:00Z",
        "text": "  Test entry  ",
        "mood": "positive",
        "category": "Test"
    }]
    
    result = transform(sample)
    print(f"Sample transformed entry: {result[0]}")
