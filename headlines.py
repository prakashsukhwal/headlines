# coding=utf8
#import codecs

from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

#feed urls
URLs = {
	'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
	'cnn': 'http://rss.cnn.com/rss/edition.rss',
	'fox': 'http://feeds.foxnews.com/foxnews/latest',
	'iol': 'http://www.iol.co.za/cmlink/1.640'
}


@app.route("/")
@app.route("/<publication>")
def get_news():
	query = request.args.get("publication")
	if not query or query.lower() not in URLs.keys():
		publication = 'bbc'
	else:
		publication = query.lower()
	feed = feedparser.parse(URLs[publication])
	return render_template("home.html", articles = feed["entries"])


if __name__ == "__main__":
	app.run(port=5000, debug=True)