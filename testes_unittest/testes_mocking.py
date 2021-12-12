# no mock a gente vai usar Mock, MagicMock e Patch
# MagicMock to mock magic methods
# MagicMock class is just a Mock variant that has all of the magic methods pre-created for you
# Se quiser da pra importar só o Mock mesmo.
#from unittest.mock import MagicMock

from unittest.mock import Mock

mock = Mock()
mock.__str__ = Mock(return_value='wheeeeee')
print(str(mock))

# Um teste mais útil seria o seguinte:
