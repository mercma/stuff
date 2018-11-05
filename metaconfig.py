#from future.utils import with_metaclass

class MetaConfig(type):

    def __contains__(cls, value):
        print('__contains')
        for k,v in cls.__dict__.items():
            if (type(v) is property):
                if (k == value):
                    return True
        return False
