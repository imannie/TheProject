import sys
from utils import (
                   build,
                   new,
                   )

usage = """ usage:
            Rebuild site: python manage.py build
            Create new pages blog post: python manage.py new
        """
def main():
    try:
        command = sys.arg[1]
    except:
        print(usage)
        return
    if command == 'build':
        build()
    elif command == 'new':
        new()

if __name__=='__main__':
    main()

