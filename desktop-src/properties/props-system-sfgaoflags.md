---
description: SFGAO values as used in IShellFolder::GetAttributesOf.
ms.assetid: 0a63e019-a03c-43c2-b2dc-20ef7c37e0d3
title: System.SFGAOFlags
ms.topic: article
ms.date: 05/31/2018
---

# System.SFGAOFlags

[**SFGAO**](../shell/sfgao.md) values as used in [**IShellFolder::GetAttributesOf**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof).

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.SFGAOFlags
   shellPKey = PKEY_SFGAOFlags
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 25
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
```

## Windows Vista

```
propertyDescription
   name = System.SFGAOFlags
   shellPKey = PKEY_SFGAOFlags
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 25
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

Certain [**SFGAO**](../shell/sfgao.md) values that are considered to cause slow calculations or lack context are excluded here by the application of the [****SFGAO\_PKEYSFGAOMASK****](../shell/sfgao.md) mask.

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> </dl>

 

 
