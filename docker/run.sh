#!/bin/bash
docker run \
    -d \
    --init \
    -p8888:8888 \
    --rm \
    -it \
    --ipc=host \
    --name=CodingTest \
    --env-file=.env \
    --volume=$PWD:/workspace \
    coding_test:latest \
    ${@-fish}
