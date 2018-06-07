---
Description: The user-friendly display path to the item.
ms.assetid: 5dd44e13-bc5c-4e32-b5eb-2c7c40e10dfb
title: System.ItemPathDisplayNarrow
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemPathDisplayNarrow

The user-friendly display path to the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemPathDisplayNarrow
   shellPKey = PKEY_ItemPathDisplayNarrow
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 8
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

To optimize for a narrow viewing column, the format of the string should be tailored so that the name comes first.

If the item is a file, the property value excludes the file extension, but includes localized names if they are present. If the item is a message, the value includes the [System.ItemNamePrefix](https://www.bing.com/search?q=System.ItemNamePrefix). To parse an item path, use [System.ItemUrl](https://www.bing.com/search?q=System.ItemUrl) or [System.ParsingPath](https://www.bing.com/search?q=System.ParsingPath).

Example values:



| Path                                   | ItemPathDisplayName                 |
|----------------------------------------|-------------------------------------|
| c:\\mydir\\bar\\hello.txt              | hello (c:\\mydir\\bar)              |
| \\\\server\\share\\mydir\\goodnews.doc | goodnews (\\\\server\\share\\mydir) |
| \\\\server\\share\\folder              | folder (\\\\server\\share)          |
| c:\\MyDir\\MyFolder                    | MyFolder (c:\\mydir)                |
| /Mailbox Account/Inbox/'Re: Hello!'    | Re: Hello! (/Mailbox Account/Inbox) |



 

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

 

 



