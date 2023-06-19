import csv
from luaparser import ast
from os import path as ospath
from luaparser import astnodes
from pathlib import Path

BASE_SEARCH_PATH = '.\\'
MOD_MARKER_FILE = 'Metadata.lua' # a file which indicates that we are insideof the mod folder
LOCALIZATION_OTPUFILE = 'Translation.csv' # a default file name for output file

def is_valid_file(arg: str):
    path: Path = Path(arg)
    return path.exists() and path.is_file

print("Looking for Items.lua near this script...")

# every mod root folder contains Metadata.lua if it not there so this is not a mod root folder where app should be placed

if not is_valid_file(ospath.join(BASE_SEARCH_PATH, MOD_MARKER_FILE)):
    print(
        'Error: Expected "'+ospath.join(BASE_SEARCH_PATH, MOD_MARKER_FILE)+'" file should be in the same directory with this script. It indicates a mod root folder.'
    )
    input("Press any key to exit >>")
    exit()
    
print("Looking for lua files where translations can be be...") # currently I know that lua files (and not only the Items.lua) may contain T() calls                                               
luaFiles = list(Path(BASE_SEARCH_PATH).glob('**/*.lua')) # al of then need to be handled.
print('Found: {0} files'.format(len(luaFiles)));
if len(luaFiles) == 0:
    print('Therer is no lua files, nothing can be translated.')
    input("Press any key to exit >>")
    exit()
    
for filePath in luaFiles:
    print('Lua file: {0}'.format(filePath))
    
    
outFile: str = ospath.join(BASE_SEARCH_PATH, LOCALIZATION_OTPUFILE);
print("Creating output file...")
# create a CSV
with open(outFile, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Text", "Translation"])
    # lets walk over all of them 
    for filePath in luaFiles:
        luaFilePath = ospath.join(BASE_SEARCH_PATH, filePath);
        print('Reading "{0}" content...'.format(luaFilePath))
        with open(luaFilePath, "r", encoding="utf-8") as luaFileObj:
            luaSourceCode = luaFileObj.read()
            luaAST = ast.parse(luaSourceCode)            
            # lets walk on the ast tree
            for node in ast.walk(luaAST):
                # skip any nodes except function calls
                if not (type(node) == astnodes.Call): continue
                
                # skip if object does nod have id attribute.
                if not hasattr(node, 'func'): continue
                if not hasattr(node.func, 'id'): continue
                
                # skip any function except T
                if not (node.func.id == "T"): continue
                
                key: int = node.args[0].n  # translation key
                defText: str = node.args[1].s  # default translation text from mod author
                writer.writerow([str(key), defText, "TRANSLATE ME!"])
                print('Exporting: "{0}": "{1}"'.format(key, defText));
        
        print("Export from {} done.".format(luaFilePath));
    print(
        "Data for translation are extracted and saved. File "+outFile+" is created near this script file."
    )
input("Press Enter to close the application... :)")