VALID_PACKAGE_1_2_RFC822 = """Metadata-Version: 1.2
Name: mudpy
Version: 0.0.1.dev232
Summary: The mudpy MUD server engine.
Home-page: http://mudpy.org/
Author: Jeremy Stanley
Author-email: fungi@yuggoth.org
License: ISC License (ISCL)
Project-URL: Bug Tracker, http://mudpy.org/contact/
Project-URL: Documentation, http://mudpy.org/documentation/
Project-URL: Source Code, http://mudpy.org/gitweb/mudpy.git
Description-Content-Type: UNKNOWN
Description: =============
         about mudpy
        =============
        
        :Copyright: (c) 2004-2016 Jeremy Stanley <fungi@yuggoth.org>. Permission
                    to use, copy, modify, and distribute this software is
                    granted under terms provided in the LICENSE file distributed
                    with this software.
        
        The mudpy project aims to create a simple, generic, cross-platform,
        freely-redistributable MUD core engine which can be easily understood
        and extended. It is written in pure Python (currently compatible with
        3.3 and later versions) and has only pure Python dependencies. All
        configuration and data are stored in consistently-formatted plain text
        (YAML) files for ease of administration. The core engine is
        unicode-clean internally and supports UTF-8 encoding for input and
        output of extended text characters.
        
        The mudpy program and sample content are released under a free and open
        license, and any bug reports, criticisms, ideas, patches, content
        submissions or other offers of collaboration are wholeheartedly welcome.
        
        Please review the other documentation files distributed with this
        software, or visit http://mudpy.org/res/src/mudpy/doc/ for additional
        information.
        
        
Keywords: mud game telnet
Platform: POSIX/Unix
Classifier: License :: OSI Approved :: ISC License (ISCL)
Classifier: Operating System :: POSIX
Classifier: Operating System :: Unix
Classifier: Programming Language :: Python
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.3
Classifier: Programming Language :: Python :: 3.4
Classifier: Programming Language :: Python :: 3.5
Classifier: Programming Language :: Python :: 3.6
Classifier: Programming Language :: Python :: 3 :: Only
Classifier: Topic :: Communications
Classifier: Topic :: Communications :: BBS
Classifier: Topic :: Communications :: Chat
Classifier: Topic :: Games/Entertainment
Classifier: Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)
Classifier: Topic :: Games/Entertainment :: Role-Playing
Classifier: Topic :: Internet
"""

VALID_PACKAGE_1_2_JSON = r"""{"license": "ISC License (ISCL)", "name": "mudpy", "metadata_version": "1.2", "description_content_type": "UNKNOWN", "home_page": "http://mudpy.org/", "author": "Jeremy Stanley", 
"project_url": ["Bug Tracker, http://mudpy.org/contact/", "Documentation, http://mudpy.org/documentation/", "Source Code, http://mudpy.org/gitweb/mudpy.git"], "summary": "The mudpy MUD server engine.", 
"platform": ["POSIX/Unix"], "version": "0.0.1.dev232", "keywords": ["mud game telnet"], "author_email": "fungi@yuggoth.org", "classifier": ["License :: OSI Approved :: ISC License (ISCL)", 
"Operating System :: POSIX", "Operating System :: Unix", "Programming Language :: Python", "Programming Language :: Python :: 3", "Programming Language :: Python :: 3.3", "Programming Language :: Python :: 3.4", 
"Programming Language :: Python :: 3.5", "Programming Language :: Python :: 3.6", "Programming Language :: Python :: 3 :: Only", "Topic :: Communications", "Topic :: Communications :: BBS", 
"Topic :: Communications :: Chat", "Topic :: Games/Entertainment", "Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)", "Topic :: Games/Entertainment :: Role-Playing", "Topic :: Internet"],
"description": "=============\n about mudpy\n=============\n\n:Copyright: (c) 2004-2016 Jeremy Stanley <fungi@yuggoth.org>. Permission\n            to use, copy, modify, and distribute this software is\n            granted under terms provided in the LICENSE file distributed\n            with this software.\n\nThe mudpy project aims to create a simple, generic, cross-platform,\nfreely-redistributable MUD core engine which can be easily understood\nand extended. It is written in pure Python (currently compatible with\n3.3 and later versions) and has only pure Python dependencies. All\nconfiguration and data are stored in consistently-formatted plain text\n(YAML) files for ease of administration. The core engine is\nunicode-clean internally and supports UTF-8 encoding for input and\noutput of extended text characters.\n\nThe mudpy program and sample content are released under a free and open\nlicense, and any bug reports, criticisms, ideas, patches, content\nsubmissions or other offers of collaboration are wholeheartedly welcome.\n\nPlease review the other documentation files distributed with this\nsoftware, or visit http://mudpy.org/res/src/mudpy/doc/ for additional\ninformation.\n\n"}"""

