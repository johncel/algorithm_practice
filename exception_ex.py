import traceback 
import sys

try:
    result = 10 / 0

except ZeroDivisionError as e:
    print(f'error: {e}')
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('*** print_tb:')
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

finally:
    print(f'finally this is over, phew!')
    # traceback.print_exc(file=sys.stdout)
