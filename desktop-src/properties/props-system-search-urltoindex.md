---
Description: 'Emitted by a container IFilter for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.'
ms.assetid: 'e864b3fa-6d43-40fe-9556-474953098947'
title: 'System.Search.UrlToIndex'
---

# System.Search.UrlToIndex

Emitted by a container [**IFilter**](search._search_IFilter) for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Search.UrlToIndex
   shellPKey = PKEY_Search_UrlToIndex
   formatID = 0B63E343-9CCC-11D0-BCDB-00805FCCCE04
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
```

## Remarks

This property contains a URL and is emitted by a protocol handler for each child URL or directoy under the current URL. The indexer calls back into the protocol handler, and asks for that document to be indexed. [System.Search.UrlToIndex](shell.props_System_Search_UrlToIndex) was called PID\_GTHR\_DIRLINK in earlier versions of the Windows operating system.

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[System.Search.UrlToIndexWithModificationTime](shell.props_System_Search_UrlToIndexWithModificationTime)
</dt> <dt>

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

 

 



