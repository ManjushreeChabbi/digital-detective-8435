# Mission 3 — Understand the Operating System

### Task 3.1 — Explore your operating system

I used Terminal commands to examine my computer's operating system, active account, available storage and running system activity.

| Information explored | What it tells me | My observation |
|---|---|---|
| Operating system | Identifies the operating system being used. | My computer uses macOS. |
| Current account identity | Identifies the currently active account. | An active account was displayed. Username kept private. |
| Available and used storage | Shows how much disk space is used and available. | [Add your actual df -h observation.] |
| System activity snapshot | Shows running processes and resource usage. | [Add your actual observation from top.] |

Commands used:

```bash
sw_vers
whoami
df -h
top -l 1
```

### Task 3.2 — Understand processes

A process is an instance of a program that is currently running on a computer.

**What is a process?**

A process is a program that is being executed by the operating system. Each running application can have one or more processes.

**What does PID represent?**

PID stands for Process Identifier. It is a unique number assigned to a running process so that the operating system can identify and manage it.

**Two examples of processes:**

1. Google Chrome — A browser process.
2. Visual Studio Code — A code editor process.

I used the following command to view running processes:

```bash
ps
```

### Task 3.3 — Understand paths and permissions

A path describes the location of a file or folder.

**Absolute path:**

An absolute path gives the complete location of a file starting from the root directory.

Example: `/Users/your-account/your-repository/mission-03-operating-system/README.md`

**Relative path:**

A relative path describes the location of a file in relation to the current working directory.

Example:

```text
mission-03-operating-system/README.md
```

**File permissions:**

| Permission | Meaning | Example |
|---|---|---|
| r — Read | Allows a file to be read. | Opening a document. |
| w — Write | Allows a file to be modified. | Editing a document. |
| x — Execute | Allows a file to be executed. | Running a program. |

I used this command to inspect file permissions:

```bash
ls -l README.md
```

**My observation:** [Record the permission letters shown for the owner.]

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Explanation | Example |
|---|---|---|
| Process management | Manages running programs and allocates CPU time. | Running Chrome and VS Code simultaneously. |
| Memory management | Allocates and manages RAM for different programs. | Giving memory to an open browser. |
| Device management | Controls hardware devices through drivers and system services. | Managing the keyboard and printer. |
| File management | Organises files and folders and manages access. | Saving documents in folders. |
| User interface / shell | Provides ways for users to interact with the computer. | macOS desktop and Terminal. |
| Security and permissions | Controls access to files and system resources. | Restricting access to certain files. |

## 3. Commands / tools used

- `sw_vers` — Displays macOS version information.
- `whoami` — Displays the current account name.
- `df -h` — Displays disk storage information.
- `top -l 1` — Displays a system activity snapshot.
- `ps` — Displays running processes.
- `pwd` — Displays the current working directory.
- `ls -l` — Displays file permissions and details.

