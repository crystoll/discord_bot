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

I have added some libraries over time. In current version they can be found from requirements.txt file, so before you start, you can just do something like:

´´´
pip install requirements.txt
´´´

If you are playing with the very initial commits I've made, you can just do something like:

```
pip install python-dotenv discord.py
```

Then you need to create the .env file, and set it up like this:

BOT_TOKEN=<MYBOTTOKENGOESHERE>

You can easily test if this part is working by running this code:

```
import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ['BOT_TOKEN'])
```

The rest you can pick up from https://discordpy.readthedocs.io/en/latest/

## 3. How to see earlier versions of the code? (AKA I'm following the video series, and want to see what you did in episode 2?) 

Yes, I always push here the latest version of the code, so if you make a clone, that's what you get. If you want to see the earlier, simpler steps, fortunately that's rather easy.

You can list all the commits I've made like this:

```
git log
```

Once you see a commit you like, for example:

```
commit ed8c6e4b491ac0bf8b37f61bb1156362efdd34f2
Author: Arto Santala <crystoll@gmail.com>
Date:   Fri Jan 29 14:50:55 2021 +0200

    Initial import. Basic bot going on
```

You can temporarily check it out by doing:

```
git checkout ed8c6
```

This takes you to detached head-state, but you can see the code so far, and can make your own version of it, or just study it, as you prefer. I have also tagged main episode parts so you can alternatively just do:

```
git checkout episode3
```


If you want to go back to latest version available in server, you can always do a:

```
git checkout -B main origin/main
```


## 4. How to run this as a module?

Now that we have refactored code under packages, it makes more sense to run this as a module. From command line it's rather easy:

```
python3 -m pomobot
```

For VSCode, I showed in pomobot series part 9 video, how to set it up. But short notes are:
- Go to Run - Add Configuration - Python - Python Module (module name: pomobot)
- Then to run this, you can either press F5, or go to Run - Start Debugging


