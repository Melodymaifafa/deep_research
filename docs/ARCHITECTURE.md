# Architecture Overview

This document provides a detailed overview of the Deep Research system architecture.

## System Overview

Deep Research is a multi-agent system designed to automatically conduct comprehensive research on any given topic. The system follows a pipeline architecture where different specialized agents handle distinct phases of the research process.

## Core Components

### 1. Research Manager (`research_manager.py`)
The central orchestrator that coordinates all agents and manages the research workflow.

**Key Responsibilities:**
- Orchestrates the entire research pipeline
- Manages async execution of agents
- Provides status updates to the UI
- Handles error recovery and retries

### 2. Planner Agent (`planner_agent.py`)
Analyzes the research query and creates a strategic search plan.

**Key Responsibilities:**
- Breaks down complex queries into searchable components
- Determines optimal search terms and strategies
- Prioritizes search areas based on relevance

**Output:** `WebSearchPlan` containing multiple `WebSearchItem` objects

### 3. Search Agent (`search_agent.py`)
Performs web searches and summarizes results.

**Key Responsibilities:**
- Executes web searches using provided search terms
- Summarizes search results into concise, relevant information
- Filters out irrelevant or low-quality content

**Input:** Search terms and reasoning
**Output:** Structured summaries of search results

### 4. Writer Agent (`writer_agent.py`)
Synthesizes all research findings into a comprehensive report.

**Key Responsibilities:**
- Analyzes all collected research data
- Structures findings into coherent sections
- Creates markdown-formatted reports
- Ensures accuracy and completeness

**Output:** `ReportData` with structured markdown report

### 5. Email Agent (`email_agent.py`)
Handles delivery of completed research reports.

**Key Responsibilities:**
- Formats reports for email delivery
- Sends reports to designated recipients
- Manages email templates and styling

## Data Flow

```
User Query → Planner Agent → Search Plan → Search Agent(s) → Writer Agent → Email Agent → Final Report
```

1. **Query Analysis**: User provides research topic
2. **Planning**: Planner agent creates search strategy
3. **Parallel Searching**: Multiple search agents work simultaneously
4. **Synthesis**: Writer agent combines all findings
5. **Delivery**: Email agent sends completed report

## Key Design Patterns

### Async/Await Pattern
All agents use async/await for non-blocking execution, allowing:
- Parallel search execution
- Real-time status updates
- Better resource utilization

### Agent Pattern
Each component is a specialized agent with:
- Clear responsibilities
- Defined input/output interfaces
- Independent execution capabilities

### Pipeline Pattern
Linear flow of data through processing stages:
- Each stage adds value to the research
- Clear separation of concerns
- Easy to debug and maintain

## Configuration

### Model Settings
- Default model: `gpt-4o-mini` (optimized for cost/performance)
- Configurable per agent
- Tool choice can be required or optional

### Search Configuration
- Configurable number of searches (default: 5)
- Adjustable search context size
- Timeout and retry mechanisms

## Error Handling

### Graceful Degradation
- Failed searches don't stop the entire process
- Partial results are still processed
- System continues with available data

### Retry Logic
- Automatic retries for transient failures
- Exponential backoff for rate limiting
- Circuit breaker pattern for persistent failures

## Scalability Considerations

### Horizontal Scaling
- Agents can be distributed across multiple processes
- Search operations are naturally parallelizable
- State is maintained in the Research Manager

### Performance Optimization
- Concurrent search execution
- Streaming responses for real-time updates
- Efficient memory usage with generators

## Security

### API Key Management
- Environment variable configuration
- No hardcoded credentials
- Secure key rotation support

### Content Filtering
- Input sanitization
- Output content validation
- Rate limiting and quota management