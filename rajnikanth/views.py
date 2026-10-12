from django.shortcuts import render
import urllib.request as rq
import json
# Create your views here.
def index(request):
    content = {}
    url = "http://api.icndb.com/jokes/random?firstName=Rajnikanth&amp&lastName="
    if request.method == 'GET':
        try:
            with rq.urlopen(url, timeout=5) as res:
                joke_json = json.loads(res.read())
                joke = joke_json['value']['joke']
        except Exception:
            joke = "Rajnikanth is too busy to tell a joke right now."
        content = {"joke": joke}
        return render(request, 'search/index.html', content)


