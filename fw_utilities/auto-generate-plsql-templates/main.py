#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main module for auto-generating PL/SQL templates

Author: [Author Name]
Date: [Creation Date]
Description: This module generates PL/SQL package specifications and bodies
             based on user input parameters.
"""

from functions import *

lista=get_initial_parameters()
print("Parmetri inseriti: ")

for i in range(len(lista)):
    print("Parametro "+str(i)+" .....: "+lista[i])

print("creazione del PACKAGE HEAD...: ")

crea_spec_code(lista)
print("FATTO ")

print(RIGA_VUOTA)
print(RIGA_VUOTA)

print("creazione del PACKAGE BODY...: ")
crea_body_code(lista)
print("FATTO ")
print("Files creati in: outfiles")