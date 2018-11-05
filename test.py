import signal
import sys
from distutils.util import strtobool

# TODO: validate values for all properties
class Test(object):

    def __init__(self):
        self._env = None
        #self._env = ''
        self._singleton = False
        self._max_age = 0

    def __getitem__(self, value):
        print("__getitem__(%s):" % value)
        print("type(%s):" % type(value))
        #sys.exit(1) 
        #return "test"
        return getattr(self, value)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    @classmethod
    def __contains__(cls, value):
        for mcls in cls:
            for k,v in Test.__dict__.items():
                if (type(v) is property):
                    if (k == value):
                        return True
        return False
    def keys(self):
        wkeys = []
        for k, v in self.__dict__.items():
            if(type(v) is property):
                wkeys.add[k]
        return wkeys

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value

    @property
    def singleton(self):
        return bool(self._singleton)

    @singleton.setter
    def singleton(self, value):
        self._singleton = strtobool(str(value))

    @property
    def max_age(self):
        return self._max_age

    @max_age.setter
    def max_age(self, value):
        self._max_age = int(value)

if __name__ == "__main__":

    a = Test()

    for k,v in Test.__dict__.items():
        if (type(v) is property):
            print("%s:%s" % (k, getattr(a, k)))


    #print("a['singleton']:%s" % a['singleton'])
    #a['singleton'] = True
    #print("a['singleton']:%s" % a['singleton'])

    #print('singleton:%s' % a.singleton)
    #print('if singleton in a')
    if 'singleton' in a:
        print('singleton is in a')
    else:
        print('singleton not int a')
