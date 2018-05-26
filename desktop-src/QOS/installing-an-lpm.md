---
title: Installing an LPM
description: For additional LPMs to function on a system, you must install the LPM on the server computer on which it will function. Note that the Microsoft-provided LPM, Msidlpm.dll, is installed by default with Windows Quality of Service.
ms.assetid: 90cbbb9e-037a-4e23-a359-89ee8f1248e8
keywords:
- Quality of Service QOS , tasks, installing a local policy module
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installing an LPM

For additional LPMs to function on a system, you must install the LPM on the server computer on which it will function. Note that the Microsoft-provided LPM, Msidlpm.dll, is installed by default with Windows Quality of Service.

**To install an LPM on a system**

1.  Create a registry entry. The key in which the entry must be created is **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\RSVP\\PCM Config\\ActiveLPMs**
    1.  The entry type is REG\_MULTI\_SZ
    2.  The value of the entry is the name of the LPM DLL
2.  Place the DLL into the Windows system directory.

 

 




