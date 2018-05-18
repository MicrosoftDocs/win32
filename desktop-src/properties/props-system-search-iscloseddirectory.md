---
Description: 'Emitted as TRUE by a container item to indicate that its child items do not need to be enumerated by an indexer if the container item has not changed since the last incremental index verification crawl.'
ms.assetid: '8bb487b9-4a51-4a6b-939e-946a8aad85de'
title: 'System.Search.IsClosedDirectory'
---

# System.Search.IsClosedDirectory

Emitted as **TRUE** by a container item to indicate that its child items do not need to be enumerated by an indexer if the container item has not changed since the last incremental index verification crawl. This contributes to the optimization of indexer performance. In these container cases (examples are an e-mail with attachments or a compressed file with a .zip name extension), child items are inseparable from their parent item. For instance, if the [System.DateModified](shell.props_System_DateModified) property of a contained item changes, then the System.DateModified value of the container changes to match. Also, if a parent item is deleted, all of the child items are deleted as well. Therefore, if the container has not changed, the indexer knows that nothing within it has changed and does not need to open the container to examine the contents individually.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Search.IsClosedDirectory
   shellPKey = PKEY_Search_IsClosedDirectory
   formatID = 0B63E343-9CCC-11D0-BCDB-00805FCCCE04
   propID = 23
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
```

## Remarks

PKEY values are defined in Propkey.h.

> \[!Important\]  
> If an item emits **TRUE** for this property, each of its child items must emit the [System.Search.IsFullyContained](shell.props_System_Search_IsFullyContained) property as **TRUE** to prevent those items from being deleted from the index.

 

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

 

 



