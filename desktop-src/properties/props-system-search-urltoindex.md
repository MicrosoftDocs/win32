---
Description: Emitted by a container IFilter for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.
ms.assetid: e864b3fa-6d43-40fe-9556-474953098947
title: System.Search.UrlToIndex
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Search.UrlToIndex

Emitted by a container [**IFilter**](https://www.bing.com/search?q=**IFilter**) for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.

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

This property contains a URL and is emitted by a protocol handler for each child URL or directoy under the current URL. The indexer calls back into the protocol handler, and asks for that document to be indexed. [System.Search.UrlToIndex](https://www.bing.com/search?q=System.Search.UrlToIndex) was called PID\_GTHR\_DIRLINK in earlier versions of the Windows operating system.

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[System.Search.UrlToIndexWithModificationTime](https://www.bing.com/search?q=System.Search.UrlToIndexWithModificationTime)
</dt> <dt>

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

 

 