VALID_PACKAGE_1_2_DICT = {"license": "ISC License (ISCL)", "name": "mudpy", "metadata_version": "1.2", "description_content_type": "UNKNOWN", "home_page": "http://mudpy.org/", "author": "Jeremy Stanley", 
"project_url": ["Bug Tracker, http://mudpy.org/contact/", "Documentation, http://mudpy.org/documentation/", "Source Code, http://mudpy.org/gitweb/mudpy.git"], "summary": "The mudpy MUD server engine.", 
"platform": ["POSIX/Unix"], "version": "0.0.1.dev232", "keywords": ["mud game telnet"], "author_email": "fungi@yuggoth.org", "classifier": ["License :: OSI Approved :: ISC License (ISCL)", 
"Operating System :: POSIX", "Operating System :: Unix", "Programming Language :: Python", "Programming Language :: Python :: 3", "Programming Language :: Python :: 3.3", "Programming Language :: Python :: 3.4", 
"Programming Language :: Python :: 3.5", "Programming Language :: Python :: 3.6", "Programming Language :: Python :: 3 :: Only", "Topic :: Communications", "Topic :: Communications :: BBS", 
"Topic :: Communications :: Chat", "Topic :: Games/Entertainment", "Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)", "Topic :: Games/Entertainment :: Role-Playing", "Topic :: Internet"],
"description": "=============\n about mudpy\n=============\n\n:Copyright: (c) 2004-2016 Jeremy Stanley <fungi@yuggoth.org>. Permission\n            to use, copy, modify, and distribute this software is\n            granted under terms provided in the LICENSE file distributed\n            with this software.\n\nThe mudpy project aims to create a simple, generic, cross-platform,\nfreely-redistributable MUD core engine which can be easily understood\nand extended. It is written in pure Python (currently compatible with\n3.3 and later versions) and has only pure Python dependencies. All\nconfiguration and data are stored in consistently-formatted plain text\n(YAML) files for ease of administration. The core engine is\nunicode-clean internally and supports UTF-8 encoding for input and\noutput of extended text characters.\n\nThe mudpy program and sample content are released under a free and open\nlicense, and any bug reports, criticisms, ideas, patches, content\nsubmissions or other offers of collaboration are wholeheartedly welcome.\n\nPlease review the other documentation files distributed with this\nsoftware, or visit http://mudpy.org/res/src/mudpy/doc/ for additional\ninformation.\n\n"}



# VALID_PACKAGE_1_0 = """Metadata-Version: 1.0
# Name: test-package
# Version: 0.1
# Summary: description
# Home-page: UNKNOWN
# Author: John Doe
# Author-email: blah@example.com
# License: UNKNOWN
# Description: UNKNOWN
# Platform: UNKNOWN
# """

VALID_PACKAGE_1_0_WITH_DESC_RFC822 = """Metadata-Version: 2.1
Name: test-pkg
Version: 0.0.1
Summary: A small example package for pypa/packaging testing
Home-page: https://github.com/pypa/sampleproject
Author: Example Author
Author-email: author@example.com
License: UNKNOWN
Platform: UNKNOWN
Classifier: Programming Language :: Python :: 3
Classifier: License :: OSI Approved :: MIT License
Classifier: Operating System :: OS Independent
Requires-Python: >=3.6
Description-Content-Type: text/markdown

# Example Package

This is a simple example package to test pypa/packaging
"""

