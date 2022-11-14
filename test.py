import re
lista = ['AppState', '\n{\n', 'appid', ':', '12120', ';', 'Universe', ':', '1', ';', 'LauncherPath', ':', 'C:\\\\Program Files (x86)\\\\Steam\\\\steam.exe', ';', 'name',
         ':', 'Grand Theft Auto: San Andreas', ';', 'StateFlags', ':', '4', ';', 'installdir', ':', 'Grand Theft Auto San Andreas', ';', 'LastUpdated', ':', '1617985291',
         ';', 'UpdateResult', ':', '0', ';', 'SizeOnDisk', ':', '4923455331', ';', 'buildid', ':', '459558', ';', 'LastOwner', ':', '76561198092699131', ';', 'BytesToDownload', ':', '4035644016', ';', 'BytesDownloaded', ':', '4035644016', ';', 'BytesToStage', ':', '4923455331', ';', 'BytesStaged', ':', '4923455331', ';', 'AutoUpdateBehavior', ':', '0', ';', 'AllowOtherDownloadsWhileRunning', ':', '0', ';', 'ScheduledAutoUpdate', ':', '0', ';', 'InstalledDepots', '\n{\n', '12123', '\n{\n', 'manifest', ':', '3229936372288409207', '\n', 'size', ':', '1707644556', '}', ';', '12122', '\n{\n', 'manifest', ':', '5085199700668523983', '\n', 'size', ':', '1676856594', '}', ';', '12121', '\n{\n', 'manifest', ':', '242870450180196986', '\n', 'size', ':', '1538954181', '\n}\n}\n', 'SharedDepots', '\n{\n', '228990', ':', '228980', '}', ';', 'UserConfig', '\n{\n', 'language', ':', 'english', '\n}\n}']

stringTest = "\n}\n}\n"


def noRegex(stringTest):

    for i in range(len(stringTest)):
        try:
            if stringTest[i] == '}' and stringTest[i+1] == '\n':
                stringTest = stringTest[:i+1] + ';' + stringTest[i+2:]
            if stringTest[i] == '{' and stringTest[i-1] == '\n':
                stringTest = stringTest[:i-2] + ':' + stringTest[i-1:]
        except:
            print('', end='')

    print(stringTest)


noRegex(stringTest)


def wRegex(stringTest):

    x = re.sub("\n{", ":{", stringTest)
    x = re.sub("}\n", "};", stringTest)
    print(x)


wRegex(stringTest)
