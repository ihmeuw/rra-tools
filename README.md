# RRA Tools

[![PyPI](https://img.shields.io/pypi/v/rra-tools?style=flat-square)](https://pypi.python.org/pypi/rra-tools/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rra-tools?style=flat-square)](https://pypi.python.org/pypi/rra-tools/)
[![PyPI - License](https://img.shields.io/pypi/l/rra-tools?style=flat-square)](https://pypi.python.org/pypi/rra-tools/)

---

**Documentation**: [https://collijk.github.io/rra-tools](https://collijk.github.io/rra-tools)

**Source Code**: [https://github.com/collijk/rra-tools](https://github.com/collijk/rra-tools)

**PyPI**: [https://pypi.org/project/rra-tools/](https://pypi.org/project/rra-tools/)

---

Common utilities for IHME Rapid Response team pipelines.

#### Translation

The `translate` module provides functions to translate text files from one
language to another.


```python
from rra_tools.translate import translate_text_file

translate_text_file("path/to/input.txt", "path/to/output.txt")
```

By default, it will attempt to autodetect the language in the input file and produce
outputs in English, but you can specify the source and target languages:

```python
from rra_tools.translate import translate_text_file
# Translate from German to Spanish
translate_text_file(
    "path/to/input.txt",
    "path/to/output.txt",
    source_language="de",
    target_language="es",
)
```

The `translate` subpackage can also translate dataframe columns

```python
import pandas as pd
from rra_tools.translate import translate_dataframe

df = pd.DataFrame({"text": ["hola", "mundo"]})
translated_df = translate_dataframe(df, columns=["text"])
```


---

## Installation

```sh
pip install rra-tools
```

## Development

Instructions using conda:

1. Clone this repository.

    Over ssh:
    ```sh
    git clone git@github.com:ihmeuw/climate-downscale.git
    ```

    Over https:
    ```sh
    git clone https://github.com/ihmeuw/climate-downscale.git
    ```

2. Create a new conda environment.

    ```sh
    conda create -n climate-downscale python=3.10
    conda activate climate-downscale
    ```

3. Install `poetry` and the project dependencies.

    ```sh
    conda install poetry
    poetry install
    ```

### Documentation

The documentation is automatically generated from the content of the `docs` directory and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/collijk/rra-tools/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/collijk/rra-tools/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/collijk/rra-tools/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatting (`ruff format`), linters (e.g. `ruff` and `mypy`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
poetry run pre-commit run --all-files
```
