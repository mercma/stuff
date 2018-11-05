from pprint import pprint
from distutils.util import strtobool
from circus.wconfig.baseconfig import CircusBaseConfig

class MetaConfig(type):
    @classmethod
    def __contains__(cls, value):
        for k,v in cls.__dict__.items():
            if (type(v) is property):
                if (k == value):
                    return True
        return False

#class Base(object):
#    pass

class BaseConfig(object):
    def __init__(self):
        self._name = 'Base.name'

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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class SubConfig(BaseConfig):
    def __init__(self):
        super(SubConfig, self).__init__()
        self._name = 'SubConfig.name'
        self._sub = 'SubConfig.sub'

    @property
    def sub(self):
        return self._sub

if __name__ == "__main__":
    a = BaseConfig()
    b = SubConfig()

    print('name' in a)
    print('name' in b)

    a['name'] = 'test.name'
    
    a.name = 'new'
    b.name = 'subnew'

    print('base %s' % a.name)
    print('sub %s:%s' % (b.name, b.sub))
    
