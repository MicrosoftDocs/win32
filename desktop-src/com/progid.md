---
title: ProgID
description: Associates a ProgID with a CLSID.
ms.assetid: 89fb20af-65bf-4ed4-9f71-eb707ee8eb09
keywords:
- ProgID registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Every insertable object class has a ProgID. For information on creating a ProgID, see the [&lt;ProgID&gt; key](-progid--key.md).

## Related topics

<dl> <dt>

[&lt;ProgID&gt; key](-progid--key.md)
</dt> <dt>

[**VersionIndependentProgID**](versionindependentprogid.md)
</dt> </dl>

 

 




