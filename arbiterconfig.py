"""
Configuration information specific to arbiter
"""
from distutils.util import strtobool
from circus.wconfig.baseconfig import CircusBaseConfig

class CircusArbiterConfig(CircusBaseConfig):

    def __init__(self):
        super(CircusArbiterConfig, self).__init__()
        self._name = ''
        self._cmd = None

        self._endpoint = None
        self._pubsub_endpoint = None
        self._check_delay = 1
        self._prereload_fn = None
        self._statsd = False
        self._stats_endpoint = None
        self._papa_endpoint = None
        self._multicast_endpoint = None
        self._plugins = None
        self._sockets = None
        self._warmup_delay = 0
        self._httpd = None
        self._loop = None
        self._httpd_host = 'localhost'
        self._httpd_port = 8080
        self._debug = False
        self._debug_gc = False
        self._ssh_server = None
        self._pidfile = None
        self._loglevel = None
        self._logoutput = None
        self._loggerconfig = None
        self._fqdn_prefix = None
        self._umask = None
        self._endpoint_owner = None

        self._singleton = True
        self._copy_env = True
        self._copy_path = True
        self._close_child_stderr = False
        self._close_child_stdout = False
        self._priority = 1

    @property
    def endpoint(self):
        return self._name

    @endpoint.setter
    def endpoint(self, value):
        self._use = str(value)

    @property
    def pubsub_endpoint(self):
        return self._pubsub_endpoint

    @pubsub_endpoint.setter
    def pubsub_endpoint(self, value):
        self._pubsub_endpoint = str(value)

    @property
    def check_delay(self):
        return self._check_delay

    @check_delay.setter
    def check_delay(self, value):
        self._check_delay = int(value)

    @property
    def prereload_fn(self):
        return self._prereload_fn

    @prereload_fn.setter
    def prereload_fn(self):
        self._prereload_fn = str(value)

    @property
    def statsd(self):
        return self._statsd

    @statsd.setter
    def statsd(self, value):
        self._statsd = strtobool(str(value))

    @property
    def stats_endpoint(self):
        return self._stats_endpoint

    @stats_endpoint.setter
    def stats_endpoint(self, value):
        self._stats_endpoint = str(value)

    @property
    def papa_endpoint(self):
        return self._papa_endpoint

    @papa_endpoint.setter
    def papa_endpoint(self, value):
        self._papa_endpoint = str(value)

   @property
   def multicast_endpoint(self):
       return self._multicast_endpoint

   @multicast_endpoint.setter
   def multicast_endpoint(self, value):
       self._multicast_endpoint = value

   @property
   def plugins(self):
       return self._plugins

   @plugins.setter
   def plugins(self, value):
       self._plugins = value

   @property
   def sockets(self):
       return self._sockets

   @sockets.setter
   def sockets(self, value):
       self._sockets = value

   @property
   def warmup_delay(self):
       return self._warmup_delay

   @warmup_delay.setter
   def warmup_delay(self, value):
       self._warmup_delay = int(value)

   @property
   def httpd(self):
       return self._httpd

   @httpd.setter
   def httpd(self, value):
       self._httpd = str(value)

   @property
   def loop(self):
       return self._loop

   @loop.setter
   def loop(self, value):
       self._loop = value

   @property
   def httpd_host(self):
       return self._httpd_host

   @httpd_host.setter
   def httpd_host(self, value):
       self._httpd_host = str(value)

   @property
   def httpd_port(self):
       return self._httpd_port

   @httpd_port.setter
   def httpd_port(self, value):
       self._httpd_port = int(value)

   @property
   def debug(self):
       return self._debug

   @debug.setter
   def debug(self, value):
       self._debug = strtobool(str(value))

    @property
    def debug_gc(self):
        return self._debug_gc

    @debug_gc.setter
    def debug_gc(self, value):
        self._debug_gc = strtobool(str(value))

    @property
    def ssh_server(self):
        return self._ssh_server

    @ssh_server.setter
    def ssh_server(self, value):
        self._ssh_server = str(value)

    @property
    def pidfile(self):
        return self._pidfile
 
    @pidfile.setter
    def pidfile(self, value):
        self._pidfile = str(value)

    @property
    def loglevel(self):
        return self._loglevel

    @loglevel.setter
    def loglevel(self, value):
        self._loglevel = value

    @property
    def logoutput(self):
        return self._logoutput

    @logoutput.setter
    def logoutput(self, value):
        self._logoutput = str(value)

    @property
    def fqdn_prefix(self):
        return self._fqdn_prefix

    @fqnd_prefix.setter
    def fqdn_prefix(self, value):
        self._fqdn_prefix = str(value)

    @property
    def umask(self):
        return self._umask

    @umask.setter
    def umask(self, value):
        self._umask = value

    @property
    def endpoint_owner(self):
        return self._endpoint_owner

    @endpoint_owner.setter
    def endpoint_owner(self, value):
        self._endpoint_owner = str(value)
