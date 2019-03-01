# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(""" Argparse Demo """)
parser.add_argument("-s", "--size", type=int, help="Bike size")
parser.add_argument("-m", "--model", type=str, help="Bike size")
args = parser.parse_args()
print("Size  is {}".format(args.size))    
print("Model is {}".format(args.model))         

