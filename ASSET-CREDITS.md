# Asset credits

## ASH microscopy

Images are downloaded directly from ASH Image Bank and stored unchanged. The slides do not crop, recolor, filter, or annotate the image pixels. Original watermarks remain; captions and credits sit beside the images.

### Peripheral blood, presentation slide 28

This image was originally published in ASH Image Bank. Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, peripheral blood. ASH Image Bank. 2015; image 60160. © the American Society of Hematology.

- Page: https://imagebank.hematology.org/image/60160/polycythemia-vera-pv-polycythemic-phase-peripheral-blood
- Download: https://imagebank.hematology.org/getimagebyid/60160?size=3
- Local original: `public/images/ash-60160.jpg`
- The image illustrates a PV case, not a claim that peripheral morphology alone establishes PV.

### Core biopsy 2, presentation slide 30

This image was originally published in ASH Image Bank. Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, core biopsy 2. ASH Image Bank. 2015; image 60162. © the American Society of Hematology.

- Page: https://imagebank.hematology.org/image/60162/polycythemia-vera-pv-polycythemic-phase-core-biopsy-2
- Download: https://imagebank.hematology.org/getimagebyid/60162?size=3
- Local original: `public/images/ash-60162.jpg`
- This illustrates PV. The adjacent ET/pre-PMF descriptions do not label these conditions within the PV micrograph.

### Core biopsy 1, presentation slide 29

This image was originally published in ASH Image Bank. Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, core biopsy 1. ASH Image Bank. 2015; image 60161. © the American Society of Hematology.

- Page: https://imagebank.hematology.org/image/60161/polycythemia-vera-pv-polycythemic-phase-core-biopsy-1
- Download: https://imagebank.hematology.org/getimagebyid/60161?size=3
- Local original: `public/images/ash-60161.jpg`

### Aspirate smear, presentation slide 31

This image was originally published in ASH Image Bank. Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, aspirate smear. ASH Image Bank. 2015; image 60164. © the American Society of Hematology.

- Page: https://imagebank.hematology.org/image/60164/polycythemia-vera-pv-polycythemic-phase-aspirate-smear
- Download: https://imagebank.hematology.org/getimagebyid/60164?size=3
- Local original: `public/images/ash-60164.jpg`

### Use

Terms: https://imagebank.hematology.org/permissions (checked 18 October 2026).

ASH permits credited, unmodified informational/noncommercial/personal use subject to its stated conditions and grants accredited institutions classroom distribution rights. Public/network posting and broadcast require separate permission. This deck is prepared for the user's confirmed local/classroom use; no public deployment is included. Read ASH's original terms for the full conditions.

The ASH image files are excluded from the public Git repository. `npm ci` restores the recorded originals locally through `scripts/fetch-microscopy.mjs`; `npm run assets:fetch` can repeat that step. Source URLs and SHA-256 checksums are committed in `reference/microscopy-assets.json`. Image-containing static builds, screenshots, and portable ZIPs are also excluded from Git.

The ASH-watermarked reference micrograph extracted from the original PowerPoint (`reference/source-images/image33.png`) remains archived locally and is also excluded from the public repository. It is not used by the Slidev presentation or required for generation.

## Font and favicon

Source Sans 3 variable upright, Adobe. SIL Open Font License 1.1.

- Source: https://github.com/adobe-fonts/source-sans
- Download: https://raw.githubusercontent.com/adobe-fonts/source-sans/release/WOFF2/VF/SourceSans3VF-Upright.ttf.woff2
- Local file: `public/fonts/SourceSans3VF.woff2`
- License: `public/fonts/OFL.txt`

The Slidev browser favicon is stored locally from https://cdn.jsdelivr.net/gh/slidevjs/slidev/assets/favicon.png . It is not used as slide artwork.

## Diagrams and supplied content

Editable diagrams illustrate statements in the supplied PowerPoint. Volume bars are schematic, not quantitative. No synthetic microscopy is used. Original reference citations have not been inferred or invented. See `CONTENT-REVIEW.md` for source inconsistencies retained for the presenter.

Blood-tube and cell artwork from the user-supplied PowerPoint remains archived in `public/art`. The medical-atlas edition uses the Servier illustrations below. New editable scientific diagrams are separate from authentic ASH microscopy. The existing locally installed VueUse Motion support is bundled with the build; no animation service is contacted while presenting.

## Servier Medical Art: medical-atlas edition

Illustrations from Servier Medical Art (https://smart.servier.com), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Attribution guidance: https://smart.servier.com/how-to-cite-servier-medical-art/ (checked 18 October 2026).

The deck displays concise attribution on every slide using these illustrations. Original grouped illustrations were exported from Servier's downloadable PPTX kits as SVG, keeping their vector geometry. They are scaled, arranged, rotated, and animated in the deck; original PNG previews and microscopy are not edited. The marrow structure, connectors, and diagram labels are editable presentation schematics, not diagnostic images or a quantitative model.

| Local SVG | Original Servier kit | Slide | Original illustration group |
|---|---|---|---|
| erythrocyte.svg | SMART-Blood-immunology.pptx | 4 | Group 844 |
| erythrocyte-oblique.svg | SMART-Blood-immunology.pptx | 4 | Group 809 |
| erythrocyte-front.svg | SMART-Blood-immunology.pptx | 4 | Group 833 |
| stem-cell.svg | SMART-Blood-immunology.pptx | 15 | Group 17 |
| neutrophil.svg | SMART-Blood-immunology.pptx | 8 | Group 711 |
| platelet.svg | SMART-Blood-immunology.pptx | 12 | Group 1208 |
| kidney.svg | SMART-Urinary-system.pptx | 4 | Group 3 |
| specimen.svg | SMART-Medical-equipment.pptx | 5 | Group 3 |

Original kits: https://smart.servier.com/wp-content/uploads/2016/10/SMART-Blood-immunology.pptx ; https://smart.servier.com/wp-content/uploads/2016/10/SMART-Urinary-system.pptx ; https://smart.servier.com/wp-content/uploads/2016/10/SMART-Medical-equipment.pptx .

Files are in `public/art/atlas`; exact source URLs, export provenance, and SHA-256 hashes are in `sources.json` and `vector-sources.json`. Original kits are bundled in `reference/servier-kits` for reproducibility. Illustrations show generic anatomy and cells, not patient specimens. Tube cap colors are not assigned to specific assays. The mixed marrow view has no implication about cell proportions.
