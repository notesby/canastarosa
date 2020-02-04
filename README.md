# Canasta Rosa
Entrevista tecnica canasta rosa python developer

# Curl scripts

## Post

curl --location --request POST 'localhost:8000/store/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test",
    "slug": "test",
    "store_schedules": [
        {
            "weekday": 1,
            "opens": "10:10",
            "closes": "12:12"
        },
        {
            "weekday": 2,
            "opens": "10:10",
            "closes": "12:12"
        },
        {
            "weekday": 3,
            "opens": "11:10",
            "closes": "20:12"
        }
    ]
}'

## Get

curl --location --request GET 'localhost:8000/store/' \
--header 'Content-Type: application/json'