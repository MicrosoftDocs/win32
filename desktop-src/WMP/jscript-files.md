---
title: JScript Files
description: JScript Files
ms.assetid: 5b862e52-5d49-44b4-811c-3dbca5552167
keywords:
- Windows Media Player skins,JScript files
- skins,JScript files
- files for skins,JScript
- JScript files for skins,about
ms.topic: article
ms.date: 05/31/2018
---

# JScript Files

JScript files are loaded with the **scriptFile** attribute of the **VIEW** element. They must be text files and should use the file name extension .js. If you have a JScript file that has the same name as the skin definition file, the JScript file will be loaded at the same time as the skin definition file. For example, if you have a skin definition file named laure.wms, and you have a JScript file called laure.js, the laure.js file will be loaded automatically.

You can use JScript to create elaborate functionality behind your skin. By creating functions in JScript, you can do almost anything imaginable with skins. For example, you could use a different playlist for every day of the week, but always have the same one on Friday.

See [Using JScript](using-jscript.md) for more information about using JScript with skins. Note that Visual Basic Scripting Edition (VBScript), which can be used when embedding the Windows Media Player control in a webpage, is not supported for use with skins.

## Related topics

<dl> <dt>

[**Skin Files**](skin-files.md)
</dt> </dl>

 

 




