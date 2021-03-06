'''
Tests for the file state
'''
# Import python libs
import os
#
# Import salt libs
from saltunittest import TestLoader, TextTestRunner
import integration
from integration import TestDaemon

class CMDTest(integration.ModuleCase):
    '''
    Validate the cmd state
    '''
    def test_run(self):
        '''
        cmd.run
        '''
        ret = self.run_state('cmd.run', name='ls')
        result = ret[ret.keys()[0]]['result']
        self.assertTrue(result)

    def test_test_run(self):
        '''
        cmd.run test interface
        '''
        ret = self.run_state('cmd.run', name='ls', test=True)
        result = ret[ret.keys()[0]]['result']
        self.assertIsNone(result)

