import circus
import collections
from distutils.util import strtobool

# TODO: validate values for all properties
class WatcherConfiguration(object):

    def __init__(self):
        self._name = None
        self._cmd = None
        self._args = None
        self._numprocesses = 1
        self._working_dir = None
        self._shell = False
        self._uid = None
        self._gid = None
        self._send_hup = False
        self._stop_signal = 'SIGTERM'
        self._stop_children = False
        self._env = None
        self._rlimits = None  #TODO: fix me
        self._stdout_stream = None 
        self._stderr_stream = None
        self._priority = 0
        self._singleton = False
        self._use_sockets = False
        self._on_demand = False
        self._copy_env = False
        self._copy_path = False
        self._max_age = 0
        self._max_age_variance = 0
        self._respawn = True
        self._virtualenv = None
        self._stdin_socket = None
        self._close_child_stdin = True
        self._close_child_stdout = False
        self._close_child_stderr = False
        self._use_papa = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if (type(value) is str):
            self._name = value
        else:
            raise ValueError('name must be a string')

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if (type(value) is str):
            self._cmd = value
        else:
            raise ValueError('cmd must be a string')

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        if (type(value) is str):
            self._args = value
        else:
            raise ValueError('args must be a string')

    @property
    def numprocesses(self):
        return self._numprocesses

    @numprocesses.setter
    def numprocesses(self, value):
        if (type(value) is int):
            self._numprocesses = value
        else:
            raise ValueError('numprocesses must be an integer')

    @property
    def working_dir(self):
        return self._working_dir

    @working_dir.setter
    def working_dir(self, value):
        if (type(value) is str):
            self._working_dir = value
        else:
            raise ValueError('working_dir must be a string')

    @property
    def shell(self):
        return bool(self._shell)

    @shell.setter
    def shell(self, value):
        self._shell = strtobool(str(value))

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        if (type(value) is int):
            self._uid = value
        else:
            raise ValueError('uid must be an integer')

    @property
    def gid(self):
        return self._gid

    @gid.setter
    def gid(self, value):
        if (type(value) is int):
            self._gid = value
        else:
            raise ValueError('gid must be an integer')

    @property
    def send_hup(self):
        return bool(self._send_hup)

    @send_hup.setter
    def send_hup(self, value):
        self._send_hup = strtobool(str(value))

    @property
    def stop_signal(self):
        return self._stop_signal

    @stop_signal.setter
    def stop_signal(self, value):
        #TODO: create a signel validation
        self._stop_signal = value

    @property
    def stop_children(self):
        return bool(self._stop_children)

    @stop_children.setter
    def stop_children(self, value):
        self._stop_children = strtobool(value)

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value

    # TODO: need to get all the rlimits

    @property
    def stdout_stream(self):
        return self._stdout_stream

    @stdout_stream.setter
    def stdout_stream(self, value):
        #TODO: validate the items()
        #if (isinstance(dictionay, dict)):
        if (type(value) is dict):
            if (type(self._stdout_stream) is not dict):
                self._stdout_stream = dict()
            for k, v in value.items():
                self._stdout_stream[k] = v
        else:
            raise ValueError('stdout_stream must be a dict')

    @property
    def stderr_stream(self):
        return self._stderr_stream

    @stderr_stream.setter
    def stderr_stream(self, value):
        if (type(value) is dict):
            print(type(self._stderr_stream))
            if (type(self._stderr_stream) is not dict):
                print('make it a dict!!')
                self._stderr_stream = dict()
            for k, v in value.items():
                self._stdout_stream[k] = v
        else:
            raise ValueError('stderr_stream must be a dict')

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if (type(value) is int):
            self._priority = value
        else:
            raise ValueError('priority must be an integer')

    @property
    def singleton(self):
        return bool(self._singleton)

    @singleton.setter
    def singleton(self, value):
        self._singleton = strtobool(value)

    @property
    def use_sockets(self):
        return bool(self._use_sockets)

    @use_sockets.setter
    def use_sockets(self, value):
        self._use_sockets = strtobool(value)

    @property
    def on_demand(self):
        return bool(self._on_demand)

    @on_demand.setter
    def on_demand(self, value):
        self._on_demand = strtobool(value)

    @property
    def copy_env(self):
        return bool(self._copy_env)

    @copy_env.setter
    def copy_env(self, value):
        self._copy_env = strtobool(value)

    @property
    def copy_path(self):
        return bool(self._copy_path)

    @copy_path.setter
    def copy_path(self, value):
        self._copy_path = strtobool(value)

    @property
    def max_age(self):
        return self._max_age

    @max_age.setter
    def max_age(self, value):
        if (type(value) is int):
            self._max_age = value
        else:
            raise ValueError('max_age must be an integer')

    @property
    def max_age_variance(self):
        return self._max_age_variance

    @max_age_variance.setter
    def max_age_variance(self, value):
        self._max_age_variance = int(value)

    # TODO: need to get all the hooks

    # TODO: need to figure out what to do with options

    @property
    def respawn(self):
        return bool(self._respawn)

    @respawn.setter
    def respawn(self, value):
        self._respawn = strtobool(value)

    @property
    def virutalenv(self):
        return self._virtualenv

    @virutalenv.setter
    def virutalenv(self, value):
        if (type(value) is str):
            self._virtualenv = value
        else:
            raise ValueError('virutualenv need to be a string path')

    @property
    def stdin_socket(self):
        return self._stdin_socket

    @stdin_socket.setter
    def stdin_socket(self, value):
        #TODO: what does this value need to be?
        pass

    @property
    def close_child_stdin(self):
        return self._close_child_stdin

    @close_child_stdin.setter
    def close_child_stdin(self, value):
        self._close_child_stdin = strtobool(value)

    @property
    def close_child_stdout(self):
        return self._close_child_stdout

    @close_child_stdout.setter
    def close_child_stdout(self, value):
        self._close_child_stdout = strtobool(value)

    @property
    def close_child_stderr(self):
        return self._close_child_stderr

    @close_child_stderr.setter
    def close_child_stderr(self, value):
        self._close_child_stdout = strtobool(value)

    @property
    def use_papa(self):
        return self._use_papa

    @use_papa.setter
    def use_papa(self, value):
        self._use_papa = strtobool(value)

if __name__ == "__main__":
    a = WatcherConfiguration()
    #a.max_age_variance = 'aa'
    a.respawn = 'false'
    print('respawn %s' % a.respawn)
    a.send_hup = False
    print("send_hup %s" % a.send_hup)
    try:
        a.stdout_stream = 11
        print("%s:%s" % (type(a.stdout_stream), a.stdout_stream))
    except ValueError as e:
        print(str(e))
        pass

    try:
        a.stdout_stream = { 'class': 'FileOutputStream', 'filename': '/Users/mercma/output.log' }
        print("%s:%s" % (type(a.stdout_stream), a.stdout_stream))
    except ValueError as e:
        print(str(e))
        pass

    #try:
    #    a['stdout_stream'] = 10
    #    print("%s:%s" % (type(a.stdout_stream), a.stdout_stream))
    #except ValueError as e:
    #    print(str(e))


    for k,v in WatcherConfiguration.__dict__.items():
        if (type(v) is property):
            print("%s:%s" % (k, getattr(a, k)))
