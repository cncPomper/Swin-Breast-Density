# Swin-Breast-Density


## Requirement uv

```bash
pip install uv
```

### Then

```bash
uv sync
```

### Windows
```
source .venv/Script/activate
```
### Linux
```
source .venv/bin/activate
```

## Notebook

### Create project
```bash
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

### Run notebooks
```bash
uv run --with jupyter jupyter lab
```
