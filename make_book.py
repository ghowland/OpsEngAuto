#!/usr/bin/python

"""
Throw-away program to generate a book.  Not meant to be re-usable at this point,
and not a full life-cycle yet, but getting me up and running in the method I
want to write the book sections and TOC in.
"""


import hashlib
import pprint
import time
import os
import glob


#DEBUG=True
DEBUG=False


OUT_PATH = 'book.html'
OUT_GIT_PATH = 'README.md'
IN_PATH = '_toc_details.yaml'

# Directory to backup current TOC IN_PATH file, as we make changes to it, so it cannot be corrupted by the automated changes
TOC_BACKUP_DIR = '__toc_backups'

# This is what we will append to lines.  It basically pushes it off the screen in non-word-wrap mode, which is good enough for me.
#NOTE(g): Making it so these spaces can be deleted, the parser wont care.  Its just to make reading easy.
SECTION_TAG_STRING = '%-500s [[%s]]'

# This is where our Section Tag files will go
SECTION_DIR = 'sections'


def Report__SectionsPopulated():
  """Prints out how many sections have been populated."""
  glob_path = '%s/*' % SECTION_DIR
  paths = glob.glob(glob_path)
  
  populated = []
  
  for path in paths:
    lines = open(path).read().split('\n')
    
    # Simple line count check.  Not enough lines?  Not populated.
    if len(lines) > 4:
      populated.append(path)
    
  
  print 'Populated Sections: %s' % len(populated)


def Report__SectionsAbandoned():
  """Prints out how many sections no longer have references in the TOC."""
  #TODO(g): If these are empty just move them to the backup directory (deleted, effectively).  Use git commands, since this is in the repo now.
  pass
  
  #NOTE(g): Look for non-empty files with no references from TOC and list them, so I can edit them and move their content into other sections and not lose them.  Manually delete.
  pass


def OutputSectionGitMarkDown(section_dict, header_prefix=None, depth=0):
  """GitHub MarkDown Output section, and recurse through sub-sections."""
  output = ''
  
  #print 'DEBUG: %s' % section_dict
  
  # Split the title and section tag out of this entry
  (title, section_tag) = section_dict['title'].split(' [[', 1)
  title = title.strip()
  section_tag = section_tag.split(']]', 1)[0]
  
  
  # Build section file path
  #TODO(g): Switch this to HTML after processing with Jinja to template out vars
  section_path = '%s/%s.txt' % (SECTION_DIR, section_tag)
  
  
  # Chapter header
  if depth == 0:
    label = 'Chapter %s: %s' % (header_prefix, title)
    
    output += '# %s\n' % label
    
  # H2 to H3, beyond that is just paragraph headers?
  elif depth < 3:
    label = '%s: %s' % (header_prefix, title)
    
    line_prefix = '#' * depth
    
    output += '%s %s</h%d>\n' % (line_prefix, label)
  
  # Else, deeper, not using HTML headers
  else:
    label = '%s: %s' % (header_prefix, title)
    
    output += '#### %s\n' % label
  
  
  # If we dont have the section path, create it from our title label
  if not os.path.isfile(section_path):
    raise Exception('Section path not found, this should have been handled in HTML output: %s' % section_path)
  
  # Else, we do have it, so read it in and put it under the section header
  else:
    section_content = open(section_path).read()
  
  
  # Print the section contents to our ouput (under our section header, which this is the content for)
  for line in section_content.split('\n'):
    # Skip the comment lines out (comments start with: ###)
    if not line.strip().startswith('###'):
      output += '%s\n\n' % line
  
  
  # If this section has children, output them too
  if section_dict['children']:
    count = 0
    for section_child_dict in section_dict['children']:
      count += 1
      cur_header_prefix = '%s.%s' % (header_prefix, count)
      output += OutputSection(section_child_dict, header_prefix=cur_header_prefix, depth=depth+1)
  
  
  return output


