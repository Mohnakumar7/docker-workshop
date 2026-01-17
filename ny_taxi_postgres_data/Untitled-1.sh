
uv run python3 ingest_data.py \
  --network=pg-network \
  --year=2021 \
  --month=1 \
  --pg-user=root \
  --pg-pass=root \
  --pg-db=ny_taxi \
  --pg-host=localhost \
  --pg-port=5432 \
  --chunksize=100000 \
  --target-table=yellow_taxi_trips_2021_1


docker run -it --rm  \
  --network=pipeline_pg-network \
  taxi_ingest:v001 \
    --year=2021 \
    --month=1 \
    --pg-user=root \
    --pg-pass=root \
    --pg-db=ny_taxi \
    --pg-host=pg-database \
    --pg-port=5432 \
    --chunksize=100000 \
    --target-table=yellow_taxi_trips_2021_1


docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:18

  docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4