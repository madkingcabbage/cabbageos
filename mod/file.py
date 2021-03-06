import json
from ast import literal_eval

# A guide to adding a new file var:
# First, add a var to parse;
# Then, add a var to save;
# Last, add a var to load.
# Next add the var and a var container to hack.py.
# After that, do the same for the write, save, and load functions in hack.py.
# Then for the remoteLoad function.
# Then remoteReset.

def init(username, dirs, files):
  
  # Syntax for dirs is: name, isRootDir, parent, contents
  dirs = [['/', '1', 'thereisnoparent', []], ['home', '0', '/', []]]

  # Syntax for files is: name, parent, contents
  files = [['welcome.txt', '/', "Welcome to cabbageOS! Type 'help' for a list of commands."], ['luck.txt', 'home', "Good luck!"], ['for_help.txt', 'home', "If you're looking for help, try inf_serv at 65.61.234.21. Username is info_server and password is tellmeyoursecrets!"]]

  strDirs = str(dirs)
  strFiles = str(files)
  savFile = open('saves/%s/%s.sav' % (username, username), 'a')
  savFile.write("<%s>\n<%s>\ncrackSecure: <1>" % (strDirs, strFiles))

def refresh(dirs, files):
  for comp1 in dirs:
    comp1[3] = []
    for file in files:
      if file[1] == comp1[0]:
        comp1[3].append(file[0])
    for comp2 in dirs:
      if comp1[0] == comp2[2]:
        comp1[3].append(comp2[0])

def parseLs(parseFile):
  savFile = open(parseFile, 'r')
  fileStr = savFile.read()
  savFile.close()
  read = 1
  updateRead = 0
  container = ''
  returnList = []
  for elem in fileStr:
    if elem == '\n':
      read = 0
      updateRead = 1
      returnList.append(container)
      container = ''
    if read == 1:
      container += elem
    if updateRead == 1:
      read = 1
  return returnList

def parse(file, mode):
  sav = open(file, 'r')
  savStr = sav.read()
  read = 0
  tries = 0
  updateRead = 0
  trueUsername = ''
  truePassword = ''
  trueHostname = ''
  strDirs = ''
  strFiles = ''
  ip = ''
  crackSecure = ''
  sysColor0 = ''
  sysColor1 = ''
  for elem in savStr:
    if read == 0:
      if elem == '<':
        updateRead = 1
    if elem == '>':
      read = 0  
      tries += 1
    if read == 1:
      if tries == 0:
        trueUsername += elem
      elif tries == 1:
        truePassword += elem
      elif tries == 2:
        trueHostname += elem
      elif tries == 3:
        ip += elem
      elif tries == 4:
        strDirs += elem
      elif tries == 5:
        strFiles += elem
      elif tries == 6:
        crackSecure += elem
      elif tries == 7:
        sysColor0 += elem
      elif tries == 8:
        sysColor1 += elem
    if updateRead == 1:
      read = 1
      updateRead = 0
  sav.close()
  if mode == 'username':
    return(trueUsername)
  elif mode == 'password':
    return(truePassword)
  elif mode == 'hostname':
    return(trueHostname)
  elif mode == 'files':
    return(strFiles)
  elif mode == 'dirs':
    return(strDirs)
  elif mode == 'ip':
    return(ip)
  elif mode == 'crackSecure':
    return(crackSecure)
  elif mode == 'sysColor0':
    return(sysColor0)
  elif mode == 'sysColor1':
    return(sysColor1)
  elif mode == 'all':
    return([trueUsername, truePassword, hostname, ip, strFiles, strDirs, crackSecure])

def write(file, *args):
  savFile = open(file, 'w')
  for elem in args:
    strElem = str(elem)
    myStr = '<' + strElem + '>'
    savFile.write(myStr)
  savFile.close()

def save(dirs, files, toSavFile):
  strDirs = str(dirs)
  strFiles = str(files)
  username = parse(toSavFile, 'username')
  password = parse(toSavFile, 'password')
  hostname = parse(toSavFile, 'hostname')
  crackSecure = parse(toSavFile, 'crackSecure')
  write(toSavFile, username, password, hostname, strDirs, strFiles, crackSecure)
  
def load(toSavFile, mode):
  if mode == 'username':
    return(parse(toSavFile, 'username'))
  elif mode == 'password':
    return(parse(toSavFile, 'password'))
  elif mode == 'hostname':
    return(parse(toSavFile, 'hostname'))
  elif mode == 'files':
    savList = literal_eval(parse(toSavFile, 'files'))
    return(savList)
  elif mode == 'dirs':
    savList = literal_eval(parse(toSavFile, 'dirs'))
    return(savList)
  elif mode == 'ip':
    return(parse(toSavFile, 'ip'))
  elif mode == 'crackSecure':
    return(parse(toSavFile, 'crackSecure'))
  elif mode == 'sysColor0':
    return(parse(toSavFile, 'sysColor0'))
  elif mode == 'sysColor1':
    return(parse(toSavFile, 'sysColor1'))
  else:
    print("ERROR: Consult file.py. Code 0.") # Error code 0 here
    exit()
