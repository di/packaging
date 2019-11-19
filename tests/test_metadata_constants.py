VALID_PACKAGE_1_2 = """Metadata-Version: 1.2
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


VALID_PACKAGE_1_0 = """Metadata-Version: 1.0
Name: test-package
Version: 0.1
Summary: description
Home-page: UNKNOWN
Author: Blah Blah
Author-email: blah@example.com
License: UNKNOWN
Description: UNKNOWN
Platform: UNKNOWN
"""

INVALID_LICENSE_1_0 = """Metadata-Version: 1.0
Name: test-package
Version: 0.1
Summary: description
Home-page: UNKNOWN
Author: Blah Blah
Author-email: blah@example.com
License: blah not
correct
at all
Description: this
        is
        a
        long
        description
Platform: UNKNOWN
"""