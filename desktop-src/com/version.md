---
title: Version
description: Specifies the version number of the control.
ms.assetid: ff12c4b3-9548-4135-aaf4-d8b49f9aed41
keywords:
- Version registry key COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Version

Specifies the version number of the control.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Version = value
```

## Remarks

This is a **REG\_SZ** value.

The version number should match the version of the type library associated with the control.

 

 




