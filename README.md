
# Prerequists

- Docker v20.10.6 see [here](https://docs.docker.com/get-docker/) for instalation instructions
- Curl for testing purposes 


# How to use

## Bring up server
 In order to bring up the server you have to first build the docker image using:
```bash
docker build --tag autodesk:dev . 
```
Which will build a docker image with the tag autodesk:dev which we can reference later.

After the image is built bring up the server with the command:

```sh
docker run --rm -it  -p 5000:5000/tcp autodesk:dev
```

Which should make the server aviable through localhost:

Naviagate to the url: `http://localhost:5000/` to check that it is working correctly.

## Enabling Logging

by default the logging available does not log to standard out. If you wish to see the logs a enviorment variable `DEBUG_MODE` should be set to true. This can be done using this docker command:

```sh
docker run --rm -it --env DEBUG_MODE=True -p 5000:5000/tcp autodesk:dev
```

### Cleaning up

When finished run:  `docker stop` to bring down all the containers


# Testing

#### Test main end point with header: 

```sh
curl --header "Accept:application/json" http://localhost:5000/
```
output: ```{"message":"Hello, World"}```



```sh
curl  http://localhost:5000/
```

output: ```<p>Hello, World!</p>```




#### Run Unit Tests 

``` 
docker compose up
```

Will execute through docker compose to bring up the flask app and run tests againist it.

Note: will also work with sperate docker-compose application
