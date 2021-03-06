TravisDemo demonstrates a possible bug in TravisCI.

It's bad practice to name files so generically that they conflict with
standard library filenames such as math.py and email.py. But as new
files are added to the standard library, advising developers to avoid
name conflicts doesnt scale. So python 2.5 introduced the
absolute\_import option, which became the default in python 3. In my
[OpenTaxForms](https://github.com/jsaponara/opentaxforms/) project, I
had a math.py file until I noticed that it broke my travis build. This
project exists merely to demonstrate that a conflicting python filename
breaks the travis build, and perhaps to prompt some discussion at
travis-ci.org about whether this is a bug.

-   **Build status**

    -   should be failing

    [![Build Status](https://travis-ci.org/jsaponara/travisdemo.svg)](https://travis-ci.org/jsaponara/travisdemo)

-   **Github**

    -   [code](https://github.com/jsaponara/travisdemo/)

-   **License**

    [GNU AGPLv3](http://choosealicense.com/licenses/agpl-3.0/)

-   **Install**

    pip install travisdemo

-   **To do**

    -   all done!

