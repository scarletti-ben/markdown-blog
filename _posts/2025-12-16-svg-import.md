---
title: "Importing SVG Into Sites via HTML / JavaScript"
date: "2025-12-16"
# description: ""
categories: [
  webdev
]
tags: [
  html, javascript, css, svg, spritesheet
]
---

# Old Version of Importing SVG
Previously I was under the impression that the only functional way to have a `.svg` file accessible as a spritesheet was via something similar to the code below

```javascript
/** 
 * Fetch `.svg` file from URL as an `<svg>` spritesheet element
 * - Automatically appends `<svg>` to body, and hides it
 * 
 * @param {string} url The URL for the `.svg` file
 * @returns {Promise<SVGElement>} Promise of the `<svg>` element
 * @throws For an unsuccessful fetch
 */
async function fetchSpritesheet(url) {
    const svg = await fetchSVGElement(url, true);
    svg.style.display = 'none';
    document.body.append(svg);
    return svg;
}

/** 
 * Create an `<svg>` sprite from a given symbol id
 * - Requires a pre-loaded `<svg>` spritesheet in the DOM (eg. via `fetchSpritesheet`)
 * 
 * @param {string} id The symbol id from the pre-loaded spritesheet
 * @returns {SVGElement} The `<svg>` sprite element
 */
function createSprite(id) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttributeNS('http://www.w3.org/1999/xlink', 'href', `#${id}`);
    svg.appendChild(use);
    return svg;
}

await fetchSpritesheet('https://example.com/file.svg');
const container = document.getElementById('container');
const sprite = createSprite('test');
sprite.classList.add('sprite');
container.appendChild(sprite);

```

In the example, the `.svg` file is loaded as hidden `<svg>` element into the `DOM`, and references are made via the `<use>` tag in the format below

```html
<svg>
  <use href="#save"></use>
</svg>
```

The `href="#save"` references an icon from the loaded `.svg` file. An abridged version can be seen below where `save` matches a `<symbol>` id

```html
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <symbol id="save" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
      stroke-linejoin="round">
      <path d="M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8a2 2 0 0 1 .6 1.4V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z">
      </path>
      <path d="M17 21v-7a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v7"></path>
      <path d="M7 3v4a1 1 0 0 0 1 1h7"></path>
    </symbol>
  </defs>
</svg>
```

# New Version of Importing SVG
It turns out you can make direct reference to a `.svg` file and id, without adding it to the `DOM`. I was aware of this feature but seemed to have issues in certain use cases at the time, which I cannot remember, and so stopped using the method

```html
<button id="save-button" title="Save">
  <svg>
    <use href="/assets/svg/lucide.svg#save"></use>
  </svg>
</button>
```