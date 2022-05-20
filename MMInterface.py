class MMInterface(object):
    BUS_NAME = 'org.freedesktop.ModemManager1'

    def __init__(self, manager=None):
        self._manager = manager
        self._instance = None

    def __getattr__(self, item):
        if not hasattr(self, item):
            return getattr(self._instance, item)
        return getattr(self, item)

    @property
    def path(self) -> str:
        return self._instance._path

    def get_object(self, path):
        return self._manager.get_object(path)
