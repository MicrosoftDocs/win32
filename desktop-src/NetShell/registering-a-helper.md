---
title: Registering a Helper
description: Helpers should register themselves in the Windows registry during their installation process.
ms.assetid: 41548a13-5785-471b-ab3e-09a066c467bc
keywords:
- helper NetSh , registering
- NetShell NetSh , tasks, registering a helper
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering a Helper

Helpers should register themselves in the Windows registry during their installation process. NetShell stores its list of installed helper DLLs in the following location:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\NetSh**

A set of string values reside in this key. There value name should be the same as the name of the DLL without the .dll extension (for example, *sample*). The value data is the DLL name with the extension (for example, *sample.dll*). If the DLL resides in a common location, such as the winnt\\system32 directory, the full path name is not required.

 

 




