from abc import ABCMeta, abstractmethod
 
class Capability(object):
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def handle(self):
        pass


