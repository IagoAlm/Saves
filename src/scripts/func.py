from tkinter import *
import winreg
import os
import vdf
import re


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


def transformString(lista):
    string = ''
    for item in lista:
        string = string+item
    return string


def listFilter(data):
    i = 0

    while i < len(data):
        if data[i] == '\t\t':
            data[i] = '-middle-'
        if data[i] == '\n\t':
            data[i] = '; '
        if data[i] == '':
            data.pop(i)
        else:
            i += 1
    return data


def filterString(string):
    subs = re.sub('{', ':{', string)
    subs = re.sub('}', '}; ', subs)
    subs = re.sub('\n', '', subs)
    # fix 12121 items with line 72, put line 88 on top of line 86 and create something that can see if there's more than 1 \t and replace with -middle-
    subs = re.sub('\t', '', subs)

    return subs


def showGame():
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\appmanifest_12120.acf"
    file = open(path, "r")
    arq = file.read()

    lines = (arq.strip() for lines in arq.splitlines())
    string = str()

    for line in lines:
        arqLista = line.split('"')
    print(arqLista)
    string = transformString(listFilter(arqLista))

    print(filterString(string))


showGame()
# findLocales(findFolders())
