---
Description: The Shell namespace path to the target of the link item.
ms.assetid: 05bd6cae-68b2-49ce-ad4f-e395ec88407a
title: System.Link.TargetParsingPath
ms.technology: desktop
ms.prod: windows
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

This path can be passed to [**SHParseDisplayName**](https://msdn.microsoft.com/7bdfeed5-dcd0-40f6-a9d0-08ce816ee055) to parse the path to the correct Shell folder. If the target item is a file, the value is identical to [System.ItemPathDisplay](https://www.bing.com/search?q=System.ItemPathDisplay).If the target item cannot be accessed through the Shell namespace, this value is VT\_EMPTY.

## Related topics

<dl> <dt>

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> </dl>

 

 



