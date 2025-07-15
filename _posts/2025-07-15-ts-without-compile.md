---
title: "Typescript Without Compiler"
date: "2025-07-15"
# last_modified_at: "2025-07-15"
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

# Miscellaneous
- By default, `IntelliSense` searches in `node_modules/@types` for `.d.ts` files