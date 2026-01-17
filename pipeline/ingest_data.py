import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


def run(
    year: int = 2021,
    month: int = 1,
    pg_user: str = "root",
    pg_pass: str = "root",
    pg_db: str = "ny_taxi",
    pg_host: str = "localhost",
    pg_port: int = 5432,
    chunksize: int = 100000,
    target_table: str = "yellow_taxi_data",
):
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"
    engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(n=0).to_sql(name=target_table,
                                      con=engine, if_exists="replace")
            first = False

        df_chunk.to_sql(name=target_table, con=engine, if_exists="append")


@click.command()
@click.option("--year", default=2021, type=int, help="Year of the dataset")
@click.option("--month", default=1, type=int, help="Month of the dataset (1-12)")
@click.option("--pg-user", default="root", help="Postgres username")
@click.option("--pg-pass", default="root", help="Postgres password")
@click.option("--pg-db", default="ny_taxi", help="Postgres database name")
@click.option("--pg-host", default="localhost", help="Postgres host")
@click.option("--pg-port", default=5432, type=int, help="Postgres port")
@click.option("--chunksize", default=100000, type=int, help="CSV read chunksize")
@click.option("--target-table", default="yellow_taxi_data", help="Target DB table name")
def main(year, month, pg_user, pg_pass, pg_db, pg_host, pg_port, chunksize, target_table):
    run(
        year=year,
        month=month,
        pg_user=pg_user,
        pg_pass=pg_pass,
        pg_db=pg_db,
        pg_host=pg_host,
        pg_port=pg_port,
        chunksize=chunksize,
        target_table=target_table,
    )


if __name__ == '__main__':
    main()