def OutputSection(section_dict, header_prefix=None, depth=0):
  """Output section, and recurse through sub-sections."""
  output = ''
  
  #print 'DEBUG: %s' % section_dict
  
  # Split the title and section tag out of this entry
  (title, section_tag) = section_dict['title'].split(' [[', 1)
  title = title.strip()
  section_tag = section_tag.split(']]', 1)[0]
  
  
  # Build section file path
  #TODO(g): Switch this to HTML after processing with Jinja to template out vars
  section_path = '%s/%s.txt' % (SECTION_DIR, section_tag)
  
  
  # Chapter header
  if depth == 0:
    label = 'Chapter %s: %s' % (header_prefix, title)
    label_html = '<a href="#%s">Chapter %s</a>: %s' % (section_tag, header_prefix, title)
    output += '<h1 id=%s>%s</h1>\n' % (section_tag, label_html)
    
  # H2 to H3, beyond that is just paragraph headers?
  elif depth < 3:
    label = '%s: %s' % (header_prefix, title)
    label_html = '<a href="#%s">%s</a>: %s' % (section_tag, header_prefix, title)
    
    output += '<h%d id=%s>%s</h%d>\n' % (depth + 1, section_tag, label_html, depth + 1)
  
  # Else, deeper, not using HTML headers
  else:
    label = '%s: %s' % (header_prefix, title)
    label_html = '<a href="#%s">%s</a>: %s' % (section_tag, header_prefix, title)
    
    output += '<p id=%s><b>%s</b></p>\n' % (section_tag, label_html)
  
  
  # If we dont have the section path, create it from our title label
  if not os.path.isfile(section_path):
    section_content = '### [[%s]]\n\n\n' % label
    open(section_path, 'w').write(section_content)
  
  # Else, we do have it, so read it in and put it under the section header
  else:
    section_content = open(section_path).read()
  
  
  # Print the section contents to our ouput (under our section header, which this is the content for)
  for line in section_content.split('\n'):
    # Skip the comment lines out (comments start with: ###)
    if not line.strip().startswith('###'):
      output += '%s\n\n' % line
  
  
  # If this section has children, output them too
  if section_dict['children']:
    count = 0
    for section_child_dict in section_dict['children']:
      count += 1
      cur_header_prefix = '%s.%s' % (header_prefix, count)
      output += OutputSection(section_child_dict, header_prefix=cur_header_prefix, depth=depth+1)
  
  
  return output


