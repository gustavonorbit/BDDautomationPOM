import configparser

import os

def readConfigData(section, key):
    config = configparser.ConfigParser()
    path = "D:\\BDDautomationPOM\\configFiles\\config.cfg"
    config.read(path)
    return config.get(section, key)

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    path = "D:\\BDDautomationPOM\\configFiles\\Elements.cfg"
    config.read(path)
    return config.get(section, key)