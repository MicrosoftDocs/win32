---
description: Emitted by a container IFilter for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.
ms.assetid: e864b3fa-6d43-40fe-9556-474953098947
title: System.Search.UrlToIndex
ms.topic: article
ms.date: 05/31/2018
---

# System.Search.UrlToIndex

Emitted by a container [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.

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

This property contains a URL and is emitted by a protocol handler for each child URL or directoy under the current URL. The indexer calls back into the protocol handler, and asks for that document to be indexed. [System.Search.UrlToIndex](/previous-versions/windows/desktop/legacy/bb760177(v=vs.85)) was called PID\_GTHR\_DIRLINK in earlier versions of the Windows operating system.

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[System.Search.UrlToIndexWithModificationTime](./props-system-search-urltoindexwithmodificationtime.md)
</dt> <dt>

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

 

 
