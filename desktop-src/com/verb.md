---
title: Verb
description: Specifies the verbs to be registered for an application.
ms.assetid: fc9b3474-6f56-4274-af7d-72e0920c0457
keywords:
- Verb registry key COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Verb

Specifies the verbs to be registered for an application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Verb
         1 = verb1
         2 = verb2
         3 = ...
```

## Remarks

Each verb is a **REG\_SZ** value of the form "*name*, *menu\_flag*, *verb\_flag*". Verbs must be numbered consecutively.

The *name* describes how the verb is appended by an [**AppendMenu**](https://msdn.microsoft.com/library/ms647616(v=VS.85).aspx) function call. For example, "&Play".

The *menu\_flag* value indicates how the verb should appear in the menu. All flags supported by [**AppendMenu**](https://msdn.microsoft.com/library/ms647616(v=VS.85).aspx) are supported, except for MF\_BITMAP, MF\_OWNERDRAW, and MF\_POPUP.

The *verb\_flag* value describes attributes of the verbs. Use one of the values from [**OLEVERBATTRIB**](/windows/desktop/api/OleIdl/ne-oleidl-tagoleverbattrib), or 0.

For more information, see [**OLEVERB**](/windows/desktop/api/OleIdl/ns-oleidl-tagoleverb), [**IOleObject::DoVerb**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-doverb), and [**IOleObject::EnumVerbs**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-enumverbs).

## Related topics

<dl> <dt>

[**AppendMenu**](https://msdn.microsoft.com/library/ms647616(v=VS.85).aspx)
</dt> <dt>

[**OLEVERB**](/windows/desktop/api/OleIdl/ns-oleidl-tagoleverb)
</dt> <dt>

[**OLEVERBATTRIB**](/windows/desktop/api/OleIdl/ne-oleidl-tagoleverbattrib)
</dt> </dl>

 

 




