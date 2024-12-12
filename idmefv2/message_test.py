from datetime import datetime
import unittest
import uuid
from idmefv2.message import Message

VERSION = '2.D.V03'

def now():
    return datetime.now().isoformat('T')

def new_uuid():
    return str(uuid.uuid4())

def message1():
    msg = Message()
    msg['Version'] = VERSION
    msg['ID'] = new_uuid()
    msg['CreateTime'] = now()
    msg['Analyzer'] = {
        'IP':'127.0.0.1',
        'Name':'foobar',
        'Model':'generic',
        'Category':['LOG'],
        'Data':['Log'],
        'Method':['Monitor'],
    }
    return msg


def message2():
    msg = Message()
    msg['Version'] = VERSION
    msg['ID'] = new_uuid()
    msg['CreateTime'] = now()
    msg['Analyzer'] = {
        'IP':'127.0.0.1',
        'Name':'foobar',
        'Model':'generic',
        'Category':['LOG'],
        'Data':['Log'],
        'Method':['Monitor'],
    }
    msg['Sensor'] = [
        {
            'IP':'192.168.1.1',
            'Name':'TheSensor',
            'Model':'TheSensorModel',
        },
        {
            'IP':'192.168.1.2',
            'Name':'TheSensor2',
            'Model':'TheSensor2Model',
        },
    ]
    return msg

class MessageTest(unittest.TestCase):
    def testMessage1(self):
        m = message1()
        m.validate()

    def testMessage2(self):
        m = message2()
        m.validate()
