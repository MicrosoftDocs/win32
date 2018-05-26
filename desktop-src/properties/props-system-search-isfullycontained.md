---
Description: Emitted as TRUE by all child items of a container (such as an e-mail or a compressed file with a .zip name extension) that emits System.Search.IsClosedDirectory as TRUE. This ensures that the child items are included in the search index.
ms.assetid: 6da60e89-6956-41f6-8624-063c4d46464d
title: System.Search.IsFullyContained
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Search.IsFullyContained

Emitted as **TRUE** by all child items of a container (such as an e-mail or a compressed file with a .zip name extension) that emits [System.Search.IsClosedDirectory](shell.props_System_Search_IsClosedDirectory) as **TRUE**. This ensures that the child items are included in the search index.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Search.IsFullyContained
   shellPKey = PKEY_Search_IsFullyContained
   formatID = 0B63E343-9CCC-11D0-BCDB-00805FCCCE04
   propID = 24
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
```

## Remarks

PKEY values are defined in Propkey.h.

The [System.Search.IsClosedDirectory](shell.props_System_Search_IsClosedDirectory) property helps to optimize indexer performance by allowing the indexer to skip the enumeration of a container's child items. However, those child items are marked by the indexer as not visited, and as such will be deleted from the index. By emitting [System.Search.IsFullyContained](shell.props_System_Search_IsFullyContained) as **TRUE**, an item is not deleted from the index despite having not been visited.

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

 

 



