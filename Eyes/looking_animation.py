import time

def looking():
    print(
        '''
  ____   ____
 /    \ /    \\
|      ||     |'''
    )
    while True:
        print('\r', "\  o / \   o/", end='')
        time.sleep(.75)
        print('\r', "\ o  / \  o /", end='')
        time.sleep(.75)
        print('\r', "\o   / \ o  /", end='')
        time.sleep(.75)
        print('\r', "\ o  / \  o /", end='')
        time.sleep(.75)