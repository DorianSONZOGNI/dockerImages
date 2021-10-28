from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
	try:
		visite = redis.incr("computer")
	except RedisError:
		visite = "<i>Erreur de connection Redis, compter desactive</i>"

	html = "<h3>Bonjour {nom}!</h3>" \
		"<b>Hostname:</b> {hostname}<br/>" \
		"<b>Visites:</b> {visites}" \
		"<p>Hello world d'image docker!<p>"
	return html.format(nom=os.getenv("NOM", "visiteur"), hostname=socket.gethostname(), visites=visite)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
