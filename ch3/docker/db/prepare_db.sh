#!/bin/sh
set -e

/opt/code/db/start_postgres.sh

echo 'Creating Schema'
python3 /opt/code/init_db.py

echo 'Loading initial data'
python3 /opt/code/load_from_csv.py -f /opt/code/db/input.txt

/opt/code/db/stop_postgres.sh
