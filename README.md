# AI Coding Agent

A minimal AI-powered coding agent built with Python that can inspect files, read source code, execute Python scripts, and modify files to fix bugs.

## Features

- **List files:** Explore files and directories in the project.
- **Read files:** Inspect source code to understand existing implementations.
- **Run Python files:** Execute scripts with command-line arguments and inspect their output.
- **Write files:** Create or update source files to fix bugs.
- **Tool calling:** Use AI-generated function calls to perform coding tasks.

## Project Structure

```text
AI-agent/
├── main.py
├── call_function.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/
    ├── main.py
    └── pkg/
```

## Getting Started

Run the agent from the project root using `uv` (a fast Python package and project manager):

```bash
uv run main.py "Fix the bug in the calculator."
```

## How It Works

1. The user provides a coding task.
2. The AI analyzes the request and selects appropriate tools.
3. The agent executes tool calls to inspect or modify files.
4. Python scripts can be executed to check behavior.
5. The agent reports the results.

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/) (Python package and project manager)
- An appropriately configured AI model and API client

## Goal

Build a lightweight coding agent that can investigate code, fix bugs, and verify changes using a small set of Python tools.
