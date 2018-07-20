# similar-items-api

## Overview
The api returns for a given collection of items and a query item, the most similar items to the query item 
## Requirements
Python 3.5+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m app
```

and open your browser to here:

```
http://localhost:8080//ui/
```

Your Swagger definition lives here:

```
http://localhost:8080//swagger.json
```

To launch the unit tests, run:
```
test_default_controller.py
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t app .

# starting up a container
docker run -p 8080:8080 app
```

## Examples
The following example returns the most similar items (from the passed items) to item#4 (Mini Spy Hidden Camera ...). The similar items are also ordered by their similarity.
####Request
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "data": [
    {
      "id": "item1",
      "name": "WyzeCam 1080p HD Wireless Smart Home Camera with Night Vision, 2-Way Audio, Free Cloud, for iOS and Android"
    },
    {
      "id": "item2",
      "name": "AKASO Brave 4 4K 20MP Wifi Action Camera Sony Sensor Ultra HD with EIS 30m Underwater Waterproof Camera Remote Sports Camcorder with 2 Batteries and Helmet Accessories Kit"
    },
    {
      "id": "item3",
      "name": "Samsung 360 Camera"
    },
    {
      "id": "item4",
      "name": "Mini Spy Hidden Camera,NIYPS 1080P Portable Small HD Nanny Cam with Night Vision and Motion Detective,Perfect Indoor Covert Security Camera for Home and Office"
    },
    {
      "id": "item5",
      "name": "Sandisk Ultra 32GB Class 10 SDHC UHS-I Memory Card Up to 80MB, Grey/Black (SDSDUNC-032G-GN6IN)"
    },
    {
      "id": "item6",
      "name": "Canon EOS Rebel T6 Digital SLR Camera Kit with EF-S 18-55mm f/3.5-5.6 IS II Lens (Black)"
    },
    {
      "id": "item8",
      "name": "Fire TV Stick | Basic Edition | Streaming Media Player"
    }
    
  ]
}' \
 'http://127.0.0.1:8080/similar/item4'
```
####Response
```
{
"data":[
{
"id": "item1",
"name": "WyzeCam 1080p HD Wireless Smart Home Camera with Night Vision, 2-Way Audio, Free Cloud, for iOS and Android",
"similarity": 0.21210023172176612
},
{
"id": "item3",
"name": "Samsung 360 Camera",
"similarity": 0.07240380080811215
},
{
"id": "item2",
"name": "AKASO Brave 4 4K 20MP Wifi Action Camera Sony Sensor Ultra HD with EIS 30m Underwater Waterproof Camera Remote Sports Camcorder with 2 Batteries and Helmet Accessories Kit",
"similarity": 0.07032375786428317
},
{
"id": "item6",
"name": "Canon EOS Rebel T6 Digital SLR Camera Kit with EF-S 18-55mm f/3.5-5.6 IS II Lens (Black)",
"similarity": 0.03118930822565627
},
{
"id": "item5",
"name": "Sandisk Ultra 32GB Class 10 SDHC UHS-I Memory Card Up to 80MB, Grey/Black (SDSDUNC-032G-GN6IN)",
"similarity": 0
},
{
"id": "item8",
"name": "Fire TV Stick | Basic Edition | Streaming Media Player",
"similarity": 0
}
]
}

```