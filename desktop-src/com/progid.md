---
title: ProgID
description: Associates a ProgID with a CLSID.
ms.assetid: 89fb20af-65bf-4ed4-9f71-eb707ee8eb09
keywords:
- ProgID registry key COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProgID

Associates a ProgID with a CLSID.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      ProgID = value
```

## Remarks

Every insertable object class has a ProgID. For information on creating a ProgID, see the [<ProgID&gt; key](-progid--key.md).

## Related topics

<dl> <dt>

[<ProgID&gt; key](-progid--key.md)
</dt> <dt>

[**VersionIndependentProgID**](versionindependentprogid.md)
</dt> </dl>

 

 




