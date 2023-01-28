from github import Github
import sqlite3
from github_authentication import Git_auth
import os

# Connection to Github API
auth_key = Git_auth()
g = Github(auth_key.git_token())

# Search using GitHub API to find repositories with Python in them
repositories = g.search_repositories(query='language:python', sort='stars', order='desc')
path = './instance/pythongit.db'
exists = os.path.exists(path)
if not exists:
    os.makedirs('instance')
# Creation of database table
con = sqlite3.connect(path, check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS repos
          (repository_id int PRIMARY KEY, name VARCHAR, URL VARCHAR, created_date datetime,
          last_push datetime, description VARCHAR, star_num int)''')

# Extract repository information and organize each piece to match a field in our sql table:
def repo_parser(repositories):
    repo_list = []

    """
    Because of GitHub's rate limit exception 
    this is the limit of iterations that can be 
    run per functional call this does hamper results 
    given the number of python repositories that exist 
    """
    for repo in repositories[:350]:
        if repo.stargazers_count >= 20000:
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
    repo_list = repo_parser(repositories)
    # Inserts repo information to our database table
    cur.executemany("INSERT OR IGNORE INTO repos VALUES (?, ?, ?, ?, ?, ?, ?)", repo_list)
    # Reorders table based on highest star number
    cur.execute('''SELECT * FROM repos ORDER BY star_num DESC;''')
    # Commits changes to our database
    con.commit()
execute_db()