#!/usr/bin/env python3

import os
import yaml
import sys
  
# This is to get the directory that the program  
# is currently running in. 
dir_path = os.getcwd()

TEMPLATESDIR = sys.argv[1]
JOBFILE = sys.argv[2]


children = {}

builds = []
for root, dirs, files in os.walk(TEMPLATESDIR):
    for file in files:
        builds.append(file.removesuffix('.yaml'))

#print(builds)

for root, dirs, files in os.walk(dir_path): 
    for file in files:
        if file in builds:
            the_path = os.path.join(root,file)
            if file not in children:
                children[file] = []
            folder = os.path.dirname(os.path.relpath(the_path, start = os.curdir))
            children[file].append(folder)

#print(children)

new_jobs = {}
for key in children:
    for fname in children[key]:
        templatename = 'citemplates/'+key+'.yaml'
        yamlfile = open(templatename)
        template = yaml.load(yamlfile, Loader=yaml.SafeLoader)
        yamlfile.close()
        print(template)
        template['script'] = [s.replace('AUTOGENPROJECT', fname) for s in template['script']]
        job_name = template['stub'] + '-' + fname 
        new_jobs[job_name] = template
        new_jobs[job_name].pop('stub')


jobfile=open(JOBFILE,'w')
yaml.dump(new_jobs,jobfile)
jobfile.close()

