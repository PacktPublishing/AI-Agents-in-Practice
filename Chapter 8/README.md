## Getting Started with MCP in Your Python Project

These instructions are adapted from the original GitHub MCP Python SDK Repository: [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk).

We will use [**uv**](https://github.com/astral-sh/uv) to manage your Python projects for a streamlined and reproducible setup.

### 1. Initialize a New uv-Managed Project

If you're starting fresh, initialize a new project:

```bash
uv init mcp-server-demo
cd mcp-server-demo
```
You can then copy the `server.py` file in your new project.

### 2. Add MCP to Your Project
Add the MCP package, including the CLI tools, as a dependency:

```bash
uv add "mcp[cli]"
```

### 3. Run the MCP Development Tools
To use the MCP CLI with uv:

```bash
uv run mcp
```

### 3. Interact with the Tool
If you have [Claude Desktop](https://claude.ai/download), you can start interacting with the tool from the UI by running the following command:

```bash
uv mcp install server.py
```
You can follow this [tutorial](https://modelcontextprotocol.io/quickstart/user) for a step by step initialziation.

Alternatively, you can test it with the MCP Inspector:

```bash
uv mcp dev server.py
```