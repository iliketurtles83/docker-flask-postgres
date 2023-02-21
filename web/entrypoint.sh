#!/bin/sh
gunicorn -w 2 -b :8000 app:app