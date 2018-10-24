---
Description: Emitted as TRUE by all child items of a container (such as an e-mail or a compressed file with a .zip name extension) that emits System.Search.IsClosedDirectory as TRUE. This ensures that the child items are included in the search index.
ms.assetid: 6da60e89-6956-41f6-8624-063c4d46464d
title: System.Search.IsFullyContained
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Search.IsFullyContained

Emitted as **TRUE** by all child items of a container (such as an e-mail or a compressed file with a .zip name extension) that emits [System.Search.IsClosedDirectory](https://msdn.microsoft.com/library/Bb760168(v=VS.85).aspx) as **TRUE**. This ensures that the child items are included in the search index.

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

The [System.Search.IsClosedDirectory](https://msdn.microsoft.com/library/Bb760168(v=VS.85).aspx) property helps to optimize indexer performance by allowing the indexer to skip the enumeration of a container's child items. However, those child items are marked by the indexer as not visited, and as such will be deleted from the index. By emitting [System.Search.IsFullyContained](https://msdn.microsoft.com/library/Bb760169(v=VS.85).aspx) as **TRUE**, an item is not deleted from the index despite having not been visited.

## Related topics

<dl> <dt>

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

 

 



