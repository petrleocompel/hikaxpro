# Agent instructions — hikaxpro

Python ISAPI wrapper for Hikvision AX Pro. Companion Home Assistant integration: [`petrleocompel/hikaxpro_hacs`](https://github.com/petrleocompel/hikaxpro_hacs).

Read this file at the start of any change to this project (or when releasing / syncing with HACS).

## Repos

| Repo | Role |
|---|---|
| `hikaxpro` (this) | Library published to PyPI (`hikaxpro`) |
| `hikaxpro_hacs` | HA custom component; pins this library in `custom_components/hikvision_axpro/manifest.json` → `requirements` |

## Commit messages

Conventional commits, lowercase type prefix, imperative subject:

- `feat: …` — new capability / endpoint / behaviour
- `fix: …` — bug fix
- `chore: release version X.Y.Z` — version bump only (see Release)
- `docs: …`, `test: …`, `refactor: …` as needed

One logical change per commit. Match existing history style (short subject, optional body explaining why).

## Changelog (this library)

Maintain root `CHANGELOG.md` in the same bullet style as HACS:

```markdown
## vX.Y.Z
- **fix**: short user-facing description (#issue if any)
- **feat**: …
```

- Add bullets under a new `## vX.Y.Z` header in the **same commit set** as the behavioural change (or in the release commit), never as an afterthought forgotten at the end.
- Prefer `**fix**` / `**feat**` / `**docs**` / `**chore**` markers like HACS `CHANGELOG.md`.

## Version bump (this library)

- Source of truth: `pyproject.toml` → `[project].version` (also `[tool.bumpver].current_version`).
- After user-facing fixes/features that should ship: bump patch/minor with bumpver (preferred) or edit both version fields together:

  ```bash
  bumpver update --patch   # or --minor / --major
  ```

- That produces `chore: release version X.Y.Z` and a git tag. Do **not** invent a different release commit message style.
- Do not bump version for pure docs/tests unless releasing anyway.

## Sync to HACS (required when the library version changes)

When this library gets a new published version that HACS should use, update `hikaxpro_hacs` in the same effort (clone sibling if needed):

1. `custom_components/hikvision_axpro/manifest.json`
   - bump integration `"version"` (semver; patch for dependency-only / small fixes)
   - set `"requirements"` pin to the new library, e.g. `"hikaxpro==X.Y.Z"`
2. Root `CHANGELOG.md` — new `## v…` section with bullets in HACS style, mentioning the library bump and the fixes/features users get.
3. Commit there with matching `fix:` / `feat:` / `chore:` messages.

Publish **this** package to PyPI (or confirm the version is available) before relying on the HACS pin in production.

If the change is library-only and HACS does not need a pin bump yet, say so explicitly to the user; do not silently skip the question when behaviour affects HA setup/auth/polling.

## Checklist before finishing a user-facing change

1. [ ] Commit message uses `feat:` / `fix:` / … style above
2. [ ] `CHANGELOG.md` (this repo) updated for the new version
3. [ ] Version bumped when the change should ship (`chore: release version …`)
4. [ ] If HACS consumers need it: HACS `manifest.json` pin + version + `CHANGELOG.md` updated (or user explicitly deferred)
5. [ ] Never commit secrets / local `src/dev.py` credentials

## Local notes

- Tests: `pytest` from a venv with `pip install -e '.[dev]'`
- Untracked `src/dev.py` is a local scratch file; leave it out of commits
