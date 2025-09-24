# Examples

This directory contains example scripts demonstrating different ways to use the Deep Research system.

## Available Examples

### `basic_research.py`
Demonstrates basic programmatic usage of the ResearchManager without the Gradio UI.

**Usage:**
```bash
cd examples
python basic_research.py
```

## Running Examples

1. Make sure you have installed the dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Set up your environment variables by copying and editing `.env.example`:
   ```bash
   cp ../.env.example ../.env
   # Edit .env with your API keys
   ```

3. Run any example:
   ```bash
   python basic_research.py
   ```

## Creating Your Own Examples

Feel free to create additional examples by:
1. Copying `basic_research.py` as a template
2. Modifying the query and research parameters
3. Adding custom processing of the research results