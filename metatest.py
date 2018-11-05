class MetaEnum(type):
    def __contains__(cls, value):
        for k,v in cls.__dict__.items():
            if(type(v) is property):
                if (k == value):
                    return True
        return False
        #return x in range(cls.k)

class BaseEnum(metaclass=MetaEnum):
    def __init__(self):
        self._name = 'BaseEnum.name'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class MyEnum(BaseEnum):
    def __init__(self):
        super(MyEnum, self).__init__()
        self._name = 'MyEnum.name'
        self._subname = 'MyEnum.subname' 

    @property
    def subname(self):
        return self._subname

    @subname.setter
    def subname(self, value):
        self._subname = value

baseenum = BaseEnum()
myenum = MyEnum()

print('name in baseenum %s' % baseenum.name)
baseenum.name = 'BaseEnum.name.changed'
print('name in baseenum %s' % baseenum.name)
print('name in myenum %s' % myenum.name)
myenum.name = 'MyEnum.name.changed'
print('name in myenum %s' % myenum.name)
print('subname in myenum %s' % myenum.subname)

print('name in BaseEnum %s' % ('name' in BaseEnum))
print('name in MyEnum %s' % ('name' in MyEnum))
print('name in baseenum %s' % ('name' in baseenum))
