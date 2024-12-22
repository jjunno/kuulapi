# kuulapi

Raspberry Pi Marble Machine Player.

My toddler really likes the Marble Machine by Wintergatan. I had old heavily used RPI 3 B+, so I figured to create one-button miracle Marble Machine player.

Basically it just boots up (using either kuulapi.service or run.sh), red led indicates the script is on and a press of a button starts playing the song. Another press of a button stops the song. A green led indicates that the song is playing.

Note: This repository does not contain the song itself, you need to acquire it somewhere else.

# Clone & Run
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
