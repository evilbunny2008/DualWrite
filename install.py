""" Installer for SinceLastArchiveAccumulator service. """

import configobj

from weecfg.extension import ExtensionInstaller

VERSION = "0.0.2"

CONFIG = """
[DualWrite]
    binding = wx_binding_sqlite
"""

def loader():
    """ Load and return the extension installer. """
    return SinceLastArchiveAccumulatorInstaller()

class SinceLastArchiveAccumulatorInstaller(ExtensionInstaller):
    """ The extension installer. """
    def __init__(self):

        install_dict = {
            'version': VERSION,
            'name': 'DualWrite',
            # add a leading space, so that long versions does not run into the description
            'description': ' Simple extension to save the archive data to a secondary wx_binding',
            'author': "John Smith",
            'author_email': "deltafoxtrot256+DualWrite@gmail.com",
            'files': [('bin/user', ['bin/user/dualwrite.py'])],
            'config': configobj.ConfigObj(StringIO(CONFIG)),
            'archive_services': 'user.dualwrite.DualWrite',
        }

        super().__init__(install_dict)
