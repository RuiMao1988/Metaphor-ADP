#! /usr/bin/env python

# Generates lexical axioms. This is called from sqlite_query.py.

import argparse
import sys
import re

class Template(object):
    """
    Class representing axiom templates
    """
    def __init__(self, pos, name, domain, subdomain, r1, r2, r3, r4, weight):
        self.pos = pos
        self.name = name
        self.dash = re.search("-", name)
        self.domain = domain.upper()
        self.subdomain = subdomain.upper()
        self.r1 = r1 if r1 else None
        self.r2 = r2 if r2 else None
        self.r3 = r3 if r3 else None
        self.r4 = r4 if r4 else None
        self.weight = str(weight)

    def build_name(self):
        return "(name " + self.name + ")"

    def build_domain(self):
        if self.pos == "noun":
            arg = "x"
        else:
            arg = "e0"
        return "(S#" + self.domain.upper() + " " + arg + " :" \
          + self.weight + ")"

    def build_subdomain(self):
        if self.pos == "noun":
            arg = "x e0"
        elif  self.pos == "adjective":
            arg = "e0 e0"
        elif self.pos == "verb":
            arg = "e0 e0"
        return "(SS#" + self.subdomain + " " + arg + " :" + self.weight + ")"

    def build_role(self, role):
        if role:
            arg = "x e0"
            return "(R#" + role.upper() + " " + arg + " :" + self.weight + ")"
        else:
            return ""

    def build_left_side(self):
        roles = ""
        lsdomain = self.build_domain()
        lssubdomain = self.build_subdomain()
        for role in [self.r1, self.r2, self.r3, self.r4]:
            roles += self.build_role(role)
        return "(^" + lsdomain + lssubdomain + roles + ")"

    def assign_posTag(self, text):
        if text.lower() == "noun":
            return "nn"
        if text.lower() == "verb":
            return "vb"
        if text.lower() == "adjective":
            return "adj"

    def build_right_side(self):
        tag = self.assign_posTag(self.pos)
        if not self.dash:
            if tag == "nn":
                body = "(" + self.name + "-" + tag + " e0 x)"
            if tag == "vb":
                body = "(" + self.name + "-" + tag + " e0 x y z)"
            if tag == "adj":
                body = "(" + self.name + "-" + tag + " e0 x)"
            return body
        else:
            words = self.name.split("-")
            if tag == "nn":
                body = "(" + words[0] + "-" + tag + " e0 x)"
            if tag == "vb":
                body = "(" + words[0] + "-" + tag + " e0 x y u)"
            if tag == "adj":
                body = "(" + words[0] + "-" + tag + " e0 x)"
            leftovers = ""
            for word in words[1:]:
                leftovers += "(" + word + "- )"
            return "(^" + body + leftovers + ")"

    def build_full_axiom(self):
        outname = self.build_name()
        ls = self.build_left_side()
        rs = self.build_right_side()
        return '(B ' + outname + '(=>' + ls + ' ' + rs + '))'


def determine_weight(d, sd, r1, r2, r3, r4):
    elements = 0
    for v in locals().values():
        if v is not None:
            if type(v) == str:
                elements += 1
    weight = round(0.9/elements, 2)
    return weight


def main():
    parser = argparse.ArgumentParser(description='Build lexical axioms.')
    parser.add_argument('-n', '--name', required=True,
                        help='The name of the word to be axiomatized. '
                        'Should be the lemma of the word. '
                        'Required to build an axiom.')
    parser.add_argument('-p', '--pos', required=True,
                        help='Part of speech for the lexical entry. '
                        'Must be one of: noun, verb, adjective. '
                        'Required to build an axiom.')
    parser.add_argument('-d', '--domain', required=True,
                        help='The domain of the lexical entry. '
                        'Required to build an axiom.')
    parser.add_argument('-s', '--subdomain', required=True,
                        help='The subdomain of the lexical entry. '
                        'If none is provided, the output will have only a '
                        'domain.')
    parser.add_argument('--role',
                        help='Role that the word being axiomatized expects '
                        'to be filled.')
    parser.add_argument('--role2',
                        help='Second role that the word being axiomatized '
                        'expects to be filled.')
    parser.add_argument('--role3',
                        help='Third role that the word being axiomatized '
                        'expects to be filled.')
    parser.add_argument('--role4',
                        help='Fourth role that the word being axiomatized '
                        'expects to be filled.')
    parser.add_argument('--output', default=None,
                        help='Output file. Default is stdout.')
    pa = parser.parse_args()

    axName = str(pa.name).lower()
    axPOS = str(pa.pos).lower()
    axDomain = str(pa.domain)
    axSubdomain = str(pa.subdomain)
    axRole = str(pa.role) if pa.role else None
    axRole2 = str(pa.role2) if pa.role2 else None
    axRole3 = str(pa.role3) if pa.role3 else None
    axRole4 = str(pa.role4) if pa.role4 else None
    weight = determine_weight(axDomain, axSubdomain, axRole, axRole2, axRole3,
                              axRole4)
    template = Template(axPOS, axName, axDomain, axSubdomain, axRole, axRole2,
                        axRole3, axRole4, weight)
    print template.build_full_axiom()


if __name__ == '__main__':
    main()
