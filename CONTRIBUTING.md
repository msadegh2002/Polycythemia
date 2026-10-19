# Contributing

Use Node.js 24 and npm. Run `npm ci`, then `npm run dev`. Setup restores the locally used ASH microscopy images; those image files must remain outside Git.

## Content and authoring

- Preserve source medical statements, numerical values, thresholds, tables, footnotes, and qualifications. Record unresolved clinical questions in `CONTENT-REVIEW.md`.
- `slides.md` is directly editable. Shared formatting is in `style.css`, and diagrams and reading views are Vue components.
- For reproducible generated changes, update `scripts/author_deck.py` or `scripts/illustrated_edition.py` and run `python scripts/author_deck.py`. Regeneration replaces direct edits to `slides.md`.
- Keep `slide-manifest.json` and `reference/CONTENT-MAP.md` consistent with slide order, source references, and reveal counts.
- Preserve image proportions, watermarks, and attribution. Keep additional assets local and document their sources and permissions.

## Before committing

Run `npm run assets:check` and `npm run build`. For visual or interaction changes, start the deck and run `npm run verify -- <slideshow-url>` using Microsoft Edge on Windows, or set `PLAYWRIGHT_EXECUTABLE_PATH` to a compatible installed Chromium browser.

Inspect the affected slides and reveal states, including forward/back navigation and reduced motion. Screenshots and reports belong in `.qa/`, which is ignored by Git. Do not commit `node_modules`, generated builds, portable ZIPs, runtime executables, local backups, secrets, or ASH image files.

CI checks installation, local asset restoration, and compilation. It does not publish the presentation or replace visual inspection.
