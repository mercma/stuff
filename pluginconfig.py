"""
Configuration information specific to Plug-in
"""
class CircusPluginConfig(CircusBaseConfig):

    def __init__(self):
        self._name = ''
        self._cmd = None
        self._use = ''
        self._singleton = True
        self._copy_env = True
        self._copy_path = True
        self._close_child_stderr = False
        self._close_child_stdout = False
        self._priority = 1

    @property
    def use(self):
        return self._name

    @use.setter
    def use(self, value):
        self._use = str(value)
