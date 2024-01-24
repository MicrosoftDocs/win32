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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# JScript Files

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

JScript files are loaded with the **scriptFile** attribute of the **VIEW** element. They must be text files and should use the file name extension .js. If you have a JScript file that has the same name as the skin definition file, the JScript file will be loaded at the same time as the skin definition file. For example, if you have a skin definition file named laure.wms, and you have a JScript file called laure.js, the laure.js file will be loaded automatically.

You can use JScript to create elaborate functionality behind your skin. By creating functions in JScript, you can do almost anything imaginable with skins. For example, you could use a different playlist for every day of the week, but always have the same one on Friday.

See [Using JScript](using-jscript.md) for more information about using JScript with skins. Note that Visual Basic Scripting Edition (VBScript), which can be used when embedding the Windows Media Player control in a webpage, is not supported for use with skins.

## Related topics

<dl> <dt>

[**Skin Files**](skin-files.md)
</dt> </dl>

 

 




