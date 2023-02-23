#!/bin/sh
cd /
gunicorn -w 2 -b :8000 web.app:app