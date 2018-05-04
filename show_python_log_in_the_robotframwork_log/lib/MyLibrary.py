from robot.api import logger
#import logging
import sys

class MyLibrary(object):
    
    def __init__(self):
        self.count = 0
        
    def get_count_value(self):
        self.count = self.count + 1
        return self.count

    def show_log_via_print(self):
        print '*INFO* Info Message'
        print '*DEBUG* Debug Message'
        print '*TRACE* Trace Message'
        print '*WARN* Warn Message'
        print '*ERROR* Error Message'
    

    def show_log_via_robot_api(self):
        """ from robot.api import logger """
        
        logger.debug('Debug Message')
        logger.info('Info Message')
        logger.trace('Trace Message')
        logger.warn('Warn Message')
        logger.error('Error Message')
    
    def show_message_on_console_only(self):
        """ import sys """
        
        sys.__stdout__.write('This stdout message is on console only, not in the log file.')
        sys.__stderr__.write('This stderr message is on console only, not in the log file.')
