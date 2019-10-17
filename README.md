# :cocktail: gimlet

## setup
- `virtualenv venv`
- `pip install -r requirements.txt`
- Make a `.env` file with the following information
```
GITHUB_PERSONAL_ACCESS_TOKEN=<token>
GITHUB_USER=<user>
```
After creating a Personal access token, make sure to `Enable SSO`.

## usage
```
> python gimlet.py https://github.com/pallets/flask/pull/1416
success +181 -98 (7 files) | JSON support for test client and response object
        https://github.com/pallets/flask/pull/1416     
```

Sources:
- [auth](https://developer.github.com/v3/auth/#via-oauth-tokens)
