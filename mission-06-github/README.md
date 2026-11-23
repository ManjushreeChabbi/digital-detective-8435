# Mission 6 — Git and GitHub

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does |
|---|---|
| Check repository status | `git status` displays modified, staged and untracked files. |
| Stage selected changes | `git add filename` selects changes for the next commit. |
| Create a commit | `git commit -m "message"` saves staged changes in Git history. |
| View commit history | `git log --oneline` displays previous commits. |

**Difference between staging and committing:**

Staging means selecting the changes that should be included in the next commit.

Committing means permanently recording those staged changes in the local Git history.

### Task 6.2 — Create and use a branch

I created a new branch named `update-about`.

Command:

```bash
git switch -c update-about
```

I opened the root README.md file and added a section titled My Learning.

The section contains three things I learned during the assignment:

1. I learned how computers process information using the IPOS cycle.
2. I learned how to use Terminal commands to manage files and folders.
3. I learned how Git and GitHub help track and manage project changes.

After updating the README, I checked the repository status, staged the changes, created a commit and published the branch.

Commands:

```bash
git status
git add README.md
git commit -m "Add my learning section to README"
git push -u origin update-about
```

### Task 6.3 — Create a Pull Request

I opened my GitHub repository and compared the update-about branch with the main branch.

I created a Pull Request from update-about into main.

**Pull Request description:**

This Pull Request adds a My Learning section to the root README file. It summarises the important concepts learned during the Digital Detective assignment and improves the project documentation.

**Pull Request URL:** [Paste your actual Pull Request URL.]

**Pull Request status:** [Open / Merged / Closed.]

A branch is a separate line of development that allows changes to be made without directly modifying the main branch.

A Pull Request is a request to review and merge changes from one branch into another. It helps team members review code and collaborate safely.

### Task 6.4 — Git command glossary

| Git command | Explanation |
|---|---|
| `git init` | Initialises a new Git repository. |
| `git status` | Displays the current repository status. |
| `git add` | Stages changes for a commit. |
| `git commit` | Records staged changes. |
| `git log` | Displays commit history. |
| `git branch` | Lists or creates branches. |
| `git switch` | Switches between branches. |
| `git push` | Uploads local commits to a remote repository. |
| `git pull` | Retrieves and integrates remote changes. |

## 3. Commands / tools used

- `git status`
- `git add`
- `git commit`
- `git log`
- `git branch`
- `git switch`
- `git push`
- `git pull`
- GitHub Pull Requests
