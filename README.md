## NW Share

Imagine your girlfriend and some of your other friend are in such a country, that they cannot visit Youtube or other fancy website such as Reddit. How are you going to share funny videos with them?

Introducing NW Share. The system consists of 2 parts, an Android client, and a server. The client does not have any user interface. The only usage of it is to accept share intent, and send the Youtube URL to the server. The server would download the video automatically, and host a file server so you can view it easily.

## Note

Currently there's only Android Client, since the library I used for sharing doesn't support iOS yet. But since the main application is written in Flutter, surely we can improve it later.

## How to try it yourself

Note: this appication is still in early development, so it's **VERY NOT USER FRIENDLY**.

- Prepare develop environment for Flutter, Python as well as Node.js
- Modify the server IP in `share_client/lib/main.dart`
- Build and install the application on your Android phone
- Get a server somewhere
- Run `python download_server.py`
- Also run `cd file_server && npm start`

## Why NW?

NW can be North West, No Wall, No Where...

## Roadmap

- Add a form for inputting server IP instead of headcoding in the app
- Release pipeline