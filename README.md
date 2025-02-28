# ToolInstallerAI
ToolInstallerAI is a utility that takes a tool name, searches the internet for it, and generates a bash script to download and install the tool based on the installation instructions found.


## Installation:
```bash
# Clone the repository
git clone https://github.com/0xh7ml/toolInstallerAI.git

# Navigate to the project directory
cd toolInstallerAI

# Install required Python packages
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file to add your OpenAI API key
```

## Usage:
./main.py --tool-name subfinder

```console
INPUT: 
  -tn , --tool-name   Tool name to install
```

## ToDo:
- [x] Take Tool Name. 
- [x] Initiate OPENAI API Handler. 
- [x] Search the tool name using OPENAI API Handler. 
- [x] Read the source or the installation instruction. 
- [x] Create a bash script to download / install that tool. 

## Required modules:
- openai
- dotenv