---
Description: The user-friendly display path to the item.
ms.assetid: 27e4490b-7914-4b38-9799-e9d5dc407f13
title: System.ItemPathDisplay
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemPathDisplay

The user-friendly display path to the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemPathDisplay
   shellPKey = PKEY_ItemPathDisplay
   formatID = E3E0584C-B788-4A5A-BB20-7F5A44C9ACDD
   propID = 7
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If the item is a file or folder, this property includes the extension in all cases, and is localized if a localized name is available. For other items, this is the user-friendly equivalent, assuming that the item exists in hierarchical storage.

Unlike [System.ItemUrl](https://www.bing.com/search?q=System.ItemUrl), this property value does not include the URL scheme. To parse an item path, use System.ItemUrl or [System.ParsingPath](https://www.bing.com/search?q=System.ParsingPath). To reference Shell namespace items using Shell APIs, use System.ParsingPath.

Example values:



| Path                                   | ItemPathDisplay                        |
|----------------------------------------|----------------------------------------|
| c:\\mydir\\bar\\hello.txt              | c:\\mydir\\bar\\hello.txt              |
| \\\\server\\share\\mydir\\goodnews.doc | \\\\server\\share\\mydir\\goodnews.doc |
| \\\\server\\share\\numbers.xls         | \\\\server\\share\\numbers.xls         |
| c:\\mydir\\MyFolder                    | c:\\mydir\\MyFolder                    |
| /Mailbox Account/Inbox/'Re: Hello!'    | /Mailbox Account/Inbox/'Re: Hello!'    |



 

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

 

 



