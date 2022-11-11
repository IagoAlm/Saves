from tkinter import *
import winreg
import os
import vdf


def findVersion(steamPath, bits):
    inicReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    try:
        path = winreg.OpenKey(inicReg, rf"{steamPath}")
        return path
    except:
        print(f"Não foi encontrado steam {bits}bits")
        return False


def findFolders():
    steam32 = "SOFTWARE\\VALVE\\STEAM"
    steam64 = "SOFTWARE\\Wow6432Node\\Valve\\Steam"

    path32 = ""
    path64 = ""

    if findVersion(steam32, 32) != False:
        path32 = winreg.QueryValueEx(
            findVersion(steam32, 32), "InstallPath")[0]

    if findVersion(steam64, 64) != False:
        path64 = winreg.QueryValueEx(
            findVersion(steam64, 64), "InstallPath")[0]

    if path32 == path64 and path32 != "" and path64 != "":
        path = path32
    if path64 != "" and path32 == "":
        path = path64
    if path32 != "" and path64 == "":
        path = path32

    arch = vdf.load(open(path + "\\steamapps\\libraryfolders.vdf"))
    libraries = list()
    for library in arch:
        for index in arch[library]:
            libraries.append(arch[library][index]['path']+"\\steamapps")
    return libraries


def findLocales(libraries):
    apps = dict()

    for path in libraries:
        items = list()
        files = os.listdir(path)
        for item in files:
            if ".acf" in item:
                items.append(item)
        apps[path] = items
    print(apps)


def showGame(wrapper=dict):
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\appmanifest_12120.acf"
    file = open(path, "r")
    arq = file.read()

    # print(arq)
    lines = (arq.strip() for lines in arq.splitlines())

    for line in lines:
        data = line.split('"')

    contr = 0
    string = ""
    for item in data:

        temp = item.replace('\n', '')
        temp = temp.replace('\t\t', ':')
        temp = temp.replace('\t{:', '\t{')
        temp = temp.replace(':{:\t', '{\t')

        data[contr] = temp
        contr += 1

    for item in data:
        string += item
    print(string)
    print(data)


showGame()
# findLocales(findFolders())
