# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details. 

def singular(plural):
    """
    Take a plural English word and turn it into singular

    Obviously, this doesn't work in general. It know just enough words to
    generate XML tag names for list items. For example, if we have an element
    called 'tracks' in the response, it will be serialized as a list without
    named items in JSON, but we need names for items in XML, so those will be
    called 'track'.
    """
    if plural.endswith('ies'):
        return plural[:-3] + 'y'
    if plural.endswith('s'):
        return plural[:-1]
    raise ValueError('unknown plural form %r' % (plural,))