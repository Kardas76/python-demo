import pytest
import unittest

from app import functions

import modbus_tk.defines as cst

# from model.modbus_tk_custom import modbus_rtu_serial_interface

@pytest.fixture
def init_functions_obj():
    return functions.Functions()

@pytest.mark.skip
@pytest.mark.parametrize("word, expected", [('kayak', True), ('civic', True), ('forest', False)])
def test_get_program_arguments(word, expected, init_functions_obj):
    result = init_functions_obj.get_program_arguments()
    
    assert result.mode is None