# macos-surgery

Various personal macOS things.

This project is managed with [Hatch](https://hatch.pypa.io/latest/) and uses `uv` for faster dependency management within Hatch environments where possible. It incorporates modern Python development practices, including linting with [Ruff](https://beta.ruff.rs/docs/), type checking with [Mypy](http://mypy-lang.org/), testing with [Pytest](https://docs.pytest.org/), and pre-commit hooks.

## Project Structure

```
.
├── .github/workflows/        # GitHub Actions CI/CD workflows
│   └── ci.yml
├── .gitignore                # Standard Python .gitignore
├── .pre-commit-config.yaml   # Configuration for pre-commit hooks
├── LICENSE                   # Project license (TODO: Verify/Choose a license)
├── README.md                 # This file
├── pyproject.toml            # Project metadata, dependencies, and tool configurations (Hatch, Ruff, Mypy, Pytest)
├── setup-macos-in-vmware.sh  # Original script (TODO: Integrate or update as needed)
├── src/                      # Source code
│   └── macos_surgery/
│       ├── __init__.py
│       └── example.py        # Example module
└── tests/                    # Test files
    ├── __init__.py
    └── test_example.py       # Tests for the example module
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Git](https://git-scm.com/)
- [Hatch](https://hatch.pypa.io/latest/install/):
  ```bash
  pip install hatch
  ```
  It's also recommended to install `uv` for faster operations, which Hatch can sometimes leverage:
  ```bash
  pip install uv
  ```
  (Note: `uv` is also listed as a dev dependency in `pyproject.toml`, so `hatch env create default` will install it into the project's virtual environment.)


### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/example-user/macos-surgery.git # TODO: Update with actual URL
    cd macos-surgery
    ```

2.  **Create the Hatch environment:**
    This will create a virtual environment and install all dependencies defined in `pyproject.toml` (including development dependencies like Ruff, Mypy, Pytest, and pre-commit).
    ```bash
    hatch env create default
    ```
    If you prefer to use `uv` explicitly for faster environment setup after installing `hatch` and `uv` globally:
    ```bash
    # Ensure hatch is configured to use uv if desired (this might require global uv setup or future Hatch features)
    # For now, hatch env create will use its default installer (pip or uv if it detects and prefers it)
    ```

3.  **Activate the Hatch environment:**
    To work within the project's isolated environment:
    ```bash
    hatch shell
    ```
    You are now inside the virtual environment with all dependencies available.

4.  **Install pre-commit hooks (recommended):**
    To ensure code quality checks are run before each commit:
    ```bash
    # Ensure you are inside the hatch shell or have pre-commit available in your PATH
    pre-commit install
    ```

## Development

### Running QA Checks and Tests

The following tools are configured:

-   **Ruff**: For linting and formatting.
-   **Mypy**: For static type checking.
-   **Pytest**: For running unit tests.

You can run these checks using Hatch scripts (defined in `pyproject.toml`). Activate the Hatch shell (`hatch shell`) first.

-   **Lint and Format:**
    ```bash
    hatch run lint
    # Or directly:
    # hatch run ruff check .
    # hatch run ruff format .
    ```

-   **Type Check:**
    ```bash
    hatch run check
    # Or directly:
    # hatch run mypy src tests
    ```

-   **Run Tests:**
    ```bash
    hatch run test
    # Or directly:
    # hatch run pytest -v
    ```

-   **Run Tests with Coverage:**
    ```bash
    hatch run cov
    # Or directly:
    # hatch run pytest -v --cov=src/macos_surgery --cov-report=term-missing
    ```

-   **Run All Checks (Lint, Test with Coverage, Type Check):**
    ```bash
    hatch run all-checks
    ```
    *(Note: If `hatch run <script_name>` gives an error like "script not found", it might be due to the Hatch version or environment. In such cases, use the direct commands shown above, e.g., `hatch run ruff check .` instead of `hatch run lint`.)*

### Building the Package

To build the wheel and source distribution:
```bash
hatch build
```
Artifacts will be in the `dist/` directory.

### Versioning

This project uses `hatch-vcs` for versioning based on Git tags. Versions are automatically derived from tags like `v0.1.0` or `1.0.0`.

## TODO

-   **Verify License**: The `LICENSE` file and `pyproject.toml` currently assume MIT. Please verify and update if necessary.
-   **Author Information**: Update placeholder author name and email in `pyproject.toml`.
-   **Repository URL**: Update placeholder repository URLs in `pyproject.toml` and this README.
-   **`setup-macos-in-vmware.sh`**: Review this original script. Decide if it should be integrated into the Python package, updated, or kept separate. Its functionality is not currently part of the Python package structure.
-   **Codecov Token**: If using Codecov for private repositories or for guaranteed uploads, set the `CODECOV_TOKEN` secret in your GitHub repository settings for the CI workflow.

## Contributing

Contributions are welcome! Please ensure that your code adheres to the linting and formatting standards (enforced by pre-commit hooks and CI) and that all tests pass.
```
