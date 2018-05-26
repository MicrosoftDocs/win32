---
Description: Indicates the sharing status of an item Not Shared, Shared, Everyone (homegroup or everyone), or Private.
ms.assetid: 61d8a4fc-d9ad-467f-aa79-b0c208d0e905
title: System.SharingStatus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.SharingStatus

Indicates the sharing status of an item: Not Shared, Shared, Everyone (homegroup or everyone), or Private.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.SharingStatus
   shellPKey = PKEY_SharingStatus
   formatID = EF884C5B-2BFE-41BB-AAE5-76EEDF4F9902
   propID = 300
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotShared
            value = 0
            text = Not shared
            defineToken = SHARINGSTATUS_NOTSHARED
         enum
            name = Shared
            value = 1
            text = Shared
            defineToken = SHARINGSTATUS_SHARED
         enum
            name = Private
            value = 2
            text = Private
            defineToken = SHARINGSTATUS_PRIVATE
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

 

 



