import os
from thoughts_backend.app import create_app

NO_SYSLOG = bool(os.environ.get('NO_SYSLOG'))
application = create_app(script=NO_SYSLOG)
