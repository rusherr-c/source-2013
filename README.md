# Source Engine 2013
Fork of nillerusr's source engine with x86 support.

The fork does not correspond to the master branch of the nillerusr's engine, since the master branch does not support (although it did) Win32 build mode.

Instead of the master branch, <a href="https://github.com/nillerusr/source-engine/tree/be3d0e301f2bf7c53267378ad8c932084077967f">Commit be3d0e3</a> is used.

# How to build? (WINDOWS ONLY)
Install **Python 3 (3.9 - 3.14 is supported) and Visual Studio with MSVC compiler (v141 - v143 is supported)** <br>
Open powershell,<br>
Clone repo and change directory:
```
git clone https://github.com/rusherr-c/source-engine --recursive --depth 1
cd source-engine
```

# Instructions
## Configure
> 📝
> Also there is a configure macro (configure.py)

Run `.\waf configure -T <BUILDMODE>`, where BUILDMODE is release or debug.<br>
If it says something like `No such file or directory` use python3 or python prefix before ./waf.<br>
If you need a 64 bit build add -64bits argument to WAF.<br>
To change game that will be builded add `--build-games <GAME> --prefix <GAME>`<br>
Where GAME is:

**_hl1_** = Half-Life 1: Source

**_hl2_** = Half-Life 2 // Default - This will be selected if you don't specify a game

**_episodic_** = Half-Life 2 Episode 1 + Episode 2

**_hl2mp_** = Half-Life 2: Deathmatch

**_cstrike_** = Counter-Strike: Source

## Build

Run `.\waf build` to build every project or if you want to build just one project or several projects use `.\waf build --targets <TARGETS>`<br>
Where TARGETS is projects separated by comma (E.G `.\waf build --targets client,server`)<br>

## Run

You need to use some Half-Life 2 build before Anniversary Update and not the steam_legacy.<br>
I'm using <b>build 5377866 (from 2020)</b> that can be installed from <b>Steam Console</b> <br>
To open <b>Steam Console</b> you need to press <b>Windows + R</b>, and type:<br>
```
steam://open/console
```
Command in Steam Console:
```
download_depot 220 221 773449029659131748
```

# Problems
If you running Counter-Strike Source please ensure you are using v92(build 6953255) content,<br>
You can install it from Steam, using beta version previous_build.<br>
Or if you don't have bought CSS, install it's dedicated server using SteamCmd.<br>
Commands in SteamCmd:
```
login anonymous
app_update 232330 -beta previous_build validate
```
