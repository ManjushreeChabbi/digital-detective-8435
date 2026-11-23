# Mission 2 — Become Comfortable with the Terminal

### Task 2.1 — Explore basic Terminal operations

| Operation | Command | What it does | What I observed |
|---|---|---|---|
| Current-directory display | `pwd` | Displays the full path of the current folder. | It displayed my current working directory. |
| Directory listing | `ls` | Lists files and folders. | It displayed the contents of the current folder. |
| Detailed listing | `ls -l` | Displays files with detailed information. | It showed permissions, size and modification details. |
| Change directory | `cd ..` | Moves to the parent directory. | My current location changed to the parent folder. |
| Create directory | `mkdir practice-folder` | Creates a new folder. | A new folder was created. |
| Create empty file | `touch notes.txt` | Creates an empty text file. | The file was created successfully. |
| Copy file | `cp notes.txt notes-copy.txt` | Creates a copy of a file. | A second copy was created. |
| Move / rename file | `mv notes-copy.txt renamed-copy.txt` | Moves or renames a file. | The copied file was renamed. |
| Display file contents | `cat notes.txt` | Displays the contents of a file. | The text appeared in Terminal. |

### Task 2.2 — Practise file changes safely

I created a folder named `terminal-practice` inside my assignment repository.

Commands used:

```bash
mkdir terminal-practice
cd terminal-practice
touch notes.txt
echo "This is my first line." > notes.txt
echo "This is my second line." >> notes.txt
cat notes.txt
cp notes.txt backup.txt
mv backup.txt notes-backup.txt
```

**Answers:**

1. The `>` symbol replaces the existing contents of a file, while `>>` adds new content at the end without deleting previous content.
2. Copying creates another version of a file while keeping the original. Moving changes the file's location or name.
3. The `pwd` command displays the complete path of my current working directory.
4. The `ls` command helps me identify the files and folders available in a directory.

### Task 2.3 — Understand flags and pipes

| Command | Purpose |
|---|---|
| `ls` | Displays a basic directory listing. |
| `ls -l` | Displays detailed file information. |
| `ls -la` | Displays detailed information, including hidden files. |
| `ls -lah` | Displays hidden files and detailed information with human-readable sizes. |
| `ls -l \| head` | Displays only the first few lines of the detailed listing. |

A flag changes the behaviour of a command. For example, `-l` displays additional file information.

The pipe symbol `|` sends the output of one command to another command. In `ls -l | head`, the first command generates the listing, and the second command displays only the first few lines.

### Task 2.4 — Understand package managers

A package manager is a tool used to install, update and remove software packages.

Homebrew is a popular package manager for macOS. It makes software management easier by handling package installation and updates.

Commands:

brew --version
brew list 