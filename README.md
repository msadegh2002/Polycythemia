# Polycythemias

An illustrated hematology presentation for Zeinab Eftekhar, built with [Slidev](https://sli.dev/). It contains **36 slides and 64 slide/reveal states**, including editable diagrams, enlarged table reading views, and authentic microscopy.

The source medical content and numerical values are preserved from the original 28-slide presentation. Clinical questions retained for the presenter are recorded in [CONTENT-REVIEW.md](CONTENT-REVIEW.md).

## Set up on another computer

Install **Node.js 24 LTS** and Git, then run:

```sh
git clone https://github.com/msadegh2002/Polycythemia.git
cd Polycythemia
npm ci
npm run dev
```

`npm ci` uses the committed dependency lockfile and restores the four microscopy images locally. Initial setup needs internet access. After setup, presenting uses bundled local assets.

Open the slideshow address printed in the terminal. Slidev automatically chooses an available port. On Windows, you can also double-click **Start-Presentation.cmd** after setup. Keep the terminal open while presenting; Ctrl+C stops the server.

If setup was run with `--ignore-scripts`, restore the images explicitly with `npm run assets:fetch`.

## Presentation controls

| Key | Action |
| --- | --- |
| Space / Right | Next reveal or slide |
| Left | Previous reveal or slide |
| F | Fullscreen |
| O | Overview |
| P | Presenter mode |

Reduced-motion preferences are respected. Teaching sequences are controlled by the presenter and settle after each step.

- Slides **3, 6, 12, 17, 23, and 24** contain staged mechanisms and diagrams.
- Slide **20** has a full differential-table overview followed by six enlarged reading views.
- Slides **25 and 34** focus on diagnostic criteria and treatment groups.
- Slides **28, 29, and 31** show dedicated microscopy; slide **30** retains the marrow differential comparison.

## Commands

| Command | Purpose |
| --- | --- |
| `npm run dev` | Start the editable presentation |
| `npm run build` | Generate the static application in `dist/` |
| `npm run preview` | Serve the static build locally |
| `npm run assets:fetch` | Restore missing microscopy images |
| `npm run assets:check` | Verify the four images against their recorded originals |
| `npm run verify -- <slideshow-url>` | Check content, layouts, navigation, and motion |
| `npm run review:package` | Build a portable Windows review ZIP |

Static builds must be served over HTTP; opening `dist/index.html` directly is insufficient. Builds, exports, review packages, and installed dependencies are generated locally and are excluded from Git.

The visual verification script uses Microsoft Edge on Windows by default. Set `PLAYWRIGHT_EXECUTABLE_PATH` for another installed Chromium browser. Screenshots and reports are written to the ignored `.qa/` folder. The GitHub Actions workflow checks installation, image restoration, and compilation without publishing the build.

## Send a review copy

On **64-bit Windows**, with Python 3 also installed, run:

```sh
npm run review:package
```

This creates **Polycythemia-Review.zip** beside the repository folder. Send that ZIP privately. The recipient chooses **Extract All**, then double-clicks **Open Presentation.cmd**. The complete animated presentation opens in their browser without installing Slidev or Node.js, entering commands, or connecting to the internet.

Keep the extracted files together. Closing the presentation tab stops the local viewer. The ZIP includes its portable runtime and third-party notices; it does not include the editable authoring project.

## Project structure and editing

| Location | Contents |
| --- | --- |
| `slides.md` | Editable slide content |
| `style.css` | Shared clinical typography and layout |
| `components/`, `composables/` | Diagrams, motion, microscopy, and reading views |
| `slide-manifest.json` | Stable slide IDs, source references, chapters, and reveal counts |
| `public/art/`, `public/fonts/` | Bundled artwork, provenance, and font files |
| `reference/` | Extracted source text, content maps, original references, and asset checksums |
| `scripts/` | Authoring, asset maintenance, packaging, and verification tools |

The extracted reference material needed to reproduce the deck is committed. The original PowerPoint is kept separately and is not required to run or build the presentation.

For generated authoring changes, update `scripts/author_deck.py` or `scripts/illustrated_edition.py`, then run `python scripts/author_deck.py`. This replaces direct edits to `slides.md` and regenerates the manifest and source map. Read [CONTRIBUTING.md](CONTRIBUTING.md) before making medical-content changes.

Artwork is already included. Optional Servier maintenance uses Python with Pillow; re-exporting the original vector groups uses PowerPoint on Windows. These tools are not needed for normal presentation or builds.

The `floating-vue` override in `package.json` preserves compatibility with Slidev 53's Twoslash integration. Keep it until the upstream integration supports the newer component structure.

## Assets and permissions

See [ASSET-CREDITS.md](ASSET-CREDITS.md) and [LICENSE.md](LICENSE.md) for attribution, sources, and applicable permissions.

- Servier illustrations and their original kits are included with CC BY 4.0 attribution.
- Source Sans 3 is bundled with its SIL Open Font License.
- **ASH microscopy image files are excluded from this public repository.** Setup downloads the recorded originals locally for the permitted informational, personal, or classroom use. Checksums are recorded in `reference/microscopy-assets.json`.
- Public posting or redistribution of ASH material requires the appropriate permission under [ASH's terms](https://imagebank.hematology.org/permissions). This repository does not deploy a public slideshow or publish image-containing builds and review ZIPs.

## Recovery

Git history provides a portable record of committed versions. The earlier complete rollback snapshot on the original authoring computer remains in the sibling `Polycythemia-backups/` folder, with restoration instructions. That local snapshot is intentionally outside this repository.
