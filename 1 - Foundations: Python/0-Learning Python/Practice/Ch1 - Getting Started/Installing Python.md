// ...existing code...
# Installing Python (macOS)

1. Check if Python is already installed
```bash
python3 --version
```

2. Install Homebrew (if missing)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# On Apple Silicon, ensure Homebrew is in your shell:
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

3. Install Python via Homebrew
```bash
brew update
brew install python
```

4. (Recommended) Use pyenv to manage multiple Python versions
```bash
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
source ~/.zprofile
pyenv install 3.12.2
pyenv global 3.12.2
```

5. Set up a virtual environment for a project
```bash
python3 -m pip install --upgrade pip
python3 -m venv .venv
source .venv/bin/activate
# inside venv:
python --version
pip install -r requirements.txt   # if you have dependencies
```

6. Alternative: download installer from python.org
- Visit https://www.python.org/downloads/macos/ and run the macOS installer.

Notes
- Use `python` (not `python3`) after activating a venv.
- I can add a shell script that automates these steps if you want.