VALID_PACKAGE_1_0_WITH_DESC_JSON = r"""{"metadata_version": "2.1", "name": "test-pkg", "version": "0.0.1", "summary": "A small example package for pypa/packaging testing", "home_page": "https://github.com/pypa/sampleproject", "author": "Example Author", "author_email": "author@example.com", 
"license": "UNKNOWN", "platform": ["UNKNOWN"], "classifier": ["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"], "requires_python": ">=3.6", "description_content_type": "text/markdown", "description": "# Example Package\n\nThis is a simple example package to test pypa/packaging\n"}"""

VALID_PACKAGE_1_0_WITH_DESC_DICT = {'metadata_version': '2.1', 'name': 'test-pkg', 'version': '0.0.1', 'summary': 'A small example package for pypa/packaging testing', 
'home_page': 'https://github.com/pypa/sampleproject', 'author': 'Example Author', 'author_email': 'author@example.com', 'license': 'UNKNOWN', 'platform': ['UNKNOWN'], 
'classifier': ['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'], 'requires_python': '>=3.6', 
'description_content_type': 'text/markdown', 'description': '# Example Package\n\nThis is a simple example package to test pypa/packaging\n'}

VALID_PACKAGE_1_0_WITH_DESC_REPEATED = """Metadata-Version: 2.1
Name: test-pkg
Version: 0.0.1
Summary: A small example package for pypa/packaging testing
Home-page: https://github.com/pypa/sampleproject
Author: Example Author
Author-email: author@example.com
License: UNKNOWN
Platform: UNKNOWN
Classifier: Programming Language :: Python :: 3
Classifier: License :: OSI Approved :: MIT License
Classifier: Operating System :: OS Independent
Description: Two Descriptions!
Requires-Python: >=3.6
Description-Content-Type: text/markdown

# Example Package

This is a simple example package to test pypa/packaging"""



VALID_PACKAGE_2_1_RFC822 = """Metadata-Version: 2.1
Name: test-pkg
Version: 0.0.1
Summary: A small example package for pypa/packaging testing
Home-page: https://github.com/pypa/sampleproject
Author: Example Author
Author-email: author@example.com
License: UNKNOWN
Description: # Example Package
        
        This is a simple example package to test pypa/packaging
Platform: UNKNOWN
Classifier: Programming Language :: Python :: 3
Classifier: License :: OSI Approved :: MIT License
Classifier: Operating System :: OS Independent
Requires-Python: >=3.6
Description-Content-Type: text/markdown
"""
VALID_PACKAGE_2_1_JSON = r"""{"license": "UNKNOWN", "name": "test-pkg", "metadata_version": "2.1", "description_content_type": "text/markdown", "home_page": "https://github.com/pypa/sampleproject", "author": "Example Author", "requires_python": ">=3.6", "summary": "A small example package for pypa/packaging testing", "platform": ["UNKNOWN"], "version": "0.0.1", "author_email": "author@example.com", "classifier": ["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"], "description": "# Example Package\n\nThis is a simple example package to test pypa/packaging"}"""

VALID_PACKAGE_2_1_DICT = {'license': 'UNKNOWN', 'name': 'test-pkg', 'metadata_version': '2.1', 'description_content_type': 'text/markdown', 'home_page': 'https://github.com/pypa/sampleproject', 'author': 'Example Author', 'requires_python': '>=3.6', 'summary': 'A small example package for pypa/packaging testing', 'platform': ['UNKNOWN'], 'version': '0.0.1', 'author_email': 'author@example.com', 'classifier': ['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'], 'description': '# Example Package\n\nThis is a simple example package to test pypa/packaging'}




