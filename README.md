# Polycythemia

An illustrated hematology presentation built with [Slidev](https://sli.dev/), prepared for Zeinab Eftekhar. The 36-slide deck includes animated diagrams, enlarged clinical tables, and microscopy images.

## Run the presentation

Install **Node.js 24** and **Git**, then open a terminal and run:

```sh
git clone https://github.com/msadegh2002/Polycythemia.git
cd Polycythemia
npm ci
npm run dev
```

Setup needs an internet connection and automatically downloads the microscopy images. Open the slideshow address printed in the terminal; an available port is selected automatically. After setup on Windows, you can also double-click **Start-Presentation.cmd**.

Use **Space / Right** to advance and **Left** to go back. Keep the terminal open while presenting.

## Edit or share

- Edit slide content in `slides.md`; shared styling is in `style.css` and interactive figures are in `components/`.
- Run `npm run build` to create a static build, then `npm run preview` to view it.
- For a Windows review copy with animations and no installation required for the recipient, follow [Send a review copy](SETUP.md#send-a-review-copy).

See [SETUP.md](SETUP.md) for detailed instructions and [CONTRIBUTING.md](CONTRIBUTING.md) for the authoring workflow. Artwork sources and usage terms are recorded in [ASSET-CREDITS.md](ASSET-CREDITS.md) and [LICENSE.md](LICENSE.md).
