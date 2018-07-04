#! /usr/bin/env python3
# coding: utf-8

import argparse

import analysis.csv, analysis.xml

def parse_arguments():
    parser = argparse.ArgumentParser() #create an instance
    parser.add_argument("-e", "--extension", help="""type of file to analyze (csv or xml)""")
    parser.add_argument("-d", "--datafile", help="""name of the file to analyze (csv or xml)""")
    return parser.parse_args()

def main():
    args = parse_arguments()
    #import pdb; pdb.set_trace() #breakpoint definition
    datafile = args.datafile
    if args.extension == 'csv':
        analysis.csv.launch_analysis(datafile)
    elif args.extension == 'xml':
        analysis.xml.launch_analysis(datafile)

    
if __name__ == "__main__":    
    main()