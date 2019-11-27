import sys
import traceback
from easysnmp import Session

if len(sys.argv) != 2:
    print('Usage: python resetter.py PRINTER_IP')
    sys.exit('Error: Missing printer IP')

PRINTER_IP = sys.argv[1]

try:
    session = Session(hostname=PRINTER_IP, community='public', version=1)
    object_ids = [
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.48.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.49.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.47.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.50.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.51.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.47.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.115.116.1.0.1',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.68.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.69.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.70.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.71.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.72.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.73.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.74.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.75.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.76.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.7.0.73.8.65.190.160.76.6',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.118.105.1.0.0',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.115.116.1.0.1',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.48.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.49.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.47.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.52.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.53.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.54.0.94.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.50.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.51.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.47.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.55.0.94.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.124.124.16.0.73.8.66.189.33.28.0.0.66.115.98.111.117.106.103.112',
        '1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1.99.100.1.0.0',
    ]

    for id in object_ids:
        response = session.get(id)
        print(response)

except Exception as e:
    print(f'Error connecting to the printer. Verify the printer\'s IP is {PRINTER_IP}.')
    print()
    print(traceback.print_tb(e.__traceback__))