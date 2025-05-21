import os
import git

class GitExplorer:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)

    def list_branches(self):
        """List all branches in the repository."""
        branches = [branch.name for branch in self.repo.branches]
        print("\nBranches in the repository:")
        for branch in branches:
            print(branch)

    def list_commits(self, num_commits=5):
        """List recent commits."""
        commits = list(self.repo.iter_commits('master', max_count=num_commits))
        print(f"\nRecent {num_commits} commits:")
        for commit in commits:
            print(f"{commit.hexsha[:7]} - {commit.author} - {commit.message}")

    def list_files(self):
        """List all files in the repository."""
        files = self.repo.git.ls_tree('HEAD', '-r', '--name-only').split('\n')
        print("\nFiles in the repository:")
        for file in files:
            print(file)

    def explore(self):
        """Allow user to interactively explore the repository."""
        while True:
            print("\nGit Explorer Options:")
            print("1. List Branches")
            print("2. List Recent Commits")
            print("3. List Files in the Repo")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.list_branches()
            elif choice == '2':
                num_commits = int(input("Enter the number of recent commits to show: "))
                self.list_commits(num_commits)
            elif choice == '3':
                self.list_files()
            elif choice == '4':
                print("Exiting Git Explorer.")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    repo_path = input("Enter the path to the Git repository: ")

    if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, '.git')):
        explorer = GitExplorer(repo_path)
        explorer.explore()
    else:
        print("Invalid Git repository path.")
