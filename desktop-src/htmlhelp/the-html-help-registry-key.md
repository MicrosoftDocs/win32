---
title: The HTML Help Registry Key
description: You can determine if HTML Help is installed on a computer by checking for the HTML Help registry key.
ms.assetid: 40599795-1278-42bf-941A-BBF8CFFB3843
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The HTML Help Registry Key

You can determine if HTML Help is installed on a computer by checking for the HTML Help registry key.

1.  Click **Start**, and then click **Run**.
2.  Type **regedit** in the **Open** box, and then click **OK**. This will open the Microsoft Registry Editor.
3.  Click **Find** on the **Edit** menu, and then search for the following CLSID:

    52A2AAAE-085D-4187-97EA-8C30DB990436

    This is the CLSID of the HTML Help ActiveX Control (Hhctrl.ocx) in Windows XP SP1 and later. It is registered by the system during setup. If Hhctrl.ocx is installed on your system, the CLSID will be found under HKEY\_CLASSES\_ROOT/CLSID. If it is not found, Hhctrl.ocx is not installed.

> \[!Important\]  
> Use extreme caution when viewing your registry with the Registry Editor. Changing anything in the registry can adversely affect how your system functions.

 

 

 




