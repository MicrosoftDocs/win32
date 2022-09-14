---
title: Debugging Code
description: Debugging Code
ms.assetid: 315bc692-86bc-481e-abe4-f35309807a58
keywords:
- Windows Media Player skins,debugging code
- skins,debugging code
- debugging code for skins
- Windows Media Player skins,logging
- skins,logging
- logging functionality in skins
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Code

You often will want to see what is happening inside your skin. You can do this through a text control or through a log file.

You can create a **TEXT** element and place it on a part of your skin temporarily. For example, you could use the following code to create your **TEXT** element:


```C++
<!-- debugging control -- remove later -->        
<TEXT
    id = "debug"
    foregroundColor = "white"
    backgroundColor = "black"
    value = "debug"
    top = "100"
    left = "50"
    height = "15"
    width = "100" 
    z-order = "5" />
<!-- end debugging control -->
```



Then, for example, if you want to see the current position of the digital media content in Windows Media Player, you could use code similar to the following to display the current position in the text box.


```C++
<PLAYER
    id = "myplayer">
    <CONTROLS
        id = "mycontrols"
        currentPosition_onchange="value=player.controls.currentPosition"/>
</PLAYER>

```



## To Write Debugging Information to a Log File

To enable or disable debugging, change the value of the following registry key:

**HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft\\MediaPlayer\\Preferences\\ScriptDebugging**

When you set the value to 1, logging is enabled. When you set the value to 0 (the default), logging is disabled.

If logging is enabled, a file will be placed on the user's computer in the same folder as the skin. The file will be named "*filename*\_0\_log.txt", where *filename* is the name of the skin file. The code in your skin can write text to this file by using the *Theme*.**logString** method. This can be useful if you want to determine what is going on inside your code while it is running. Note that the text file is encoded with Unicode characters.

When logging is enabled and you have installed a development system that provides debugging capabilities (such as Microsoft Visual Studio), exceptions that are not handled by your script code will cause a debugger warning dialog box to open for each exception. This is a useful feature to help you debug your script code. Also, you can manually attach the Windows Media Player process to your debugger when logging is enabled.

This SDK includes a sample skin, called "logging", that demonstrates logging functionality in skins. To learn more about using the samples, see [Samples](samples.md).

## Related topics

<dl> <dt>

[**About Skins**](about-skins.md)
</dt> </dl>

 

 




