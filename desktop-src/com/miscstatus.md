---
title: MiscStatus
description: Specifies how to create and display an object.
ms.assetid: '585b2d1e-3edb-494e-a61e-bbfa6eae2ba1'
keywords:
- MiscStatus registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# MiscStatus

Specifies how to create and display an object.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      MiscStatus
         (Default) = value
         aspect = value
```

## Remarks

For more information, see the [**OLEMISC**](/windows/win32/api/oleidl/ne-oleidl-olemisc) enumeration and [**IOleObject::GetMiscStatus**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getmiscstatus).

If no subkey that corresponds to a DVASPECT is found, the default value of **MiscStatus** is used.

## Related topics

<dl> <dt>

[**IOleObject::GetMiscStatus**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getmiscstatus)
</dt> </dl>

 

 




