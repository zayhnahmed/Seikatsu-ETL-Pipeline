# Seikatsu ETL Pipeline

A minimal Extract-Transform-Load (ETL) pipeline demonstrating data processing principles for journal entries from the Seikatsu personal development application.

## Overview

This pipeline processes raw journal data through three distinct stages:

1. **Extract**: Read raw journal entries from JSON source
2. **Transform**: Clean, normalize, and enrich the data
3. **Load**: Persist processed data to storage layer

## Project Structure

```
seikatsu-etl-pipeline/
├── data/
│   └── raw_journals.json       # Sample raw journal entries
├── etl/
│   ├── __init__.py
│   ├── extract.py              # Data extraction module
│   ├── transform.py            # Data transformation module
│   └── load.py                 # Data loading module
├── main.py                     # Pipeline orchestrator
├── requirements.txt
└── README.md
```

## Pipeline Stages

### Extract
- Reads raw journal entries from JSON file
- Handles file I/O errors gracefully
- Returns structured data for processing

### Transform
- Strips whitespace and normalizes text
- Parses timestamps into standard ISO format
- Calculates word count metrics
- Extracts mood and category information
- Produces clean, consistent data structure

### Load
- Persists processed data to JSON storage
- Generates summary statistics
- Displays category distribution
- In production: would integrate with PostgreSQL/vector database

## Usage

Run the complete pipeline:

```bash
python main.py
```

Run individual stages for testing:

```bash
# Test extraction
python etl/extract.py

# Test transformation
python etl/transform.py

# Test loading
python etl/load.py
```

## Sample Output

```
============================================================
SEIKATSU ETL PIPELINE
============================================================

[1/3] EXTRACTING raw journal data...
✓ Extracted 5 journal entries

[2/3] TRANSFORMING and cleaning data...
✓ Transformed 5 journal entries

[3/3] LOADING processed data...
✓ Loaded 5 journal entries to data/processed_journals.json

Summary Statistics:
  Total entries: 5
  Total words: 67
  Avg words/entry: 13.4

Category Distribution:
  Career: 1
  Learning: 1
  Relationships: 1
  Spirituality: 1
  Strength: 1

============================================================
✓ ETL PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

## Use Case in Seikatsu

This ETL pipeline forms the foundation for:

- **Analytics Dashboard**: Processing journal data for insights
- **AI-Powered Recommendations**: Preparing data for ML models
- **Trend Analysis**: Identifying patterns in user journaling habits
- **Data Quality**: Ensuring consistent data structure for downstream systems

## Technical Stack

- **Language**: Python 3.8+
- **Dependencies**: Standard library only (minimal footprint)
- **Data Format**: JSON (easy to extend to PostgreSQL/pgvector)

## Future Enhancements

- PostgreSQL integration for persistent storage
- pgvector support for semantic search capabilities
- Batch processing for large datasets
- Data validation with Pydantic
- Airflow/Prefect orchestration for scheduled runs

## Academic Context

This project demonstrates:
- Clean separation of ETL concerns
- Error handling and data validation
- Scalable architecture patterns
- Real-world data engineering principles

---

**Author**: Zayn  
**Project**: Seikatsu Personal Development App  
**Purpose**: Data engineering portfolio demonstration
