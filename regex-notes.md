## Methods

- `match(`regex`, `string`)`: matches the beginning of the string
- `search(`regex`, `string`)`: search through the string
- `findall(`regex`, `string`)`: find all substrings, return as a list
- `finditer(`regex`, `string`)`: return as an iterator
- `re.split(`regex`, `string`)`: split the str into list wherever RE matches
- `re.sub(`regex`, `replacement`, `string`)`: replace all matches
- `subn(`regex`, `replacement`, `string`)`: returns the new string and the number of replacements

## Match object

- `m.group()`: return the string matched by RE
- `m.start()`: return the starting position of the match
- `m.end()`: return the ending position
- `m.span()`: a tuple of (start, end)
