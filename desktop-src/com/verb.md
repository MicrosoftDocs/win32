---
title: Verb
description: Specifies the verbs to be registered for an application.
ms.assetid: 'bfcad36d-a52a-4117-bf0b-6135b197a7ee'
keywords:
- Verb registry key COM
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

The *name* describes how the verb is appended by an [**AppendMenu**](/windows/win32/api/winuser/nf-winuser-appendmenua) function call. For example, "&Play".

The *menu\_flag* value indicates how the verb should appear in the menu. All flags supported by [**AppendMenu**](/windows/win32/api/winuser/nf-winuser-appendmenua) are supported, except for MF\_BITMAP, MF\_OWNERDRAW, and MF\_POPUP.

The *verb\_flag* value describes attributes of the verbs. Use one of the values from [**OLEVERBATTRIB**](/windows/win32/api/oleidl/ne-oleidl-oleverbattrib), or 0.

For more information, see [**OLEVERB**](/windows/win32/api/oleidl/ns-oleidl-oleverb), [**IOleObject::DoVerb**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-doverb), and [**IOleObject::EnumVerbs**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-enumverbs).

## Related topics

<dl> <dt>

[**AppendMenu**](/windows/win32/api/winuser/nf-winuser-appendmenua)
</dt> <dt>

[**OLEVERB**](/windows/win32/api/oleidl/ns-oleidl-oleverb)
</dt> <dt>

[**OLEVERBATTRIB**](/windows/win32/api/oleidl/ne-oleidl-oleverbattrib)
</dt> </dl>

 

 