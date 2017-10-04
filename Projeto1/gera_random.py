# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:56:55 2017

@author: Ricardo
"""

import random, string

def ger_num(quantidade):
    random1 = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(quantidade)])
    return random1