# Overpass Query Language Syntax

[Overpass QL][opql] is a language
for retrieving results
from [OpenStreetMap][osm]'s Overpass API.
This project is a WIP syntax highlighter
for OverpassQL syntax
in [Sublime Text][st].


## Status

### Language syntax

- Support for basic query statements
- Support for logical block statements
- Minimal support for settings
- Minimal support for literals (currently just quoted strings)
- Naive support for styles (delegates to CSS)


## TODO

### Build system

- Send query to Overpass in browser
- Send query to Overpass API

### Language syntax

- Support more literals (numbers and dates; probably not unquoted strings)
- Support operators
- Support sets
- Support functions
- Support flow control
- Support intersection
- Better scopes for `out` clauses


[opql]: https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
[osm]: https://osm.org
[st]: https://www.sublimetext.com
