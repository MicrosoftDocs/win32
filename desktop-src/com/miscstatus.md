---
title: MiscStatus
description: Specifies how to create and display an object.
ms.assetid: de279d46-057e-4c3a-8af3-14f7b65147fd
keywords:
- MiscStatus registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

For more information, see the [**OLEMISC**](/windows/win32/OleIdl/ne-oleidl-tagolemisc?branch=master) enumeration and [**IOleObject::GetMiscStatus**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getmiscstatus?branch=master).

If no subkey that corresponds to a DVASPECT is found, the default value of **MiscStatus** is used.

## Related topics

<dl> <dt>

[**IOleObject::GetMiscStatus**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getmiscstatus?branch=master)
</dt> </dl>

 

 




