"""
Configuration properties common to everything:
Arbiter, Watcher, Plugin, etc
"""
class CircusBaseConfig(object):

    def __init__(self):
        self._name = ''
        self._cmd = None
        self._singleton = False 
        self._copy_env = False
        self._copy_path = False
        self._close_child_stderr = False
        self._close_child_stdout = False
        self._priority = 0
        self._ssh_server = None       

    def __getitem__(self, value):
        return getattr(self, value)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    @classmethod
    def __contains__(cls, value):
        for mcls in cls.__mro__:
            for k,v in mcls.__dict__.items():
                if (type(v) is property):
                    if (k == value):
                        return True
        return False

    def pop(self, value):
        return getattr(self, value)

    def keys(self):
        wkeys = []
        for k, v in self.__dict__.items():
            if (type(v) is property):
                wkeys.add[k]
        return wkeys

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = str(value)

    @property
    def singleton(self):
        return bool(self._singleton)

    @singleton.setter
    def singleton(self, value):
        self._singleton = strtobool(str(value))
    @property
    def copy_env(self):
        return bool(self._copy_env)

    @copy_env.setter
    def copy_env(self, value):
        self._copy_env = strtobool(str(value))

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = int(value)

    @property
    def ssh_server(self):
        return self._ssh_server

    @ssh_server.setter
    def ssh_server(self, value):
        self._ssh_server = str(value)

