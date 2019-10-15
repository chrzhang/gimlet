# gimlet

## setup
- `virtualenv venv`
- `pip install -r requirements.txt`
- Make a `.env` file with the following information
```
GITHUB_PERSONAL_ACCESS_TOKEN=<token>
GITHUB_USER=<user>
```

## usage
```bash
> python gimlet.py https://github.com/pallets/flask/pull/1416
success +181 -98 | JSON support for test client and response object
        https://github.com/pallets/flask/pull/1416     
```
