#!/bin/bash
gunicorn -b 0.0.0.0:8080 -w 4 dashapp:server -t 90
