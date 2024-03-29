## Boilerplate Flask web app

For practice purposes. But once finished, it can be easily copied and adapted to suit all kinds of needs. It works locally but since i'm still learning, a lot of things are not configured according to best practices.

### Tech Stack
- Web: Flask
- ORM: SQLAlchemy
- Database: PostgreSQL
- User Authentication: Flask-Login and bcrypt
- Containerization: Docker
- WSGI Server: Gunicorn
- Reverse Proxy Server: NGINX

### Todo / Roadmap
- [x] Basic Flask container
- [x] Basic dockerization
- [x] models for SQLAlchemy
- [x] Postgres container
- [x] Postgres integration into Flask
- [x] Flask separate config.py
- [x] Routes via blueprints
- [x] Add new entry
- [x] Update entry/entries
- [x] Remove entry
- [x] Nginx server container
- [x] WSGI-Gunicorn
- [x] use __init__.py for Flask
- [x] Reorganize Flask app folder structure
- [x] User auth and respective routes
- [x] Separate development and production environment
- [ ] Redis?
- [ ] Celery?
- [ ] RabbitMQ?

### Instructions
1. Rename .env_flask.sample and .env_pg.sample to .env_flask and .env_pg
2. Replace your Postgres username, password and db_name in both files.
3. Run ```chmod +x entrypoint.sh``` (not sure if Github keeps permissions)
4. Run ```docker-compose build```
5. Run ```docker-compose up```
6. In new terminal run ```docker-compose exec web python manage.py create_db``` to create tables
7. ???
8. Profit