from app import myapp, db
import sys

debug_mode = False

if '-r' in sys.argv:
    print('Refreshing database')
    db.drop_all()
    db.create_all()
elif '-R' in sys.argv:
    print('Refreshing...')
    db.drop_all()
    db.create_all()
    print('Done!')
    quit()
else:
    print('Reusing database')
    
if '-d' in sys.argv:
    print('debug on')
    debug_mode = True
    
myapp.run(debug=debug_mode)