VALID_PACKAGE_1_1_RFC822 = """Metadata-Version: 1.1
Name: CryptoIM
Version: 0.1.1
Summary: Crypto Instant Messenger
Home-page: http://pypi.python.org/pypi/CryptoIM/
Author: CryptoIM Development Team
Author-email: skopekondrej@gmail.com
License: Apache License 2.0
Description: ========
        CryptoIM
        ========
        
        .. image:: https://travis-ci.org/oskopek/CryptoIM.png?branch=develop
            :target: https://travis-ci.org/oskopek/CryptoIM
            :alt: TravisCI
        
        .. image:: https://coveralls.io/repos/oskopek/CryptoIM/badge.png?branch=develop
            :target: https://coveralls.io/r/oskopek/CryptoIM?branch=develop
            :alt: Coveralls
        
        .. image:: https://pypip.in/v/CryptoIM/badge.png
            :target: https://pypi.python.org/pypi/CryptoIM/
            :alt: Latest Version
        
        .. image:: https://pypip.in/d/CryptoIM/badge.png
            :target: https://pypi.python.org/pypi/CryptoIM/
            :alt: Downloads
        
        .. image:: https://pypip.in/license/CryptoIM/badge.png
            :target: https://pypi.python.org/pypi/CryptoIM/
            :alt: License
        
        A secure* instant messenger written in Python out of sheer fun.
        
        \* not really secure (at least not yet)
        
        .. image:: http://cdn.imghack.se/images/47f573797aea70092c62defa3a35b3fe.png
            :alt: CryptoIM snapshot
        
        Building
        ========
        
        1. **Get the source code** `at GitHub <https://github.com/oskopek/CryptoIM>`_.
        
        2. **Build**: ``python setup.py build`` and ``sudo python setup.py install``
        
        3. To **run**: ``python main.py``
        
        4. To run **unit tests**: ``python setup.py nosetests``
        
        5. To **clean**, run: ``python setup.py clean --all``
        
        6. To **edit** connection options, edit the ``main.cfg`` file.
        
        Building on Linux
        =================
        
        * Make sure to **install** these packages using your package manager: ``python`` and ``python-setuptools``
        
        * Follow steps 2., 3. and 6. from **Building**
        
        Building on Windows
        ===================
        
        * **Install** `Python <http://www.python.org/download/releases/3.3.3/#download>`_ and `Setuptools <https://pypi.python.org/pypi/setuptools#windows>`_.
        
        * Follow steps 2., 3. and 6. from **Building**
        
        Contributing
        ============
        
        **Everyone** is encouraged to help improve this project.
        
        Here are some ways *you* can contribute:
        
        * by using alpha, beta, and prerelease versions
        * by reporting bugs
        * by suggesting new features
        * by translating to a new language
        * by writing or editing documentation
        * by writing specifications
        * by writing code (**no patch is too small**: fix typos, add comments, clean up inconsistent whitespace)
        * by refactoring code
        * by closing `issues <https://github.com/oskopek/CryptoIM/issues>`_
        * by reviewing patches
        
        Info
        ====
        
        CryptoIM uses `semantic versioning <http://semver.org/>`_ and branching model similar to `this <http://nvie.com/posts/a-successful-git-branching-model/>`_.
        
        Submitting an Issue
        ===================
        
        We use the `GitHub issue tracker <https://github.com/oskopek/CryptoIM/issues>`_ to track bugs and features. Before
        submitting a bug report or feature request, check to make sure it hasn't
        already been submitted. When submitting a bug report, please include a `Gist <https://gist.github.com/>`_
        that includes a stack trace and any details that may be necessary to reproduce
        the bug, including your Python version and operating system.
        
        Submitting a Pull Request
        =========================
        
        1. `Fork the repository <http://help.github.com/fork-a-repo/>`_.
        2. `Create a topic branch <http://learn.github.com/p/branching.html>`_.
        3. Implement your feature or bug fix.
        4. Run ``python setup.py nosetests``. If the tests fail, return to step 3.
        5. If applicable, add tests for your feature or bug fix.
        6. Add, commit, and push your changes.
        7. `Submit a pull request <http://help.github.com/send-pull-requests/>`_.
        
Keywords: crypto instant messenger
Platform: UNKNOWN
Classifier: Development Status :: 4 - Beta
Classifier: Environment :: Console
Classifier: License :: OSI Approved :: Apache Software License
Classifier: Natural Language :: English
Classifier: Programming Language :: Python
Classifier: Topic :: Communications :: Chat
Classifier: Topic :: Security :: Cryptography
"""



