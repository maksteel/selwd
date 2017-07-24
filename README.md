# selwd
selenium with docker 

1. Clone the repo
```
$ git clone https://github.com/maksteel/selwd.git
```
2. Configure the project
```
$ cd selwd
$ cp sample_config.ini config.ini
$ nano config.ini OR vi config.ini
```
3. Build docker image
```
$ docker build --build-arg config_file=config.ini -t manishka/selwd:latest .
```
4. Run the docker image
```
$ docker run -d manishka/selwd:latest
```
