from os.path import isdir
from os import listdir

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return recurse_files(suffix, path, [])
  
def recurse_files(suffix, path, matched_suffix):
    if suffix == '':
          return []
    list_dir = listdir(path)
    for i in list_dir:
          ele = path+'/'+i
          if ele is None:
                continue
          if isdir(ele):
                recurse_files(suffix, ele, matched_suffix)
          elif ele.endswith(suffix):
                matched_suffix.append(ele)
    return matched_suffix

print(find_files('.c', './testdir'))

#Test One - Basic Test for file extensions
files = find_files('.c', './testdir')
expected_files = ['./testdir/t1.c', './testdir/subdir1/a.c','./testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c']
has_files = True
for i in files:
      if i not in expected_files:
          has_files == False  
print(has_files) # == True

files = find_files('.h', './testdir')
expected_files = ['./testdir/t1.h', './testdir/subdir1/a.h','./testdir/subdir5/a.h', './testdir/subdir3/subsubdir1/b.h']
has_files = True
for i in files:
      if i not in expected_files:
          has_files == False  
print(has_files) # == True

# Test Two - Check for extensions that dont exist
files = find_files('.xls', './testdir')
print(files) # == []
files = find_files('', './testdir')
print(files) # == []

#Test Three Null Check
has_error = False
try:
  files = find_files(None, './testdir')
except:
  has_error = True

print(files) # == []
print(has_error) # == True
