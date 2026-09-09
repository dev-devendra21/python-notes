# Python Virtual Environment Setup

A virtual environment allows you to create an **isolated Python environment for a project**. It keeps project dependencies separate from the global Python installation and other projects.

---

## Step 1: Check Python Installation

First, check whether Python is installed.

```bash
python --version
```

Example:

```text
Python 3.13.7
```

On Windows, you can also check:

```bash
py --version
```

If Python is not installed, install Python first and make sure **Add Python to PATH** is enabled during installation.

---

## Step 2: Check pip

`pip` is Python's package manager. It is used to install Python packages.

Check pip:

```bash
python -m pip --version
```

Example:

```text
pip 25.x from ...\site-packages\pip
```

---

## Step 3: Create a Project Directory

Create a directory for your Python project.

```bash
mkdir my-project
```

Move into the project:

```bash
cd my-project
```

Your terminal should now be inside:

```text
my-project/
```

---

## Step 4: Create the Virtual Environment

Run:

```bash
python -m venv .venv
```

### Explanation

```text
python
    ↓
Python interpreter

-m venv
    ↓
Run Python's built-in virtual environment module

.venv
    ↓
Name of the virtual environment
```

After this command, a `.venv` directory will be created.

---

## Step 5: Check the Project Structure

You should now have something similar to:

```text
my-project/
│
└── .venv/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── pyvenv.cfg
```

The `.venv` directory contains the isolated Python environment.

> Do not manually modify the contents of `.venv`.

---

# Step 6: Activate the Virtual Environment

Activation makes the terminal use the Python and packages from `.venv`.

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Windows CMD

```cmd
.venv\Scripts\activate.bat
```

## Git Bash

```bash
source .venv/Scripts/activate
```

---

## Step 7: Verify Activation

After activation, you should see `(.venv)` at the beginning of your terminal.

Example:

```text
(.venv) PS C:\Users\Deven\my-project>
```

The `(.venv)` indicates that the virtual environment is active.

---

# Step 8: Verify Python

Check the Python version:

```bash
python --version
```

Then check which Python executable is being used.

### Windows

```cmd
where python
```

The first path should point to `.venv`:

```text
C:\Users\Deven\my-project\.venv\Scripts\python.exe
```

You can also use:

```bash
python -c "import sys; print(sys.executable)"
```

Expected result:

```text
C:\Users\Deven\my-project\.venv\Scripts\python.exe
```

---

# Step 9: Upgrade pip

It is a good idea to upgrade pip inside the virtual environment:

```bash
python -m pip install --upgrade pip
```

Verify:

```bash
python -m pip --version
```

---

# Step 10: Install Python Packages

Now install the packages required by your project.

Example:

```bash
pip install requests
```

Multiple packages:

```bash
pip install requests fastapi uvicorn
```

Because the virtual environment is active, these packages are installed inside `.venv`.

---

# Step 11: Check Installed Packages

To see installed packages:

```bash
pip list
```

Example:

```text
Package    Version
---------- -------
pip        25.x
requests   2.32.x
```

You can also check a specific package:

```bash
pip show requests
```

---

# Step 12: Create `requirements.txt`

Once you have installed the packages required by your project, save them into `requirements.txt`.

Run:

```bash
pip freeze > requirements.txt
```

Example:

```text
fastapi==0.116.1
requests==2.32.5
uvicorn==0.35.0
```

This file records the package versions required by the project.

---

# Step 13: Add `.venv` to `.gitignore`

The virtual environment should **not be uploaded to GitHub**.

Create a `.gitignore` file:

```text
.gitignore
```

Add:

```gitignore
.venv/
```

A simple Python `.gitignore` could be:

```gitignore
# Virtual environment
.venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env
```

---

# Step 14: Understand What Goes to Git

### Commit these:

```text
my-project/
├── src/
├── requirements.txt
├── .gitignore
└── README.md
```

### Do NOT commit:

```text
.venv/
```

The reason is that `.venv` is specific to your local machine.

Instead of committing `.venv`, commit:

```text
requirements.txt
```

Other developers can recreate the environment using that file.

---

# Step 15: Install Dependencies from `requirements.txt`

When another developer clones your project, they don't need your `.venv`.

They can create their own:

