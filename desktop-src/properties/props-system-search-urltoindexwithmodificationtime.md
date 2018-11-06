---
Description: This property is the same as System.Search.UrlToIndex except that it includes the time that the URL was last modified.
ms.assetid: 53ca765b-0795-49ab-9946-c3ef101ababd
title: System.Search.UrlToIndexWithModificationTime
ms.topic: article
ms.date: 05/31/2018
---

# System.Search.UrlToIndexWithModificationTime

This property is the same as [**System.Search.UrlToIndex**](props-system-search-urltoindex.md) except that it includes the time that the URL was last modified. This is an optimization for the indexer so that it does not have to call back into the protocol handler to ask for this information to determine whether the content needs to be indexed again.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Search.UrlToIndexWithModificationTime
   shellPKey = PKEY_Search_UrlToIndexWithModificationTime
   formatID = 0B63E343-9CCC-11D0-BCDB-00805FCCCE04
   propID = 12
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Multivalue Any
```

## Remarks

This [System.Search.UrlToIndexWithModificationTime](https://msdn.microsoft.com/library/Bb760179(v=VS.85).aspx) property is the same as the [System.Search.UrlToIndex](https://msdn.microsoft.com/library/Bb760177(v=VS.85).aspx) property, except that you also pass in the last modified time of the document. If the last modified time matches, the indexer assumes that the document is already indexed and throws away the notification. This property is a vector with two elements, a **VT\_LPWSTR** value that contains the URL and a **VT\_FILETIME** value that contains the last modified time.

[System.Search.UrlToIndexWithModificationTime](https://msdn.microsoft.com/library/Bb760179(v=VS.85).aspx) was called PID\_GTHR\_DIRLINK\_WITH\_TIME in earlier versions of the Windows operating system.

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[System.Search.UrlToIndex](https://msdn.microsoft.com/library/Bb760177(v=VS.85).aspx)
</dt> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> </dl>

 

 