VALID_PACKAGE_1_1_JSON = r"""{"license": "Apache License 2.0", "name": "CryptoIM", "metadata_version": "1.1", "author": "CryptoIM Development Team", "home_page": "http://pypi.python.org/pypi/CryptoIM/", "summary": "Crypto Instant Messenger", "platform": ["UNKNOWN"], "version": "0.1.1", "keywords": ["crypto instant messenger"], "author_email": "skopekondrej@gmail.com", "classifier": ["Development Status :: 4 - Beta", "Environment :: Console", "License :: OSI Approved :: Apache Software License", "Natural Language :: English", "Programming Language :: Python", "Topic :: Communications :: Chat", "Topic :: Security :: Cryptography"], "description": "========\nCryptoIM\n========\n\n.. image:: https://travis-ci.org/oskopek/CryptoIM.png?branch=develop\n    :target: https://travis-ci.org/oskopek/CryptoIM\n    :alt: TravisCI\n\n.. image:: https://coveralls.io/repos/oskopek/CryptoIM/badge.png?branch=develop\n    :target: https://coveralls.io/r/oskopek/CryptoIM?branch=develop\n    :alt: Coveralls\n\n.. image:: https://pypip.in/v/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: Latest Version\n\n.. image:: https://pypip.in/d/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: Downloads\n\n.. image:: https://pypip.in/license/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: License\n\nA secure* instant messenger written in Python out of sheer fun.\n\n\\* not really secure (at least not yet)\n\n.. image:: http://cdn.imghack.se/images/47f573797aea70092c62defa3a35b3fe.png\n    :alt: CryptoIM snapshot\n\nBuilding\n========\n\n1. **Get the source code** `at GitHub <https://github.com/oskopek/CryptoIM>`_.\n\n2. **Build**: ``python setup.py build`` and ``sudo python setup.py install``\n\n3. To **run**: ``python main.py``\n\n4. To run **unit tests**: ``python setup.py nosetests``\n\n5. To **clean**, run: ``python setup.py clean --all``\n\n6. To **edit** connection options, edit the ``main.cfg`` file.\n\nBuilding on Linux\n=================\n\n* Make sure to **install** these packages using your package manager: ``python`` and ``python-setuptools``\n\n* Follow steps 2., 3. and 6. from **Building**\n\nBuilding on Windows\n===================\n\n* **Install** `Python <http://www.python.org/download/releases/3.3.3/#download>`_ and `Setuptools <https://pypi.python.org/pypi/setuptools#windows>`_.\n\n* Follow steps 2., 3. and 6. from **Building**\n\nContributing\n============\n\n**Everyone** is encouraged to help improve this project.\n\nHere are some ways *you* can contribute:\n\n* by using alpha, beta, and prerelease versions\n* by reporting bugs\n* by suggesting new features\n* by translating to a new language\n* by writing or editing documentation\n* by writing specifications\n* by writing code (**no patch is too small**: fix typos, add comments, clean up inconsistent whitespace)\n* by refactoring code\n* by closing `issues <https://github.com/oskopek/CryptoIM/issues>`_\n* by reviewing patches\n\nInfo\n====\n\nCryptoIM uses `semantic versioning <http://semver.org/>`_ and branching model similar to `this <http://nvie.com/posts/a-successful-git-branching-model/>`_.\n\nSubmitting an Issue\n===================\n\nWe use the `GitHub issue tracker <https://github.com/oskopek/CryptoIM/issues>`_ to track bugs and features. Before\nsubmitting a bug report or feature request, check to make sure it hasn't\nalready been submitted. When submitting a bug report, please include a `Gist <https://gist.github.com/>`_\nthat includes a stack trace and any details that may be necessary to reproduce\nthe bug, including your Python version and operating system.\n\nSubmitting a Pull Request\n=========================\n\n1. `Fork the repository <http://help.github.com/fork-a-repo/>`_.\n2. `Create a topic branch <http://learn.github.com/p/branching.html>`_.\n3. Implement your feature or bug fix.\n4. Run ``python setup.py nosetests``. If the tests fail, return to step 3.\n5. If applicable, add tests for your feature or bug fix.\n6. Add, commit, and push your changes.\n7. `Submit a pull request <http://help.github.com/send-pull-requests/>`_.\n"}"""