def Main():
  """Make an HTML book."""
  text = open(IN_PATH).read()
  
  lines = text.split('\n')
  
  # Dict of dicts (of list of dicts, embedded), keys are integers all the way down
  table_of_contents = []
  
  INDENT_SPACE_COUNT = 2
  
  # Make a parse for YAML-like list, that doesnt quote things (for ease of entry)
  cur_depth = 0
  cur_dict = None
  last_depth = 0
  
  # Track chapters (each depth==0 item is a chapter)
  cur_chapter = 0
  
  # Stats
  total_sections = 0
  
  # As we process each line, we may need to edit it to add a section tag (suffix: "[[md5sum]]")
  toc_rewrite_output = ''
  
  # Process all lines
  for line in lines:
    
    # Skip empties
    if not line.strip():
      toc_rewrite_output += line + '\n'
      continue
    
    # -- Parse Line --
    
    # Keep this for the TOC output
    original_line = line
    
    # Test how many indenting spaces this has
    cur_indent_spaces = 0
    while line.startswith(' '):
      cur_indent_spaces += 1
      line = line[1:]
  
    # Cut off the leading "- "
    line = line[2:]
    
    # -- Calculate --
    
    # Calculate depth and chapter
    cur_depth = cur_indent_spaces / INDENT_SPACE_COUNT
  
    # If we are a top-level item, we are a new chapter
    if cur_depth == 0:
      cur_chapter += 1
    
    
    #if cur_chapter > 3:#DEBUG, skip after chap N.  Formatting has to be perfect, because of the ghetto-depth tracking.
    #  continue
    
    # -- Build TOC Dicts --
    
    
    # Debug
    if DEBUG:
      print 'Depth: %s  Chapter: %s  Line: %s' % (cur_depth, cur_chapter, line)
    
    
    # Check if this title has the Section Tag on the end of it [[md5sum]]
    if '[[' not in original_line:
      # Create a unique digest which identifies this section, so we can use it to build all our text files
      digest = hashlib.md5('%s.%s' % (time.time(), original_line)).hexdigest()
      original_line = SECTION_TAG_STRING % (original_line, digest)
      
      # Modify the working line too, since we are going to operate on it right after this, and need this data
      line = SECTION_TAG_STRING % (line, digest)
      
    
    # If we are a top-level item, we are a new chapter
    if cur_depth == 0:
      
      # If we dont have this chapter yet, add it
      if cur_chapter not in table_of_contents:
        cur_section = {'title':line, 'children':[], 'parent':None}
        total_sections += 1
        
        # Add to top level
        table_of_contents.append(cur_section)
        
        # This chapter is now the current dictionary, we will add sub-items to this
        cur_dict = cur_section
        
        # Our last depth is now 0, because we have reset.  This goes deeper, until it meets something less-deep, and then receeds back to that point
        last_depth = 0
    
    
    # Else, this is a sub-chapter item
    else:
      #print 'Cur Depth: %s   Last Depth: %s' % (cur_depth, last_depth)
      
      # Find out parent.  If this is a sub-depth, then we are already at our parent.  If it is the same level as before, we go to our common parent.  If deeper up, then we go up until we reach the common parent for that level of children.
      while cur_depth <= last_depth:
        cur_dict = cur_dict['parent']
        
        #print 'Current: %s   Last: %s --> %s' % (cur_depth, last_depth, last_depth-1)
        last_depth -= 1
      
      # Create the new sub-chapter entry
      cur_section = {'title':line, 'children':[], 'parent':cur_dict}
      total_sections += 1
      
      # Add this to our parent (cur_dict is parent now)
      cur_dict['children'].append(cur_section)
      
      # Now we become the cur_dict, ready to parent new children
      cur_dict = cur_section
      
      # Set to current depth
      last_depth = cur_depth
    
    
    
    # Add the original line (which we may have modified actually, so its a misnomer, but only halfway)
    toc_rewrite_output += original_line + '\n'
  
  
  # -- Output --
  
  # Debug: Print full table of contents dicts
  if DEBUG:
    pprint.pprint(table_of_contents)
  
  
  # Print the HTML
  output = ''
  count = 0
  for cur_section in table_of_contents:
    count += 1
    output += OutputSection(cur_section, header_prefix=str(count))
  
  fp = open(OUT_PATH, 'w').write(output)
  
  
  # Print the GitHub MarkDown
  output = '# Operations Engineering and Automation\n\n\n'
  count = 0
  for cur_section in table_of_contents:
    count += 1
    output += OutputSectionGitMarkDown(cur_section, header_prefix=str(count))
  
  fp = open(OUT_GIT_PATH, 'w').write(output)
  
  
  # Test if we need to rewrite the TOC file
  if toc_rewrite_output.rstrip() == text.rstrip():
    print '\n- Nothing changed.  No rewrite necessary.'
  
  # Else, something changed, so we need to make a backup and re-write the original file
  else:
    backup_path = '%s/%s' % (TOC_BACKUP_DIR, IN_PATH)
    print '\n- Rewrite necessary:  Updated: %s    Backup: %s' % (IN_PATH, backup_path)
    
    # Write the original to our TOC backup dir
    open(backup_path, 'w').write(text)
    
    # Write over our original with the new-updated TOC
    open(IN_PATH, 'w').write(toc_rewrite_output.rstrip() + '\n\n')
    #open('%s.rewrite' % IN_PATH, 'w').write(toc_rewrite_output.rstrip())
  
  print '\n\nTotal Sections: %s' % total_sections
  
  # Look at how many sections actually have data in them
  Report__SectionsPopulated()
  
  #TODO(g): Look for abandoned sections (no TOC reference)
  Report__SectionsAbandoned()
  
  print
  print


if __name__ == '__main__':
  Main()
