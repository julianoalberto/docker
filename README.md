# What is Docker?
* https://www.docker.com/
* Package manager like apt, npm, pip, etc
* Packages contain app + dependencies + OS libs/bins


## Excellent Docker course (€14.99 on sales)
* https://www.udemy.com/course/docker-mastery/


## Quick demo
* apt (package manager)
    ```
    cowsay hello
    sudo apt install cowsay
    cowsay hello
    ```

* docker
    ```
    docker run hello-world
    docker run -ti --rm alpine sh
    docker run -ti --rm busybox:latest
    ```


# Build, ship, run

## Build (image)
```
cd cowsay
docker build . --tag cowsay:latest
docker images cowsay:latest
docker inspect cowsay:latest
docker run -ti cowsay:latest
```

## Ship (registry)
* https://hub.docker.com

```
docker login
docker tag cowsay:latest julianoalberto/cowsay:0.1
docker images | grep cowsay
docker push julianoalberto/cowsay:0.1
```

## Run (container)
```
docker run julianoalberto/cowsay:0.1
docker ps -a
```


# Docker vs. Virtual Machine
* https://royalnguyen.net/wp-content/uploads/2021/06/containers-vs-vms-correct.png
* https://royalnguyen.net/?cat=14


# Dockerfile

## USER
```
cd user

docker build . -f Dockerfile.root -t user:root
docker run -ti --rm user:root

docker build . -f Dockerfile.user -t user:user
docker run -ti --rm user:user
```


## WORKDIR
```
cd workdir

docker build . -f Dockerfile -t workdir:latest
docker run -ti --rm workdir:latest
```


## ARG
```
cd arg

docker build . -f Dockerfile -t arg:latest
docker build . --build-arg USER_NAME="test-user" -f Dockerfile -t arg:latest
docker run -ti --rm arg:latest
```


## ENV
```
cd env
```

### no
```
docker build . -f Dockerfile.no -t env:no
docker run -ti --rm env:no
```

### yes
```
docker build . -f Dockerfile.yes -t env:yes
docker run -ti --rm env:yes
docker run -e USER_NAME=ctw1234 -ti --rm env:yes
```


## ENTRYPOINT
```
cd entrypoint
docker build . -f Dockerfile -t entrypoint:latest
docker run -ti --rm entrypoint:latest
```


## CMD
```
cd cmd
docker build . -f Dockerfile -t cmd:latest
docker run -ti --rm cmd:latest
```


# Volumes
```
cd volume

docker build . -t volume:latest
```

## no volume
```
docker run -ti --name vol volume:latest
docker cp vol:/var/log/ctw.log .
```

## volume
```
docker volume create --name log
docker run -ti -v log:/var/log --rm volume:latest
```

## mount
```
docker run -ti -v /var/log/ctw:/var/log --rm volume:latest
```


# Case: GO (multistage build)
## go
```
cd hello-go
go mod init hello
go build -v
./hello
ls -lh hello
```

## docker for building
```
docker run -v $(pwd):/app -w /app golang:1.18 go mod init hello
docker run -v $(pwd):/app -w /app golang:1.18 go build -v

docker images golang:1.18
```

## all docker large
```
docker build . -f Dockerfile.large -t hello-go:large
docker images hello-go:large
docker run -ti --rm hello-go:large
```

## all docker small (multistage build)
```
docker build . -f Dockerfile.small -t hello-go:small
docker images hello-go:small
docker run -ti --rm hello-go:small
```


# Case: calc
## dev
```
cd calc

export FLASK_APP=calc
flask run
curl "localhost:5000/add?a=10&b=3"
```

## test (clean machine)
```
cd calc
export FLASK_APP=calc
flask run
!!fail!!
```

## docker
```
docker build . -t calc:latest
docker run -ti --network host --rm  alpine:latest
docker run -ti --network host --rm -p 5000:5000 --name calc calc:latest
curl "localhost:5000/add?a=10&b=3"
```


# Docker @CTW
## MCI
Uses Docker mostly to build and test C/C++ code.

* https://cc-github.bmwgroup.net/mci/mgu22-sdk-docker/blob/master/mgu22-sdk-base/Dockerfile
    * https://cc-github.bmwgroup.net/mci/mgu22-sdk-docker/blob/master/mgu22-sdk-pkglist/Dockerfile
        * https://cc-github.bmwgroup.net/mci/mgu22-sdk-docker/blob/master/mgu22-sdk-ccache/Dockerfile
            * https://cc-github.bmwgroup.net/mci/mgu22-sdk-docker/blob/master/mgu22-sdk-clang/Dockerfile
                * https://cc-github.bmwgroup.net/mci/mgu22-sdk-docker/blob/master/mgu22-sdk-clang-vdt/Dockerfile


## Apinext
Uses a Docker container as an entry point for CI operations. Executes Python code.

* https://cc-github.bmwgroup.net/apinext/docker-aosp-build/blob/master/docker/Dockerfile


# Why Docker?
* deploy with no need to configure host OS
* fast provisionment of test environments
* security
* better use of computing resources
* predictability
* what else?


# TBD
* docker-compose
* kubernetes
