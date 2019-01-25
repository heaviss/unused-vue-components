# Made of shit, sticks and regexes

If you import component, use it in `components` but don't use in template, ESLint won't see this. That's why this script exists.

It will live until eslint can do it for us.

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
