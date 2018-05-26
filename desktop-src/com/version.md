---
title: Version
description: Specifies the version number of the control.
ms.assetid: ff12c4b3-9548-4135-aaf4-d8b49f9aed41
keywords:
- Version registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

 

 




