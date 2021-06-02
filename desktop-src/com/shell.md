---
title: Shell (COM)
description: Provides Windows 3.1 shell printing and File Open information.
ms.assetid: 15e329f2-ed64-4940-aa00-63edbd283b07
keywords:
- Shell registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Shell (COM)

Provides Windows 3.1 shell printing and **File Open** information.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes
   {ProgID}
      Shell
         Open
            command = path %1
         Print
            command = path %1
```

## Remarks

These entries should provide the path and file name of the application.

 

 




