from circus.wconfig.baseconfig import CircusBaseConfig
from circus.wconfig.sockconfig import CircusSockConfig
from circus.wconfig.watcherconfig import CircusWatcherConfig

if __name__ == "__main__":

    a = CircusBaseConfig()
    b = CircusSockConfig()
    c = CircusWatcherConfig()

    print('a:%s:%s' % (a.name, a['name']))
    print('b:%s:%s' % (b.name, b['name']))
    print('c:%s' % c.name)

    a['name'] = 'basetest'

    if 'name' in a:
        print('name in a')
    if 'name' in b:
        print('name in b')
