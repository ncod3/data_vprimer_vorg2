#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pprint

from Bio import Restriction

# http://biopython.org/DIST/docs/cookbook/Restriction.html#1.1

def main():

    rb_supp = Restriction.RestrictionBatch(
        first=[],
        suppliers=[
            'C','B','E','I','K','J','M',\
            'O','N','Q','S','R','V','Y','X'])

    enz_cnt = len(rb_supp)

    '''
>>> RestrictionBatch.show_codes()  # as of May 2016 REBASE release.
C = Minotech Biotechnology
B = Life Technologies
E = Agilent Technologies
I = SibEnzyme Ltd.
K = Takara Bio Inc.
J = Nippon Gene Co., Ltd.
M = Roche Applied Science
O = Toyobo Biochemicals
N = New England Biolabs
Q = Molecular Biology Resources - CHIMERx
S = Sigma Chemical Corporation
R = Promega Corporation
V = Vivantis Technologies
Y = SinaClon BioScience Co.
X = EURx Ltd.
>>> # You can now choose a code and built your RestrictionBatch
    '''
    enzyme_list = list()

    for enz_cls in rb_supp:
        enzyme_list.append("{}\t{}\t{}\t{}".format(
            enz_cls,
            enz_cls.site,
            enz_cls.elucidate(), len(enz_cls)))

    last_first_char = ""
    line = ""
    
    for enz_line in sorted(enzyme_list):

        first_char = enz_line[0:1].upper()
        if last_first_char != first_char:
            print("\n#")
        
        print(enz_line)
        last_first_char = first_char

    print("{}".format(enz_cnt), file=sys.stderr)


if __name__ == '__main__':
    main()

