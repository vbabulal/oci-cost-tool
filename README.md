
---

### Setup Guide: Using `uv` for Isolation


#### Step 1: Install `uv`

On your Mac, open your terminal and run:

```bash
# Using Homebrew (Recommended)
brew install uv

# OR using curl if you don't have brew
curl -LsSf https://astral.sh/uv/install.sh | sh

```

#### Step 2: Initialize the Project

Navigate to the folder where you saved `oci_cost_manager.py`.

```bash
# 1. Initialize a new project
uv init oci-cost-tool

# 2. Enter the directory
cd oci-cost-tool

# 3. Create your script into this folder, using your favorite editor: 
vim oci_cost_manager.py

```

#### Step 3: Create Environment & Install Dependencies

`uv` makes this very simple. You don't need to manually create a venv; `uv` handles it when you run commands or add packages.

```bash
# This creates a virtual env at .venv and installs the packages into it
uv add oci tabulate

```

*Note: If you don't have Python installed on your system at all, `uv` will automatically download a managed Python version for this project to use, keeping your system completely untouched.*

#### Step 4: Run the Script

You can run the script using `uv run`. This automatically detects the virtual environment and uses the isolated Python and packages.

```bash
uv run oci_cost_manager.py

```

### Summary of what just happened

1. **Isolation:** All libraries (`oci`, `tabulate`) are inside the `.venv` folder in your project directory. Nothing was installed in your global Mac system.
2. **Ease of use:** You didn't have to manually `source .venv/bin/activate`. `uv run` handles the context switching for you.
3. **Cleanup:** To delete everything, you just delete the `oci-cost-tool` folder. No leftover files on your Mac.
