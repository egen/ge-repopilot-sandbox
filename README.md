# ge-repopilot-sandbox

Sandbox repository for testing **RepoPilot**, a Gemini Enterprise agent that works through the GitHub connector.

Everything here is synthetic test content. Issues, comments, branches and releases may be created by the agent.

## What's inside

- `src/calc/` – a tiny calculator library (with one planted bug)
- `tests/` – unit tests run by CI
- `docs/setup.md` – setup notes (with one planted typo)
- `.github/workflows/ci.yml` – CI, runnable on demand

## Run the tests

```bash
pip install pytest
pytest -q
```
