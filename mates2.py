#!/usr/bin/python
#-*- coding:utf-8 -*-
def add_property(self):
 property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()
 payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()