```bash
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the project's dependencies:

```bash
pip install -r requirements.txt
```

Now their environment contains the required packages.

---

# Step 16: Run Your Python Application

After activating the virtual environment, run your application.

For example:

```bash
python app.py
```

Or, depending on the project:

```bash
python main.py
```

---

# Step 17: Deactivate the Virtual Environment

When you finish working on the project:

```bash
deactivate
```

Before:

```text
(.venv) PS C:\Users\Deven\my-project>
```

After:

```text
PS C:\Users\Deven\my-project>
```

The `(.venv)` prefix disappears.

---

# Step 18: Activate the Environment Again

The virtual environment does not need to be recreated every time.

If `.venv` already exists, simply activate it.

```powershell
.venv\Scripts\Activate.ps1
```

You only need to create it again if you delete it or need a fresh environment.

---

# Step 19: Delete and Recreate the Environment

If the virtual environment becomes corrupted or you want a completely fresh environment:

### Deactivate

```bash
deactivate
```

### Delete `.venv`

PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
```

CMD:

```cmd
rmdir /s /q .venv
```

### Create it again

```bash
python -m venv .venv
```

### Activate

```powershell
.venv\Scripts\Activate.ps1
```

### Reinstall dependencies

```bash
pip install -r requirements.txt
```

---

# Step 20: PowerShell Activation Error

If you get:

```text
running scripts is disabled on this system
```

when running:

```powershell
.venv\Scripts\Activate.ps1
```

run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

> `RemoteSigned` with `CurrentUser` changes the policy for your Windows user rather than requiring a machine-wide policy change.

---

# Complete Setup — From Zero

Here is the complete process for a new Python project.

## 1. Create the project

```bash
mkdir my-project
cd my-project
```

## 2. Check Python

```bash
python --version
```

## 3. Create virtual environment

```bash
python -m venv .venv
```

## 4. Activate it

```powershell
.venv\Scripts\Activate.ps1
```

## 5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 6. Install packages

```bash
pip install requests
```

## 7. Create requirements.txt

```bash
pip freeze > requirements.txt
```

## 8. Create `.gitignore`

```gitignore
.venv/
__pycache__/
.env
```

## 9. Start development

```bash
python app.py
```

## 10. Deactivate when finished

```bash
deactivate
```

---

# Existing Project Setup

When you clone an existing Python project:

```bash
git clone <repository-url>
cd <project-name>
```

Create the virtual environment:

```bash
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

---

# Important Concepts

## `.venv`

```text
.venv/
```

The actual virtual environment directory.

It should normally be added to `.gitignore`.

---

## `requirements.txt`

```text
requirements.txt
```

Contains the project's Python dependencies and versions.

It should normally be committed to Git.

---

## `pip`

Python's package installer.

Example:

```bash
pip install requests
```

---

## `venv`

Python's built-in module for creating virtual environments.

Example:

```bash
python -m venv .venv
```

---

# Recommended Project Structure

A typical Python project can look like:

```text
my-project/
│
├── .venv/              # Local virtual environment
│
├── src/                # Application source code
│   └── ...
│
├── tests/              # Tests
│   └── ...
│
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules
├── README.md           # Documentation
└── app.py              # Application entry point
```

---

# Quick Reference

| Task                 | Command                               |
| -------------------- | ------------------------------------- |
| Check Python         | `python --version`                    |
| Check pip            | `python -m pip --version`             |
| Create environment   | `python -m venv .venv`                |
| Activate PowerShell  | `.venv\Scripts\Activate.ps1`          |
| Activate CMD         | `.venv\Scripts\activate.bat`          |
| Activate Git Bash    | `source .venv/Scripts/activate`       |
| Check Python path    | `where python`                        |
| Upgrade pip          | `python -m pip install --upgrade pip` |
| Install package      | `pip install package-name`            |
| Uninstall package    | `pip uninstall package-name`          |
| Update package       | `pip install --upgrade package-name`  |
| List packages        | `pip list`                            |
| Package details      | `pip show package-name`               |
| Save dependencies    | `pip freeze > requirements.txt`       |
| Install dependencies | `pip install -r requirements.txt`     |
| Deactivate           | `deactivate`                          |

---

# Final Workflow

```text
Install Python
      ↓
Create Project
      ↓
Create .venv
      ↓
Activate .venv
      ↓
Upgrade pip
      ↓
Install Packages
      ↓
Create requirements.txt
      ↓
Add .venv to .gitignore
      ↓
Develop Application
      ↓
Deactivate when finished
```

## The 5 Commands to Remember

For Windows PowerShell:

```powershell
# 1. Create
python -m venv .venv

# 2. Activate
.venv\Scripts\Activate.ps1

# 3. Install packages
pip install <package-name>

# 4. Save dependencies
pip freeze > requirements.txt

# 5. Deactivate
deactivate
```

> **Rule of thumb:** Create one virtual environment per Python project, keep `.venv/` out of Git, and use `requirements.txt` to share/recreate the project's dependencies.
