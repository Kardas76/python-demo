import glob
import os
import re
import struct
import sys
from datetime import date, datetime

import serial
from PySide2.QtCore import QDateTime


class Helpers():

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    # def get_last_element_from_parenthesis(string_argument):
    #     return re.findall('\((.*?)\)', string_argument)[-1]


    def generate_COM_ports_lists_specific_for_operating_system():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        return ports



    def available_serial_ports():
        ports = Helpers.generate_COM_ports_lists_specific_for_operating_system()

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result



    # def signal_reconnect(signal, newhandler=None, oldhandler=None):        
    #     try:
    #         if oldhandler is not None:
    #             while True:
    #                 signal.disconnect(oldhandler)
    #         else:
    #             signal.disconnect()
    #     except TypeError:
    #         pass
    #     if newhandler is not None:
    #         signal.connect(newhandler)



    def compare(item1, item2):
            if Helpers.get_key_from_elem(item1) < Helpers.get_key_from_elem(item2):
                return -1
            elif Helpers.get_key_from_elem(item1) > Helpers.get_key_from_elem(item2):
                return 1
            else:
                return 0


    def get_key_from_elem(elem):
        return elem[1]


    def convert_datetime_to_msecs_since_epoch(date_time):        
        epoch = datetime.utcfromtimestamp(0)
        ms_since_epoch = (date_time - epoch).total_seconds() * 1000.0

        return ms_since_epoch
        

    def convert_qdatetime_to_msecs_since_epoch(date_time):
        date_time = QDateTime(date_time)
        ms_since_epoch = float(date_time.toMSecsSinceEpoch())
        
        return ms_since_epoch


    def convet_ms_since_epoch_to_datetime(float_number):
        s = float_number / 1000.0
        converted_datetime = datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

        return converted_datetime


    def convet_ms_since_epoch_to_qdatetime(float_number):
        converted_datetime = QDateTime.fromMSecsSinceEpoch(float_number)

        return converted_datetime


    def __init__(self):
        pass
