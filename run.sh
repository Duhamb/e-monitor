#!/bin/bash
gunicorn -b 127.0.0.1:80 -w 4 dashapp:server -t 90
