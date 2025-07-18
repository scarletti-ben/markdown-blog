---
title: "Typescript Without Compiler"
date: "2025-07-15"
last_modified_at: "2025-07-18"
# description: ""
categories: [
  miscellaneous
]
tags: [
  coding, dev, webdev, javascript, typescript, .ts, .d.ts, type checking, typehints, type hinting, intellisense, vscode
]
---

# Typescript Without Compiler

## Typescript in a Flat Directory
For a flat directory, the layout would be as below
```text
root/
├── index.js
├── jsconfig.json
└── types.d.ts
```

The `jsconfig.json` file is used to influence how `JavaScript` interacts with `.d.ts` files, and in what folders to look, as seen below
```json
{
    "compilerOptions": {
        "checkJs": true
    },
    "include": ["./"]
}
```

The `checkJs` field allows for vanilla `.js` files to warn about type errors, and to use `.d.ts` type checking. The `include` field tells `IntelliSense` (and the compiler) which files to process, here we just said all files in the current directory.

The `.d.ts` file is a special `.ts` file that contains no executable code, and only contains type declarations, as seen below
```ts
type CustomType = {
    name: string;
    age: number;
}
```

I cannot be sure if `// @ts-check` is absolutely required, when coupled with `jsconfig.json` but it certainly *works* when it is added to the top of your `.js` file, and allows for type checking to read types from your `.d.ts` file
```javascript
// @ts-check

/** @type {CustomType} */
const obj = { name: "Bon", age: 99}

obj.name
```

## Moving `types.d.ts` to a Folder

For a foldered directory, the layout would be as below
```text
root/
├── types/
│   └── types.d.ts
│
├── index.js
└── jsconfig.json
```

The `jsconfig.json` file would be something like the code block below, where `"typeRoots": ["./types"]` has been added for the newly added `types` folder
```json
{
    "compilerOptions": {
        "checkJs": true,
        "typeRoots": ["./types"]
    },
    "include": ["./"]
}
```

## Using External TypeScript Files for CDN
When using a `CDN` version of a script, you lose some of the benefits of having the file locally, namely the type hints. Many of these `CND` links in the format `thing.js` also have an associated `thing.d.ts` file. Using something like the above can allow you to make use of type hints for `thing`.

One thing to note is that `TypeScript` can also be modular, just like `JavaScript`. This means that the `export` keyword is used, and the types within the `.d.ts` files are not global, and you would need to import them to use in `jsdoc` eg. `/** @type {import('./types').MyType} */`.

One way to make these type declarations global is to have a `global.d.ts` file that imports and exposes certain types from `thing.d.ts`.

Below is an example for a `Pyodide` project that uses `Pyodide` via `CDN`, either in `index.html` or as a dynamic import in `script.js`, and uses `pyodide.d.ts` to get the `PyodideInterface` type to assign in `const pyodide = await loadPyodide()`
```text
root/
├── types/
│   ├── global.d.ts
│   └── pyodide.d.ts
│
├── icon.png
├── index.html
├── jsconfig.json
├── script.js
└── style.css
```

The `PyodideInterface` type is not made global via `pyodide.d.ts` so it is handled via `global.d.ts`. The file also defines expected properties of `window`, namely `loadPyodide` which is added when the `CDN` script is imported
```typescript
declare global {
  interface Window {
    loadPyodide?: () => Promise<PyodideInterface>;
  }
  type PyodideInterface = import('./pyodide').PyodideInterface;
}
```

# Miscellaneous
- By default, `IntelliSense` searches in `node_modules/@types` for `.d.ts` files
- You can likely find `.d.ts` files for `CDN` installations, so you can get type checking without the original `.js` file being in your local development environment