#!/bin/bash
docker exec -itd CodingTest jupyter-lab --no-browser --port=${@-8888} --ip=0.0.0.0 --allow-root --NotebookApp.token=''
