# twittervotes
sample app using twitter api

## File twitter_auth.py
This tool creates a web server on your port 3000. Access it through your browser. It allows you to retrieve the oauth token and save it to .twitterauth yaml file.

## File app .py
Runs the app. Actually, it simply counts twits fetched in hardcoded intervals. Example:
```
> python app.py -ht python linux covid19
```

## File test .py
Manual tests for some components. Ignore this one.

## Hashtag.refresh_url format:
refresh_url':'?since_id=963341767532834817&q=%23python&result_type=mixed&include_entities=1
