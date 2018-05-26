---
Description: The entry ID for an item within a given catalog in the Windows Search Index.
ms.assetid: 9162e92b-b738-4462-b346-68410f088e95
title: System.Search.EntryID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Search.EntryID

The entry ID for an item within a given catalog in the Windows Search Index.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Search.EntryID
   shellPKey = PKEY_Search_EntryID
   formatID = 49691C90-7E17-101A-A91C-08002B2ECDA9
   propID = 5
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Int32
      IsInnate = true
```

## Remarks

[System.Search.EntryID](shell.props_System_Search_EntryID) is used in the SQL that is generated to query the index. This value is not considered unique over time because it may be recycled.

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

 

 



