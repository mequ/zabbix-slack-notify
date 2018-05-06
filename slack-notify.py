#!/usr/bin/env python

import json
import requests
import sys



slack_data = sys.argv[3]

webhook_url = "https://hooks.slack.com/services/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"

response = requests.post(
    webhook_url, data=slack_data,
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
#curl -X POST --data-urlencode "{\"channel\": \"#general\", \"username\": \"webhookbot\", \"text\": \"This is posted to #general and comes from a bot named webhookbot.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/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