VALID_PACKAGE_1_1_DICT = {'license': 'Apache License 2.0', 'name': 'CryptoIM', 'metadata_version': '1.1', 'author': 'CryptoIM Development Team', 'home_page': 'http://pypi.python.org/pypi/CryptoIM/', 'summary': 'Crypto Instant Messenger', 'platform': ['UNKNOWN'], 'version': '0.1.1', 'keywords': ['crypto instant messenger'], 'author_email': 'skopekondrej@gmail.com', 'classifier': ['Development Status :: 4 - Beta', 'Environment :: Console', 'License :: OSI Approved :: Apache Software License', 'Natural Language :: English', 'Programming Language :: Python', 'Topic :: Communications :: Chat', 'Topic :: Security :: Cryptography'], 'description': "========\nCryptoIM\n========\n\n.. image:: https://travis-ci.org/oskopek/CryptoIM.png?branch=develop\n    :target: https://travis-ci.org/oskopek/CryptoIM\n    :alt: TravisCI\n\n.. image:: https://coveralls.io/repos/oskopek/CryptoIM/badge.png?branch=develop\n    :target: https://coveralls.io/r/oskopek/CryptoIM?branch=develop\n    :alt: Coveralls\n\n.. image:: https://pypip.in/v/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: Latest Version\n\n.. image:: https://pypip.in/d/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: Downloads\n\n.. image:: https://pypip.in/license/CryptoIM/badge.png\n    :target: https://pypi.python.org/pypi/CryptoIM/\n    :alt: License\n\nA secure* instant messenger written in Python out of sheer fun.\n\n\\* not really secure (at least not yet)\n\n.. image:: http://cdn.imghack.se/images/47f573797aea70092c62defa3a35b3fe.png\n    :alt: CryptoIM snapshot\n\nBuilding\n========\n\n1. **Get the source code** `at GitHub <https://github.com/oskopek/CryptoIM>`_.\n\n2. **Build**: ``python setup.py build`` and ``sudo python setup.py install``\n\n3. To **run**: ``python main.py``\n\n4. To run **unit tests**: ``python setup.py nosetests``\n\n5. To **clean**, run: ``python setup.py clean --all``\n\n6. To **edit** connection options, edit the ``main.cfg`` file.\n\nBuilding on Linux\n=================\n\n* Make sure to **install** these packages using your package manager: ``python`` and ``python-setuptools``\n\n* Follow steps 2., 3. and 6. from **Building**\n\nBuilding on Windows\n===================\n\n* **Install** `Python <http://www.python.org/download/releases/3.3.3/#download>`_ and `Setuptools <https://pypi.python.org/pypi/setuptools#windows>`_.\n\n* Follow steps 2., 3. and 6. from **Building**\n\nContributing\n============\n\n**Everyone** is encouraged to help improve this project.\n\nHere are some ways *you* can contribute:\n\n* by using alpha, beta, and prerelease versions\n* by reporting bugs\n* by suggesting new features\n* by translating to a new language\n* by writing or editing documentation\n* by writing specifications\n* by writing code (**no patch is too small**: fix typos, add comments, clean up inconsistent whitespace)\n* by refactoring code\n* by closing `issues <https://github.com/oskopek/CryptoIM/issues>`_\n* by reviewing patches\n\nInfo\n====\n\nCryptoIM uses `semantic versioning <http://semver.org/>`_ and branching model similar to `this <http://nvie.com/posts/a-successful-git-branching-model/>`_.\n\nSubmitting an Issue\n===================\n\nWe use the `GitHub issue tracker <https://github.com/oskopek/CryptoIM/issues>`_ to track bugs and features. Before\nsubmitting a bug report or feature request, check to make sure it hasn't\nalready been submitted. When submitting a bug report, please include a `Gist <https://gist.github.com/>`_\nthat includes a stack trace and any details that may be necessary to reproduce\nthe bug, including your Python version and operating system.\n\nSubmitting a Pull Request\n=========================\n\n1. `Fork the repository <http://help.github.com/fork-a-repo/>`_.\n2. `Create a topic branch <http://learn.github.com/p/branching.html>`_.\n3. Implement your feature or bug fix.\n4. Run ``python setup.py nosetests``. If the tests fail, return to step 3.\n5. If applicable, add tests for your feature or bug fix.\n6. Add, commit, and push your changes.\n7. `Submit a pull request <http://help.github.com/send-pull-requests/>`_.\n"}