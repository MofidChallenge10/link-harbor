<div align="center">

<img src="assets/hero.svg" alt="Link Harbor animated illustration" width="100%"/>

# Link Harbor

**A quick local checker for relative links in Markdown documentation.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-2F855A.svg)](LICENSE)

</div>

## Why it exists

Find broken local links before readers hit a dead end. Checks local file targets referenced by Markdown links and images. External HTTP links are skipped; heading-fragment existence is not validated.

## Features

- Relative links and image targets
- Line-numbered findings
- External, mail and fragment links skipped
- CI-friendly exit code for broken local targets

## Quick start

Python 3.10+; no third-party packages.

```bash
git clone https://github.com/MofidChallenge10/link-harbor.git
cd link-harbor
python tool.py --help
```

### Example

```bash
python tool.py README.md docs/**/*.md
```

## Self-test

```bash
python tool.py --self-test
```

The self-test uses the standard-library `unittest` module and does not contact external services.

## Scope and safety

Checks local file targets referenced by Markdown links and images. External HTTP links are skipped; heading-fragment existence is not validated. Review output before using it in production workflows.

## Design notes

The illustration is an original lightweight SVG. Its motion is decorative only and respects `prefers-reduced-motion`; the CLI itself stays plain and pipe-friendly.

## Contributing

Issues and pull requests are welcome. Keep the standard-library-first approach, add focused tests for behavior changes, and update examples when options change.

## License

MIT — see [LICENSE](LICENSE).
