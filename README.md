# Canasta Rosa
Entrevista tecnica canasta rosa python developer

# Curl scripts

## Store

### Post

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

### Get

curl --location --request GET 'localhost:8000/store/' \
--header 'Content-Type: application/json'

## Product

### Post

curl --location --request POST 'localhost:8000/product/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name":"product_test7",
	"slug":"product_test7",
	"price": 102.10,
	"elaboration_time": 0,
	"store": 2
}'

### Get

curl --location --request GET 'localhost:8000/product/'


## Order

### Post


#### Error 

curl --location --request POST 'localhost:8000/order/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"store": 2,
	"products": [5,7],
	"delivery_date": "2020-02-05",
	"order_price": 0.00
}'

#### Success

curl --location --request POST 'localhost:8000/order/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"store": 2,
	"products": [7],
	"delivery_date": "2020-02-05",
	"order_price": 0.00
}' 