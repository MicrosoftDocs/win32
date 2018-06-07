---
Description: Identifies the file extension of the file-based item, including the leading period.
ms.assetid: b72c695e-bdbd-471d-b902-9e30a62facd4
title: System.FileExtension
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.FileExtension

Identifies the file extension of the file-based item, including the leading period. This property is derived from System.FileName. If System.FileName either does not have a file extension or is VT\_EMPTY, the value for this property should be VT\_EMPTY.

To obtain the type of any item (including an item that is not a file), use System.ItemType.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.FileExtension
   shellPKey = PKEY_FileExtension
   formatID = E4F10A3C-49E6-405D-8288-A23BD4EEAA6C
   propID = 100
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If [System.FileName](https://www.bing.com/search?q=System.FileName) is VT\_EMPTY, this property should also be empty. Otherwise, this property should be derived appropriately by the data source from System.FileName. If System.FileName does not include a file extension, [System.FileExtension](https://www.bing.com/search?q=System.FileExtension) should be VT\_EMPTY. To obtain the type of any item (including an item that is not a file), use [System.ItemType](https://www.bing.com/search?q=System.ItemType).

Path and file extension property examples. 

| Path                               | File Extension |
|------------------------------------|----------------|
| c:\\files\\personal\\hello.txt     | .txt           |
| \\\\server\\share\\mydir\\news.doc | .doc           |
| \\\\server\\share\\numbers.xls     | .xls           |
| \\\\server\\share\\folder          | VT\_EMPTY      |
| c:\\Stuff\\MyFolder                | VT\_EMPTY      |
| \[desktop\]                        | VT\_EMPTY      |



 

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

 

 



