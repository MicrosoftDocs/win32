---
title: AuxUserType
description: Specifies an application's short display name and application names.
ms.assetid: 3367eb68-01f4-4cb9-b1d0-27554c28b68d
keywords:
- AuxUserType registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# AuxUserType

Specifies an application's short display name and application names.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      AuxUserType
         2 = ShortDisplayName
         3 = ApplicationName
```

## Remarks

The recommended maximum length for *ShortDisplayName* is 15 characters. This name is used in menus, including pop-up menus.

*ApplicationName* should contain the actual name of the application (such as "Acme Draw 2.0"). This name is used in the **Results** field of the **Paste Special** dialog box.

## Related topics

<dl> <dt>

[**IOleObject::GetUserType**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getusertype)
</dt> </dl>

 

 




