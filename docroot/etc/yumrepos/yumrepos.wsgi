from yumrepos.app import create_application
from yumrepos.fs_backend import FsBackend

backend = FsBackend("/usr/share/yumrepos")
application = create_application(backend)
