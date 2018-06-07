---
Description: The user-friendly display name of an item's parent folder.
ms.assetid: 4049b6cb-41a1-4df6-89d1-a2022d3a285d
title: System.ItemFolderNameDisplay
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemFolderNameDisplay

The user-friendly display name of an item's parent folder.

This is derived from [System.ItemFolderPathDisplay](https://www.bing.com/search?q=System.ItemFolderPathDisplay). If that property is VT\_EMPTY, then this property should be too.

If the folder is a file folder, the value will be localized if a localized name is available.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemFolderNameDisplay
   shellPKey = PKEY_ItemFolderNameDisplay
   formatID = B725F130-47EF-101A-A5F1-02608C9EEBAC
   propID = 2
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If [System.ItemFolderPathDisplay](https://www.bing.com/search?q=System.ItemFolderPathDisplay) is VT\_EMPTY, then this property should also be empty. Otherwise, it should be derived appropriately by the data source from System.ItemFolderPathDisplay.

Examples:



| Given path                             | Folder Display Name |
|----------------------------------------|---------------------|
| c:\\MyFiles\\Text\\hello.txt           | Text                |
| \\\\server\\share\\mydir\\goodnews.doc | mydir               |
| \\\\server\\share\\numbers.xls         | share               |
| c:\\Folders\\MyFolder                  | Folders             |
| /Mailbox Account/Inbox/'Re: Hello!'    | Inbox               |



 

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

 

 



