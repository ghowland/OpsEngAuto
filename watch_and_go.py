#!/usr/bin/python

"""
Throw-away program to watch for changes and run the "go.sh" script if they are found, which will update things.
"""


import time
import os
import glob
import stat
import commands


# What we run
GO_COMMAND = './go.sh'

# How long between checking if we need to run our thing
SLEEP_INTERVAL = 4

# Where we look for changes
glob_paths = ['_toc_details.yaml', 'sections/*']

# Initial updated time
last_updated_time = None


print '\n\nI am the watcher.  I am watching: %s\n\n' % glob_paths


# Loop forever, we watch
while True:
  # Get all the paths in our glob paths
  paths = []
  
  for glob_path in glob_paths:
    cur_paths = glob.glob(glob_path)
    
    paths += cur_paths
  
  # Our test
  updated = False
  latest_mtime = None
  
  # Check all our paths latest MTIMEs.  If never than last_updated_time or last_updated_time==None, then GO!
  for path in paths:
    mtime = os.stat(path)[stat.ST_MTIME]
    
    # If this path has changed mtime (updated)
    if not last_updated_time or mtime > last_updated_time:
      updated = True
      
      # We cant break here, as we need to find the latest MTIME, and the first match may not be the latest
      if latest_mtime == None or mtime > latest_mtime:
        latest_mtime = mtime
        print 'Updated path: %s: %s' % (path, mtime)
  
  
  # If one of our files was updated, do the thing
  if updated:
    (status, output) = commands.getstatusoutput(GO_COMMAND)
    
    # If failed, report error.  Git returns 1 for not needed to do work.
    if status not in (0, 1):
      print '\n%s: Error running: %s: %s: %s\n' % (time.asctime(time.localtime(time.time())), GO_COMMAND, status, output)
    
    # Else, report success
    else:
      print '%s: Updated' % time.asctime(time.localtime(time.time()))
  
  
  # Sleep, so we arent spinning constantly
  time.sleep(SLEEP_INTERVAL)
  
  