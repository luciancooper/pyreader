import os

def ask_permission(path):
    resp = input("include '{}' [y/n]:".format(path))
    return resp.lower() == 'y'

def find_pyfiles(path,recursive,ask):
    #print("find_pyfiles '{}'".format(path))
    for f in [os.path.join(path,x) for x in os.listdir(path)]:
        #print("f '{}'  dir:{}".format(f,os.path.isdir(f)))
        if not os.path.isdir(f):
            if f.endswith('.py') and (ask==0 or ask_permission(f)):
                yield f
            continue
        if recursive:# and (ask<1 or ask_permission(f)):
            for rf in find_pyfiles(f,recursive,ask):
                yield rf
