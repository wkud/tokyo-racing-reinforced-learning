## Commands to use:

- `netstat -aon` - shows all ports available on windows along with their PIDs and state (empty state entry means that a given port is available)

## Throubleshooting
- check if both apps have the same port. In Unity app this is defined in file `TcpClientWrapper.cs`. In Python, simply main.py
