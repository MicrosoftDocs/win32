---
title: Running a Troubleshooting Pack
description: Users can launch the troubleshooting packs or an application can detect an issue and prompt the user to start a troubleshooting pack.
ms.assetid: 72cc7166-55b2-421b-a342-104aff4e43c4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Running a Troubleshooting Pack

Users can launch the troubleshooting packs or an application can detect an issue and prompt the user to start a troubleshooting pack. To run the troubleshooting pack from the WTP wizard (MSDT.exe), use one of the following methods to launch the pack:

-   Double-click the DIAGCAB file if the pack is contained in a cabinet file.
-   Double-click the DIAGPKG file.
-   Use the MSDT -Path argument to specify the path to pack folder.
-   Use the MSDT -Cab argument to specify the path to the pack's DIAGCAB file.

To run a troubleshooting pack in the Windows PowerShell window, use the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) cmdlet to get the pack object and then pass it to the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet. When you run the pack in the Windows PowerShell window, the interactions are translated to text prompts. To use the modules, you must first call Import-Module to import the modules (for example, **Import-Module TroubleshootingPack**). For examples on using these cmdlets, see the documentation for each cmdlet.

 

 




