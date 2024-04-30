# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "05a121d35eba4712873e2912ad7bb522"

# URL of the file to transcribe
FILE_URL = "https://soundcloud.com/harris-ford-official/ein-kompliment?si=e7211c2ea24948adb6fb619e8f19fc92&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
