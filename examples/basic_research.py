#!/usr/bin/env python3
"""
Basic usage example of the Deep Research system.

This example demonstrates how to use the ResearchManager programmatically
without the Gradio interface.
"""

import asyncio
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deep_research import ResearchManager


async def main():
    """Run a basic research example."""

    # Initialize the research manager
    manager = ResearchManager()

    # Define a research query
    query = "What are the latest developments in quantum computing in 2024?"

    print(f"Starting research on: {query}")
    print("-" * 50)

    # Run the research and print updates
    async for update in manager.run(query):
        print(f"📋 {update}")
        print("-" * 50)


if __name__ == "__main__":
    # Make sure you have your .env file configured with API keys
    asyncio.run(main())