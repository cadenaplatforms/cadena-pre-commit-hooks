[![build status](https://github.com/cadenaplatforms/cadena-pre-commit-hooks/actions/workflows/main.yml/badge.svg)](https://github.com/cadenaplatforms/cadena-pre-commit-hooks/actions/workflows/main.yml)

cadena-pre-commit-hooks
=======================

Additional hooks for pre-commit.

See also:
* https://github.com/pre-commit/pre-commit
* https://github.com/pre-commit/pre-commit-hooks


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/cadenaplatforms/cadena-pre-commit-hooks
    rev: v5.0.0  # Use the ref you want to point at
    hooks:
    -   id: check-requirements-txt-contains-version
    # -   id: ...
```

### Hooks available

#### `check-requirements-txt-contains-version`
Ensure requirements.txt files uses only pinned versions.
This avoids reproducibility issues.
