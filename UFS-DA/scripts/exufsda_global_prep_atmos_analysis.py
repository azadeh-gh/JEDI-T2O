#!/usr/bin/env python3
################################################################################
####  UNIX Script Documentation Block
#                      .                                             .
# Script name:         exufsda_global_prep_atmos_analysis.py
# Script description:  Stages files and generates YAML for UFS Global Atmosphere Analysis
#
# Author: Cory Martin      Org: NCEP/EMC     Date: 2021-12-21
#
# Abstract: This script stages necessary input files and produces YAML
#           configuration input file for FV3-JEDI executable(s) needed
#           to produce a UFS Global Atmospheric Analysis.
#
# $Id$
#
# Attributes:
#   Language: Python3
#
################################################################################

# import os and sys to add ush to path
import os
import sys

# get absolute path of ush/ directory either from env or relative to this file
sys.path.append(os.path.join(os.getenv('HOMEgfs', os.path.dirname(os.path.dirname(__file__))), 'ush'))
print(f"sys.path={sys.path}")

# import UFSDA utilities
import ufsda

# get COMOUT from env
COMOUT = os.getenv('COMOUT', './')

# create analysis directory for files
ufsda.mkdir(os.path.join(COMOUT, 'analysis'))
