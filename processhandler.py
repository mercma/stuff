import os
import re

from configparser import ConfigParser
from circus.plugins import CircusPlugin
from circus import logger

class ProcessHandler(CircusPlugin):

    name = 'processhandler'

    def __init__(self, *args, **config):
        super(ProcessHandler, self).__init__(*args, **config)
        self.configfile = config.get('configfile')

    def _handle_action_add(self):
        logger.debug('_handle_action_add')
        # read the config file
        config = ConfigParser(allow_no_value = True)
        config.read(self.configfile)

        # the section in the config file is
        # [watcher:<self.watcher_name>]
        watcher_section = "watcher:{0}".format(self.watcher_name)

        # get the options for the 'add'ed process
        watcher_msg = self.call("options", name=self.watcher_name)

        # configparser needs to have the '%' symbol escaped
        # for the *_stream.timestamp options
        for k,v in watcher_msg.get('options').items():
            match = re.search('time_format$', k)
            if match:
                result = re.sub("%", "%%", v)
                watcher_msg.get('options')[k] = result
        

        # add the config section to the file
        config[watcher_section] = watcher_msg.get('options')

        # remove any 'empty' keys
        empty_keys = [k for k,v in config[watcher_section].items() if not v]
        for k in empty_keys:
            config[watcher_section].pop(k, None)

        # write the updated configuration file
        with open(self.configfile,'w') as configfile:
            config.write(configfile)


    def _handle_action_remove(self):
        logger.debug('_handle_action_remove')
        # read the config file
        config = ConfigParser(allow_no_value = True)
        config.read(self.configfile)

        # the section in the config file is
        # [watcher:<self.watcher_name>]
        watcher_section = "watcher:{0}".format(self.watcher_name)

        #remove the section from the config file
        #del config[self.watcher_name]
        config.pop(watcher_section, None)
        #config.popitem(self.watcher_name)


        with open(self.configfile, 'w') as configfile:
            config.write(configfile)


    def handle_init(self):
        pass

    def handle_stop(self):
        pass

    def handle_recv(self, data):
        self.watcher_name, self.action, self.msg = self.split_data(data)
        logger.debug('[watcher:%s] action:\'%s\'' % 
                (self.watcher_name, self.action))
        #self.msg_dict = self.load_message(self.msg)
        if (self.action == 'add'):
            self._handle_action_add()
        if (self.action == 'remove'):
            self._handle_action_remove()
        if (self.action == 'updated'):
            self._handle_action_add()
