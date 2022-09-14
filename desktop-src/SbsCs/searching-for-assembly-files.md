---
description: Searching for Assembly Files
ms.assetid: 6e6c1104-5cde-4c07-9ee2-d87062675dac
title: Searching for Assembly Files
ms.topic: article
ms.date: 05/31/2018
---

# Searching for Assembly Files

Activation contexts can help the loader find assembly files. When the loader searches for a file to load by name, it first searches for files with the specified name that are referenced by assemblies that are members of the currently active activation context. A call to [**SearchPath**](/windows/desktop/api/processenv/nf-processenv-searchpathw) also locates these files first. Files having the specified name and the current activation context are found and loaded before files with the name in the local directory or in the PATH environment variable. This means that when you create manifests you need to list all files you plan to use with **SearchPath**, [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya), or static imports.

Note that these files are not automatically located when using [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) or other functions that do not search for files. To use these files with **CreateFile**, use [**SearchPath**](/windows/desktop/api/processenv/nf-processenv-searchpathw) first to find the path to the isolated file, and then use **CreateFile** on the returned path.

This method of file searching helps to keep isolated applications separate because multiple files with the same name can then differ only by their association with assemblies of different version numbers. The operating system can find the correct file to use during file operations.

If a DLL is loaded in this manner using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya), that DLL's entry point (DllMain) is called while the original activation context is kept active, except if the DLL itself contains a manifest at a certain resource ID (ISOLATIONAWARE\_MANIFEST\_RESOURCE\_ID, or 2)

 

 
