# Discord bot tutorial



## 1. Prerequisites

Before you can start coding, you need to have five things:

- A Discord account
- A Discord server that you have enough access to, so you can connect bots
- A Discord application
- A Discord bot, with a token we'll use in phase 2
- Permissions granted for that server so that bot is able to read and write messages there

First two you can create in discord.com. The rest you can create in https://discord.com/developers/applications

Additionally, of course, you should already have Python 3.x set up the way you like it, and suitable IDE ready to go (See previous videos on this channel)









## 2. Start coding

First you need a few libraries:

```
pip install python-dotenv discord.py
```

So that's two fun libraries covered. Then you need to create the .env file, and set it up like this:

BOT_TOKEN=<MYBOTTOKENGOESHERE>

You can easily test if this part is working by running this code:

```
import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ['BOT_TOKEN'])
```

The rest you can pick up from https://discordpy.readthedocs.io/en/latest/



