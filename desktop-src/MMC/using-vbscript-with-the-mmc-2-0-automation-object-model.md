---
title: Using VBScript with the MMC 2.0 Automation Object Model
description: The following VBScript example code is for a simple application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '592ae7ec-bd02-43b2-8911-bb7dce883e18'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Using VBScript with the MMC 2.0 Automation Object Model

The following VBScript example code is for a simple application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.

## Example Code


```VB
Option Explicit

Wscript.Echo "This script uses the MMC 2.0 Application object."

' Create the MMC Application object.
Dim objMMC
Set objMMC = Wscript.CreateObject("MMC20.Application")

' Show the MMC application.
objMMC.Show

' Add the "Folder" snap-in to the console.
objMMC.Document.SnapIns.Add("Folder")


' Set MMC status bar text.
objMMC.Document.ActiveView.StatusBarText = "This is the left pane|middle pane|right pane"

' Leave the MMC application in user control when this script ends.
objMMC.UserControl = 1

Wscript.Echo vbNewLine + "The script has ended. MMC is in user control."
```



## Related topics

<dl> <dt>

[Retrieving a Snap-in's List View Results](retrieving-a-snap-in-s-list-view-results.md)
</dt> </dl>

 

 




