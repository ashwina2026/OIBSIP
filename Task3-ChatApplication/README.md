# Python Chat Application 💬

## Project Description

The Python Chat Application is a beginner-level client-server messaging application developed using Python.

It allows multiple users to connect to a central server and exchange messages through their Terminal windows.

The application uses socket programming for communication and threading to handle multiple clients simultaneously.

## Features

- Client-server communication.
- Multiple client connections.
- Username selection.
- Send and receive messages.
- Broadcast messages to connected users.
- Display user join and leave notifications.
- Handle client disconnections.
- Simple Terminal-based interface.

## Technologies Used

- Python 3
- Socket module
- Threading module

## Project Structure

```text
Task3-ChatApplication/
│
├── server.py
├── client.py
├── README.md
│
└── screenshots/
```

## Installation

1. Install Python 3.
2. Open Terminal.
3. Navigate to the main OIBSIP folder.
4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

No additional third-party packages are required.

## How to Run

### Step 1: Start the Server

Open the first Terminal window and run:

```bash
python Task3-ChatApplication/server.py
```

The server will start listening for client connections.

### Step 2: Start the First Client

Open a second Terminal window and run:

```bash
cd ~/Documents/Oasis-Infobyte/OIBSIP

source .venv/bin/activate

python Task3-ChatApplication/client.py
```

Enter a username when prompted.

### Step 3: Start Another Client

Open a third Terminal window and run the same client command.

Enter a different username.

Now both users can exchange messages.

### Step 4: Leave the Chat

Type the following command to disconnect:

```text
/quit
```

## Screenshots

Screenshots of the running server and connected clients will be available in the screenshots folder.

## Author

GitHub: [@ashwina2026](https://github.com/ashwina2026)

## Internship

Oasis Infobyte – Python Programming Internship