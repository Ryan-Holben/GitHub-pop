import requests
import json

"""
description str
html_url str
name    str
updated_at  u'2014-10-23T04:45:17Z'
full_name "username/reponame"


watchers    int
watchers_count  int
stargazers_count    int
forks   int
fork_count  int
"""

username = "microsoft"
# top_n = 20

per_page = 100
current_page = 1
api_repo_url = "https://api.github.com/users/" + username + "/repos"
repos = []

while True:
    options_url = "?page={}&per_page={}".format(current_page, per_page)
    print "Loading:", api_repo_url + options_url
    r = requests.get(api_repo_url + options_url)
    raw_json = json.loads(r.text)
    repos += [ [r['stargazers_count'] + r['forks_count'], r] for r in raw_json]
    if len(raw_json) < per_page:
        break
    else:
        current_page += 1

print "\nFound", len(repos), "repos.\n"

total_popularity = sum(r[0] for r in repos)
repos.sort(reverse=True)

print "Top", username, "repos by popularity:"
for r in repos:
    if 1.0*r[0]/total_popularity < 0.01:
        break
    print r[0], '\t', r[1]['name']
