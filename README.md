# Made of shit, sticks and regexes

This is a toy script to find components that are imported, used in `components` but aren't used in template.

Just for fun and learning.

Use [eslint-plugin-vue v5](https://github.com/vuejs/eslint-plugin-vue/releases/tag/v5.0.0-beta.3) when it leaves beta

## Install
```
pip install unused-vue-components
```

## Use
```
find_unused_components.py PATH_TO_SOURCES
```

## Packaging

Draft a new github release with tag starting with `v-`, like `v-1.0.1`.
