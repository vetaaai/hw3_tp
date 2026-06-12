#!/bin/bash
case "$1" in
    build_generator)
        docker build -t csv-generator ./generator
        ;;
    run_generator)
        docker run --rm -v "$(pwd)/data:/data" csv-generator /data/data.csv
        ;;
    create_local_data)
        python3 ./generator/generate.py ./local_data/data.csv
        ;;
    build_reporter)
        docker build -t csv-reporter ./reporter
        ;;
    run_reporter)
        docker run --rm -v "$(pwd)/data:/data" csv-reporter
        ;;
    structure)
        find . -not -path "*/\.*" -not -path "*/node_modules/*" | sort
        ;;
    clear_data)
        rm -f data/*.csv data/*.html
        ;;
    inside_generator)
        docker run --rm -v "$(pwd)/data:/data" --entrypoint cat csv-generator /data/data.csv
        ;;
    inside_reporter)
        docker run --rm -v "$(pwd)/data:/data" --entrypoint cat csv-reporter /data/data.csv
        ;;
    *)
        echo "Неизвестная команда: $1"
        exit 1
        ;;
esac       