import click
import re
import requests
from dotenv import load_dotenv

load_dotenv()
import os


GITHUB_API = "https://api.github.com"
GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")


def to_api_url(raw_url):
    m = re.match(
        r"^https://github.com/(?P<org>[a-zA-Z0-9-_]+)/(?P<repo>[a-zA-Z0-9-_]+)/pull/(?P<pull>\d+)$",
        raw_url,
    )
    return m.group("org"), m.group("repo"), m.group("pull")


def get_response_info(r):
    return {k: r.json()[k] for k in ["title", "additions", "deletions", "changed_files", "statuses_url"]}


def craft_string(d, pr_url):
    return (
        f"{d['status']} +{d['additions']} -{d['deletions']} ({d['changed_files']} files) | {d['title']}\n\t{pr_url}"
    )


@click.command()
@click.argument("pull_request_url")
def gimlet(pull_request_url):
    owner, repo, pull_number = to_api_url(pull_request_url)

    s = requests.Session()
    s.auth = (GITHUB_USER, GITHUB_PERSONAL_ACCESS_TOKEN)
    s.headers.update({"Accept": "application/vnd.github.v3+json"})

    pull_response = s.get(f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pull_number}")
    pull_response.raise_for_status()

    final_data = get_response_info(pull_response)

    status_response = s.get(final_data["statuses_url"])
    status_response.raise_for_status()

    final_data["status"] = status_response.json()[0]["state"]

    print(craft_string(final_data, pull_request_url))


if __name__ == "__main__":
    gimlet()
