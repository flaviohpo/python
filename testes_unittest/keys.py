''' Documentação deste modulo '''

# Se quiser da pra importar só o Mock mesmo.
from unittest import mock
from unittest.mock import Mock

mock_get_keys = Mock(return_value=0b11000000)
# print(dir(keys))

UNPRESSED = 0
PRESSED = 10
RELEASED = 20
WAIT_RELEASE = 30
dict
KEY_STATES = {
    UNPRESSED: 'UNPRESSED',
    PRESSED: 'PRESSED',
    RELEASED: 'RELEASED',
    WAIT_RELEASE: 'WAIT RELEASE',
}

class KeyState:
    ''' Documentacao de KeyState '''
    def __init__(self):
        self.value = UNPRESSED

    def switch_to(self, new_state):
        if new_state in KEY_STATES.keys():
            self.value = new_state
            return True
        else:
            return False

    def __str__(self):
        return KEY_STATES[self.value]


class Key(KeyState):
    ''' documentacao de Key '''
    def __init__(self):
        self.value.state

    def process(self, value):
        ''' Documentacao desta funcao '''
        pass

    def get_state(self):
        ''' Documentacao desta funcao '''
        return self.state.value


class KeyManager:
    ''' documentacao de KeyManager '''
    def __init__(self):
        self.keys = list()

    def refresh_keys(self, input_values:list(Key)):
        ''' Documentacao desta funcao '''
        for k,v in input_values:
            self.keys[k].process(v)

    def get_key(self, index):
        ''' Documentacao desta funcao '''
        return self.keys[index].get_state()

