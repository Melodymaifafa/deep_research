#!/usr/bin/env python3
"""Main application entry point for Deep Research."""

import sys
import os
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def main():
    """Launch the Deep Research Gradio application."""
    # Import and run the Gradio app
    from deep_research.deep_research import ui
    ui.launch(inbrowser=True)

if __name__ == "__main__":
    main()