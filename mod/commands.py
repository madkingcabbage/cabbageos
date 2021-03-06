from colors import *
import file

def returnColor(arg):
  color = arg.lower()
  if color == 'black':
    return BLACK
  elif color == 'red':
    return RED
  elif color == 'green':
    return GREEN
  elif color == 'yellow':
    return YELLOW
  elif color == 'blue':
    return BLUE
  elif color == 'magenta':
    return MAGENTA
  elif color == 'cyan':
    return CYAN
  elif color == 'light-grey':
    return LIGHT_GREY
  elif color == 'light-gray':
    return LIGHT_GRAY
  elif color == 'dark-gray':
    return DARK_GRAY
  elif color == 'dark-grey':
    return DARK_GREY
  elif color == 'light-red':
    return LIGHT_RED
  elif color == 'light-green':
    return LIGHT_GREEN
  elif color == 'light-yellow':
    return LIGHT_YELLOW
  elif color == 'light-blue':
    return LIGHT_BLUE
  elif color == 'light-magenta':
    return LIGHT_MAGENTA
  elif color == 'light-cyan':
    return LIGHT_CYAN
  elif color == 'white':
    return WHITE
  else:
    return 1

def returnProbe():
  files = file.parseLs("files/computers.txt")
  returnList = []
  for elem in files:
    returnList.append(file.load("defaults/" + elem, 'ip'))
  returnStr = ""
  elems = len(returnList)
  iterations = 0
  for elem in returnList:
    iterations += 1
    if iterations != elems:
      returnStr += elem + '\n'
    else:
      returnStr += elem
  return returnStr
