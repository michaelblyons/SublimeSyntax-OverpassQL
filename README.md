# Overpass Query Language Syntax

[Overpass QL][opql] is a language
for retrieving results
from [OpenStreetMap][osm]'s Overpass API.
This project is a WIP syntax highlighter
for OverpassQL syntax
in [Sublime Text][st].


## Status

### Build system

- Send query to Overpass in browser

### Language syntax

- Support for basic query statements
- Support for logical block statements
- Support for literals
    * Naive support for regular expression string after `~` and `!~`
- Support for operators
- Support for functions
- Support for flow control
- Modest support for sets
- Minimal support for settings
- Naive support for styles (delegates to CSS)


## To-do

### Build system

- Send query to Overpass API

### Language syntax

- Support intersection
- Better scopes for `out` clauses


[opql]: https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
[osm]: https://osm.org
[st]: https://www.sublimetext.com
