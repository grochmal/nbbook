README for `nbbook`

[![Build Status][tr_build]][tr_link]
[![Test Coverage][cv_build]][cv_link]

[tr_build]: https://travis-ci.org/grochmal/nbbook.svg?branch=master
[tr_link]: https://travis-ci.org/grochmal/nbbook "Travis CI"
[cv_build]: https://codecov.io/gh/grochmal/nbbook/branch/master/graph/badge.svg
[cv_link]: https://codecov.io/gh/nbbook "CodeCov"


## Introduction

Export groups of jupyter notebooks as a full Book.

Command line usage:

    nbbook [-nv] [-c config] [-r outdir] [html|latex] <defs.yaml>
    nbbook [-nv] [-c config] [-o output] [html|latex] <notebook.ipynb>

`nbbook` will produce a full book based on definitions in `defs.yaml`
or a single notebook export (similar to `nbconvert`) from `notebook.ipynb`.
`nbbook` calls `nbconvert` behind the scenes, therefore one can configure
`nbconvert` to preprocess the notebooks.


## Copying

Copyright (C) 2019 Michal Grochmal

This file is part of `manaeng`.

`nbbook` is free software; you can redistribute and/or modify all or parts of
it under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3 of the License, or (at your option) any
later version.

`nbbook` is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

The COPYING file contains a copy of the GNU General Public License.  If you
cannot find this file, see <http://www.gnu.org/licenses/>.

