# Overpass Query Language Syntax

[Overpass QL][opql] is a language
for retrieving results
from [OpenStreetMap][osm]'s Overpass API.
This project is a syntax highlighter
for OverpassQL syntax
in [Sublime Text][st].

It should be compatible
with [bat][] and [delta][],
but this hasn't been tested.


## Installation

- This package is in Sublime Text's Package Control system.
  That's probably the easiest option,
  and it automatically updates.

- You can also install manually
  by cloning or symlinking this repository
  into the Packages directory
  for your ST installation.


## Status

### Build system

- Send query to Overpass in browser

### Language syntax

- Support for query statements
- Support for logical block statements
- Support for literals
    * Numbers
    * Dates
    * Quoted strings
        * Regular expression highlighting after `~` or `!~`
- Support for operators
- Support for functions
- Support for sets
- Some support for flow control
    * `if` statements
- Minimal support for settings
- Styles are delegated to CSS


## To-do

### Build system

- Send query to Overpass API

### Language syntax

- More support for block statements
    * `foreach`
    * `for`
    * `complete`
    * `retro`
    * `compare`
- Better support for standalone standments
    * `is_in`
    * `timeline`
    * `local`
    * `convert`
    * `make`
- Better scopes for `out` clauses


[opql]: https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
[osm]: https://osm.org
[st]: https://www.sublimetext.com
[bat]: https://github.com/sharkdp/bat
[delta]: https://dandavison.github.io/delta/
