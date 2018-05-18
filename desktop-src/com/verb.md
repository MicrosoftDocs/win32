---
title: Verb
description: Specifies the verbs to be registered for an application.
ms.assetid: 'fc9b3474-6f56-4274-af7d-72e0920c0457'
keywords: ["Verb registry key COM"]
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

The *name* describes how the verb is appended by an [**AppendMenu**](_win32_AppendMenu_cpp) function call. For example, "&Play".

The *menu\_flag* value indicates how the verb should appear in the menu. All flags supported by [**AppendMenu**](_win32_AppendMenu_cpp) are supported, except for MF\_BITMAP, MF\_OWNERDRAW, and MF\_POPUP.

The *verb\_flag* value describes attributes of the verbs. Use one of the values from [**OLEVERBATTRIB**](oleverbattrib.md), or 0.

For more information, see [**OLEVERB**](oleverb.md), [**IOleObject::DoVerb**](ioleobject-doverb.md), and [**IOleObject::EnumVerbs**](ioleobject-enumverbs.md).

## Related topics

<dl> <dt>

[**AppendMenu**](_win32_AppendMenu_cpp)
</dt> <dt>

[**OLEVERB**](oleverb.md)
</dt> <dt>

[**OLEVERBATTRIB**](oleverbattrib.md)
</dt> </dl>

 

 




