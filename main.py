"""
Seikatsu ETL Pipeline - Main Orchestrator

This pipeline demonstrates a simple Extract-Transform-Load process
for journal entries from the Seikatsu personal development app.

Pipeline Stages:
1. EXTRACT: Read raw journal entries from JSON
2. TRANSFORM: Clean, normalize, and enrich the data
3. LOAD: Persist processed data to storage layer

Usage:
    python main.py
"""

from etl.extract import extract
from etl.transform import transform
from etl.load import load


def run_etl_pipeline():
    """
    Execute the complete ETL pipeline.
    
    Returns:
        bool: True if pipeline completed successfully
    """
    print("=" * 60)
    print("SEIKATSU ETL PIPELINE")
    print("=" * 60)
    
    # STAGE 1: EXTRACT
    print("\n[1/3] EXTRACTING raw journal data...")
    raw_data = extract()
    
    if not raw_data:
        print("✗ Pipeline failed: No data extracted")
        return False
    
    # STAGE 2: TRANSFORM
    print("\n[2/3] TRANSFORMING and cleaning data...")
    processed_data = transform(raw_data)
    
    if not processed_data:
        print("✗ Pipeline failed: No data transformed")
        return False
    
    # STAGE 3: LOAD
    print("\n[3/3] LOADING processed data...")
    success = load(processed_data)
    
    if success:
        print("\n" + "=" * 60)
        print("✓ ETL PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
    else:
        print("✗ Pipeline failed: Load stage error")
    
    return success


if __name__ == "__main__":
    run_etl_pipeline()
