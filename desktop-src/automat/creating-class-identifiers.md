---
title: Creating Class Identifiers
description: CLSIDs are universally unique identifiers (UUIDs, also called globally unique identifiers, or GUIDs) that identify class objects to OLE.
ms.assetid: a802d92e-2116-4d7e-9a16-df3d889337a2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Class Identifiers

Each object that is exposed for creation must have a unique class identifier (CLSID). CLSIDs are universally unique identifiers (UUIDs, also called globally unique identifiers, or GUIDs) that identify class objects to OLE. The CLSID is included in an application, and must be registered with the operating system when an application is installed.

To generate UUIDs, run the Guidgen.exe utility. By default, Guidgen.exe puts a DEFINE\_GUID macro on the Windows Clipboard, which can then be pasted into your source code.

 

 




