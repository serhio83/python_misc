#!/usr/bin/env python
import os
import re
import subprocess
# How it works:
# First import vars
# export COMPONENTS_PARAMS='fbs/fms feature/FMS-124, fbs/cabinet release_xxx, fbs/verification-crm v2.2.1'
# then run script
ver_regexp = re.compile(r'v[0-9]+\.[0-9]+\.[0-9]+')
params = os.environ.get('COMPONENTS_PARAMS')
workdir = os.getcwd()
if params:
    for component in params.split(','):
        comp = component.strip().split()
        os.chdir(workdir+'/vendor/'+comp[0])
        print 'checkout component: vendor/{}, version: {}'.format(comp[0], comp[1])
        if ver_regexp.match(comp[1]):
            try:
                subprocess.check_call(["git", "checkout", "tags/"+comp[1]])
            except subprocess.CalledProcessError as e:
                print 'subprocess returned: {} '.format(e.returncode)
            else:
                print 'ok'
        else:
            try:
                subprocess.check_call(["git", "checkout", "origin/"+comp[1]])
            except subprocess.CalledProcessError as e:
                print 'subprocess returned: {} '.format(e.returncode)
            else:
                print 'ok'
