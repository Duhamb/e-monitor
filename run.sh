#!/bin/bash
gunicorn -b localhost:8080 -w 4 dashapp:server -t 90
