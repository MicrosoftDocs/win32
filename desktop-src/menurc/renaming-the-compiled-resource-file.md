---
title: Renaming the Compiled Resource File
description: By default, when compiling resources, RC names the compiled resource (.res) file with the base name of the .rc file and places it in the same directory as the .rc file.
ms.assetid: be120032-666f-4627-8f98-96bde7c55fa4
ms.topic: article
ms.date: 05/31/2018
---

# Renaming the Compiled Resource File

By default, when compiling resources, RC names the compiled resource (.res) file with the base name of the .rc file and places it in the same directory as the .rc file. CVTRES must then be invoked to convert the .res file to a binary resource (.rbj) format which can be understood by the linker. The following example compiles MyApp.rc and creates a compiled resource file named MyApp.res in the same directory as MyApp.rc:

**rc myapp.rc**

The **/fo** option gives the resulting .res file a name that differs from the name of the corresponding .rc file. For example, to name the resulting .res file NewFile.res, use the following command:

**rc -fo newfile.res myapp.rc**

The **/fo** option can also place the .res file in a different directory. For example, the following command places the compiled resource file MyApp.res in the directory C:\\Source\\Resource:

**rc -fo c:\\source\\resource\\myapp.res myapp.rc**

 

 




