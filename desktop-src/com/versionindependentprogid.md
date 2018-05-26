---
title: VersionIndependentProgID
description: Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application.
ms.assetid: 5d188db9-ea4f-47fe-882f-a6caa7e86a25
keywords:
- VersionIndependentProgID registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VersionIndependentProgID

Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      VersionIndependentProgID = Program.Component
```

## Remarks

This is a **REG\_SZ** value that specifies the latest version of the object application.

The version-independent ProgID is stored and maintained solely by application code. When given the version-independent ProgID, the [**CLSIDFromProgID**](/windows/win32/combaseapi/nf-combaseapi-clsidfromprogid?branch=master) function returns the CLSID of the current version.

You can use [**CLSIDFromProgID**](/windows/win32/combaseapi/nf-combaseapi-clsidfromprogid?branch=master) and [**ProgIDFromCLSID**](/windows/win32/combaseapi/nf-combaseapi-progidfromclsid?branch=master) to convert between these two representations.

 

 




