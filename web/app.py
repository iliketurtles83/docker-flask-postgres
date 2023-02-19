from __init__ import create_app

app = create_app()

if __name__ == '__main__':
	with app.app_context():
		print('in main')
		app.run(host='0.0.0.0', port=8000, use_reloader=False)