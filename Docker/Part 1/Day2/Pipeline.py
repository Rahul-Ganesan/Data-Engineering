import sys
import pandas as pd

print(sys.argv)
day = sys.argv[1]

print(f'job finished successfully for day = {day}')

"""
CMDs

docker run -it  -e POSTGRES_USER="root"  -e POSTGRES_PASSWORD="root"  -e POSTGRES_DB="ny_taxi"  -v E:/New folder/MOOC/Docker/Part 1/Day2/ny_taxi_postgres_data:/var/lib/postgresql/data  -p 5432:5432 postgres:13

"""