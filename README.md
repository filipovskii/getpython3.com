### Building

    mkvirtualenv getpython3
    pip install blogofile
    cd site
    blogofile build
    open _site/index.html

### Working with the styles:
install lessc (on ubuntu: apt-get install npm, then npm install less)

    cd site
    ./build-styles.bash

Alternatively, you can seek out your own less compiler. See the build-styles.bash script for which less file to compile to where.

During development, it may be easier to use less.js which will compile the less styles into css per-page-view. To do this, see the comments in head.mako (basically uncomment 2 lines, and comment another -- don't forget to switch back before deploying to prod).

### Working with rest api
Rest api requires web.py module.

    workon getpython3
    pip install web.py

Once installed, you can start server, that will accept
and proccess **GET** requests for url `http://localhost:8080/convert`.
To try in-browser code convertion, start **blogofile** on any other port,
open it in the browser.

    workon getpython3
    cdvirtualenv
    python modules/rest.py
    blogofile serve 8000

### Running tests
    
    workon getpython3
    cdvirtualenv
    ./run-tests.sh
