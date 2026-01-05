# OCI Cost Tool v0.1

A Python-based utility to process and analyze Oracle Cloud Infrastructure (OCI) cost data. This tool helps transform raw cost reports into actionable insights.

## Prerequisites

- **OCI Credentials**: Ensure you have your OCI CLI configured (`~/.oci/config`) or have your API keys ready.
- **uv**: This project uses `uv` for extremely fast Python package and environment management.

## Getting Started

#### Step 1. Install uv
If you don't have `uv` installed yet, run:
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Step 2: Clone the Repository 

```bash
git clone https://github.com/vbabulal/oci-cost-tool.git
cd oci-cost-tool
```

#### Step 3: Setup Isolated Environment
You don't need to manually create virtual environments. uv handles this automatically. Simply run:
```bash
# Sync dependencies and create a virtual environment (.venv)
uv sync
```

#### Step 4: Run the Tool
To run the script within the isolated environment created by uv:
```bash
uv run oci_cost_manager.py
```

## Summary of what just happened

1. **Isolation:** All libraries (`oci`, `tabulate`) are inside the `.venv` folder in your project directory. Nothing was installed in your global Mac system.
2. **Ease of use:** You didn't have to manually `source .venv/bin/activate`. `uv run` handles the context switching for you.
3. **Cleanup:** To delete everything, you just delete the `oci-cost-tool` folder. Except for `uv`, there will be no leftover files on your Mac.


## Development
Adding Dependencies
If you need to add new libraries (like pandas or requests):
```bash
uv add pandas
```


## Python Version
This project is pinned to Python 3.12+. If you have a different version, `uv` will automatically download the correct one for this project without affecting your system Python.
