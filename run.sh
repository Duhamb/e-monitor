#!/bin/bash
gunicorn -b 0.0.0.0:80 -w 4 dashapp:server -t 90
