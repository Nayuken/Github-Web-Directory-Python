"""
part 1:
1. Use the GitHub API to retrieve the most starred public Python projects.
Store the list of repositories in a database table.

2. The table must contain the
repository ID, name, URL, created date, last push date, description, and
number of stars.

3. This process should be able to be run repeatedly and
update the table each time.


Useful links from the GitHub API documentation:
https://developer.github.com/v3/
https://developer.github.com/v3/search/
Also:
https://github.com/PyGithub/PyGithub
"""
from github import Github
import sqlite3
from github_authentication import Git_auth


auth_key = Git_auth()
con = sqlite3.connect('pythongit.db', check_same_thread=False)
cur = con.cursor()

# Creation of database table
cur.execute('''CREATE TABLE IF NOT EXISTS repos
          (repository_id int PRIMARY KEY, name VARCHAR, URL VARCHAR, created_date datetime,
          last_push datetime, description VARCHAR, star_num int)''')
# Connection to Github API
g = Github(auth_key.git_token())
# Search using github API to find repositories with Python in them
repositories = g.search_repositories(query='language:python')


# Extract repository information and organize each piece to match a field in our sql table:
def repo_scrape(repositories):
    repo_list = []
    for repo in repositories[:50]:
        if repo.stargazers_count >= 10000:
            rep_id = repo.id
            name = repo.full_name
            url = repo.html_url
            creation_date = str(repo.created_at)
            push_date = str(repo.pushed_at)
            desc = repo.description
            star_num = repo.stargazers_count

            repo_list.append((rep_id,
                              name,
                              url,
                              creation_date,
                              push_date,
                              desc,
                              star_num))
    return repo_list

def execute_db():
    repo_list = repo_scrape(repositories)
    # Inserts repo information to our database table
    cur.executemany("INSERT OR IGNORE INTO repos VALUES (?, ?, ?, ?, ?, ?, ?)", repo_list)
    print("running")
    # Commits changes to our database
    con.commit()
