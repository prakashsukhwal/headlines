# coding=utf8
#import codecs

from flask import Flask 
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
def get_news(publication="bbc"):	
	feed = feedparser.parse(URLs[publication])
	first_article = feed["entries"][0]
	return """<html>
		<body>
			<h1> Headlines </h1>
			<b>{0}</b> <br/>
			<i>{1}</i> <br/>
			<p>{2}</p> <br/>
		</body>
		</html>""".format(first_article.get("title"), first_article.
get("published"), first_article.get("summary")).decode('utf-8')



if __name__ == "__main__":
	app.run(port=5000, debug=True)