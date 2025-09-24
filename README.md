# Deep Research

A multi-agent research system that automatically conducts comprehensive research on any topic using AI agents and provides detailed reports via an interactive web interface.

## Features

- **Multi-Agent Architecture**: Specialized agents for planning, searching, writing, and emailing
- **Automated Research Pipeline**: Plans searches → Performs searches → Writes report → Sends email
- **Interactive Web UI**: Clean Gradio interface for easy interaction
- **Comprehensive Reports**: Detailed markdown reports with structured findings
- **Email Integration**: Automatic email delivery of research reports

## Architecture

The system follows a clean multi-agent architecture:

- **Research Manager**: Central orchestrator managing the research pipeline
- **Planner Agent**: Creates strategic search plans from user queries
- **Search Agent**: Executes web searches and summarizes findings
- **Writer Agent**: Synthesizes all research into comprehensive reports
- **Email Agent**: Handles automated delivery of completed reports

For detailed architecture information, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Project Structure

```
deep_research/
├── src/deep_research/     # Main source code
│   ├── __init__.py
│   ├── deep_research.py   # Gradio web interface
│   ├── research_manager.py # Main orchestrator
│   ├── planner_agent.py   # Search planning
│   ├── search_agent.py    # Web searching
│   ├── writer_agent.py    # Report writing
│   └── email_agent.py     # Email delivery
├── examples/              # Usage examples
├── docs/                  # Documentation
├── tests/                 # Test files (future)
├── app.py                 # Main entry point
├── pyproject.toml        # Project configuration
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
└── README.md
```

## Installation

### Option 1: Quick Start
```bash
git clone https://github.com/yourusername/deep_research.git
cd deep_research
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python app.py
```

### Option 2: Development Setup
```bash
git clone https://github.com/yourusername/deep_research.git
cd deep_research
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
cp .env.example .env
# Edit .env with your API keys
python app.py
```

## Environment Variables

Create a `.env` file with the following variables:

```
OPENAI_API_KEY=your_openai_api_key_here
# Add other required API keys based on your agents configuration
```

## Usage

### Web Interface
1. Run `python app.py`
2. Open the Gradio interface in your browser
3. Enter your research query
4. Monitor real-time progress updates
5. View the comprehensive report

### Programmatic Usage
```python
from src.deep_research import ResearchManager

async def research_example():
    manager = ResearchManager()
    async for update in manager.run("your research query"):
        print(update)
```

### Examples
Check the `examples/` directory for more usage patterns:
- `examples/basic_research.py` - Simple programmatic usage
- `examples/README.md` - Detailed examples guide

## Example Queries

- "What are the latest developments in quantum computing?"
- "Analyze the current state of renewable energy adoption globally"
- "Compare different approaches to machine learning interpretability"

## Learning Objectives

This project is designed as an educational resource demonstrating:

### Core Concepts
- **Multi-agent system architecture** - How specialized agents coordinate
- **Async/await patterns** - Non-blocking concurrent programming
- **Pipeline design** - Data flow through processing stages
- **Error handling** - Graceful degradation and recovery

### Technical Skills
- **Python packaging** - Modern project structure with pyproject.toml
- **API integration** - Working with OpenAI and web search APIs
- **Web interfaces** - Interactive UIs with Gradio
- **Type safety** - Using Pydantic for data validation

### Software Engineering
- **Clean architecture** - Separation of concerns and modularity
- **Documentation** - Comprehensive project documentation
- **Testing strategies** - Unit and integration testing approaches
- **Open source practices** - Contributing guidelines and project management

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Setting up the development environment
- Code style and standards
- Adding new agents or features
- Testing procedures
- Pull request process

## License

MIT License - see LICENSE file for details.

## Acknowledgments

Built with:
- [OpenAI GPT Models](https://openai.com/) - AI agent capabilities
- [Gradio](https://gradio.app/) - Web interface framework
- [Pydantic](https://pydantic.dev/) - Data validation and settings
- [Agents Framework](https://github.com/gpt-agents/agents) - Agent orchestration