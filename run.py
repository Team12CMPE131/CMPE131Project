from app import myapp
import sys

debug_mode = False

if '-d' in sys.argv:
    print('debug on')
    debug_mode = True
    
myapp.run(debug=debug_mode)