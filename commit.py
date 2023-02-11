import datetime
from github import Github

# replace with your Github username and personal access token
g = Github("roniasatourian", "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")

# specify the repository name and owner
repo = g.get_repo("ronextra/git_commit")

# # specify the branch name
branch = repo.get_branch("master")

# get the latest commit on the branch
# last_commit = repo.get_commit(branch.commit.sha)

# # create a new file with the current date
# file_name = "date_" + str(datetime.datetime.now().date()) + ".txt"
# repo.create_file(file_name, "daily commit", "Today's date: " + str(datetime.datetime.now().date()), last_commit.sha)
