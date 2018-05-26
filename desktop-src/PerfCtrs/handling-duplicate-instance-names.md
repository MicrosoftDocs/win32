---
Description: Although providers are encouraged to use unique instance names, not all providers do.
ms.assetid: 3c8fcb8d-2ea4-4b24-b649-7bd375c1133d
title: Handling Duplicate Instance Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Handling Duplicate Instance Names

Although providers are encouraged to use unique instance names, not all providers do. The convention for displaying duplicate instance names is to append a \# character and serial number to the instance name, except for the first occurrence of the name. For example, if there are three instances of svchost, the three names are displayed as svchost, svchost\#1, and svchost\#2.

The issue with duplicate instance names is trying to retrieve data for the same instance. Since the instances use the same name, you do not know for sure if you are retrieving data for the same instances since instances can come and go.

For process and thread objects, you can mitigate this issue by setting the **ProcessNameFormat** and **ThreadNameFormat** registry values to 2 under the following registry key.

**HKLM**\\**System**\\**CurrentControlSet**\\**Services**\\**Perfproc**\\**Performance**

The registry type for these values is **REG\_DWORD**. Setting the value to 2 appends the process identifier (PID) to the process instance name and the thread identifier to the thread instance name. To disable this feature, set the value to 1.

 

 



