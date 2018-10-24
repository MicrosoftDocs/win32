---
Description: The Shell namespace path to the target of the link item.
ms.assetid: 05bd6cae-68b2-49ce-ad4f-e395ec88407a
title: System.Link.TargetParsingPath
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Link.TargetParsingPath

The Shell namespace path to the target of the link item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Link.TargetParsingPath
   shellPKey = PKEY_Link_TargetParsingPath
   formatID = B9B4B3FC-2B51-4A42-B5D8-324146AFCF25
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

This path can be passed to [**SHParseDisplayName**](https://msdn.microsoft.com/en-us/library/Bb762236(v=VS.85).aspx) to parse the path to the correct Shell folder. If the target item is a file, the value is identical to [System.ItemPathDisplay](https://msdn.microsoft.com/library/Bb760776(v=VS.85).aspx).If the target item cannot be accessed through the Shell namespace, this value is VT\_EMPTY.

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

 

 



