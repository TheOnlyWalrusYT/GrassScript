import sys
import importlib

if len(sys.argv) != 2:
    print('Usage: %s <script.gs>' % sys.argv[0])
    sys.exit(1)

if sys.argv[1][-3:] != '.gs':
    print('GrassScript files end in \'.gs\'!')
    sys.exit(1)

sys.path.insert(0, './grass-modules')

with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if not line or (line[0] == ';' and line[1] == ';'):
            continue
        parts = line.split()
        mod = importlib.import_module(parts[0])
        if parts[0] == 'gmath':
            try:
                getattr(mod, parts[1])(parts[2], parts[3], parts[4])
            except:
                print('Missing Argument(s) or Incorrect Module')
                sys.exit(1)
        elif parts[0] == 'grass':
            try:
                getattr(mod, parts[1])(parts[2])
            except:
                print('Missing Argument(s) or Incorrect Module')
                sys.exit(1)
