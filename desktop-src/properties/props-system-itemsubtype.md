---
Description: Describes the sub-type of an item.
ms.assetid: 7b949b2a-77c9-41d3-90f3-f2ba4cfa2762
title: System.ItemSubType
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ItemSubType

Describes the sub-type of an item. The value is intended for display to the user.In contrast to System.ItemType, which is generally used to describe a class of itemsthat all have the same common content format, System.ItemSubType may differ based onthe individual contents or purpose of the item.For example, this property may be used to identify an item with System.ItemType = "jpg"as System.ItemSubType = "Panorama" or System.ItemSubType = "Smart Shot".

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507

```
propertyDescription
   name = System.ItemSubType
   shellPKey = PKEY_ItemSubType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 37
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = false
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> </dl>

 

 



