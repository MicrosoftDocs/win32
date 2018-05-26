---
title: AutoTreatAs
description: Automatically sets the CLSID for the TreatAs key to the specified value.
ms.assetid: 5adf7bc5-a4d6-444d-bd56-0c4e6eee5111
keywords:
- AutoTreatAs registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AutoTreatAs

Automatically sets the CLSID for the [**TreatAs**](treatas.md) key to the specified value.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      AutoTreatAs = value
```

## Remarks

This is a **REG\_SZ** value that specifies the class identifier.

## Related topics

<dl> <dt>

[**CoTreatAsClass**](/windows/win32/Objbase/nf-objbase-cotreatasclass?branch=master)
</dt> </dl>

 

 




