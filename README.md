# Stranded: Alien Dawn Localization extractor
## A cool scriptopllication for translation makers, to be able make a translation mod for the another mod.

This README is available on the following languages: [**English language**](https://github.com/acwartz/SADModsTranslExtract/blob/main/README.md), [**На русском языке**](https://github.com/acwartz/SADModsTranslExtract/blob/main/README-RUS.md)

## Installation on Windows

If you're on Windows, just download the archive from releases. 
**Note: *Application binary is not signed, your AV/SmartScreen may start suspect something. 
         Actually there is nothing to suspect, same script just get packed into standalone application using [PyInstaller](https://pyinstaller.org/)*** 
         Follow "Usage" section to know how it works.

## Installation

 0. Clone or download this repository.

Script requires  [**Python 3.10**](https://www.python.org/) to be able to make it work,
Check that python is unstalled (cmd on windows, sh on unix):
```sh
python --version
```
You should see something like this:
```sh
Python 3.10.7
```
 Open cmd from the folder where you extracted/cloned the repository and type:
 ```sh
 pip install  -r requirements.txt
 ```

if you want build your own binary (at least it works for windows), do this:
```sh
pyinstaller --onefile --clean SADLocExt.py
```

## Usage

 1. Find a mod which you want translate
 2. Extract it contents using in-game mod editor
 3. Copy SADLocExt.exe/SADLocExt.py to mod contents folder (where "Metadata.lua" file is placed)
 4. Run script/app, you should see success message "Data for translation are extracted and saved.", it means that "Translation.csv" is created. 
 5. You can follow this or this guides to know how to create a localization for mods.  

Any ideas are welcome. Use Issues for this.
