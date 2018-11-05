from circus.wconfig.baseconfig import CircusBaseConfig

class CircusSockConfig(CircusBaseConfig):

    def __init__(self):
        super(CircusSockConfig, self).__init__()

        self._name = 'Sock'
        self._socket = 'socket'

    @property
    def socket(self):
        return self._socket

    @socket.setter
    def socket(self, value):
        self._socket = str(value)
