from datetime import datetime
from fabric.api import *


def do_pack():
    '''
        Creating an archive with the file in web_static folder
    '''
    now = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                    now.month,
                                                    now.day,
                                                    now.hour,
                                                    now.minute,
                                                    now.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    local("tar -vczf versions/{} web_static".format(filename))
