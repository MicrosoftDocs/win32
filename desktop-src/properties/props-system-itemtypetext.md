---
Description: The user-friendly type name of the item.
ms.assetid: 5d4c86da-6317-4a34-88d6-caf794aaa165
title: System.ItemTypeText
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemTypeText

The user-friendly type name of the item. This value is not intended to be programmatically parsed.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemTypeText
   shellPKey = PKEY_ItemTypeText
   formatID = B725F130-47EF-101A-A5F1-02608C9EEBAC
   propID = 4
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If [System.ItemType](https://www.bing.com/search?q=System.ItemType) is VT\_EMPTY, the value of this property is also VT\_EMPTY. If the item is a file, the value of this property is the same as if you passed the file's System.ItemType value to [**PSFormatForDisplay**](https://www.bing.com/search?q=**PSFormatForDisplay**).

This property should not be confused with [System.Kind](https://www.bing.com/search?q=System.Kind), which is a high-level, user-friendly kind name. For example, for a .doc document file, the various properties are as shown here:



| Property                                               | Value                   |
|--------------------------------------------------------|-------------------------|
| [System.Kind](https://www.bing.com/search?q=System.Kind)                 | Document                |
| [System.ItemType](https://www.bing.com/search?q=System.ItemType)         | .doc                    |
| [System.ItemTypeText](https://www.bing.com/search?q=System.ItemTypeText) | Microsoft Word Document |



 

Example values:



| Path                                   | ItemTypeText            |
|----------------------------------------|-------------------------|
| c:\\mydir\\bar\\hello.txt              | Text File               |
| \\\\server\\share\\mydir\\goodnews.doc | Microsoft Word Document |
| \\\\server\\share\\folder              | File Folder             |
| c:\\MyDir\\MyFolder                    | File Folder             |
| /Mailbox Account/Inbox/'Re: Hello!'    | Outlook E-Mail Message  |



 

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

 

 



