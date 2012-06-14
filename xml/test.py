'''
Created on 14/06/2012

@author: dnavarro
'''
import unittest
from lxml_tools import xml2dict
from lxml.builder import E

class TestLxml(unittest.TestCase):


    def test_xml2dict_simple(self):
        '''
        Converting from lxml etree to python dict
        '''
        
        xml = E.root(E.entry(E.name('Hello World')))
        expected_result = {'root': {'entry': {'name': 'Hello World'}}}
        result = xml2dict(xml)
        self.assertEquals(expected_result, result)
        
        
    def test_xml2dict_multiple_tags(self):
        '''
        Converting from lxml etree to python dict
        '''
        
        xml = E.root(E.entry(E.name('Hello World')),
                     E.entry(E.name('Bye')))
        expected_result = {'root': {'entry': [{'name': 'Hello World'}, 
                                              {'name': 'Bye'}]}}
        result = xml2dict(xml)
        self.assertEquals(expected_result, result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()