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

If [System.ItemType](https://msdn.microsoft.com/library/Bb760781(v=VS.85).aspx) is VT\_EMPTY, the value of this property is also VT\_EMPTY. If the item is a file, the value of this property is the same as if you passed the file's System.ItemType value to [**PSFormatForDisplay**](https://msdn.microsoft.com/library/Bb776496(v=VS.85).aspx).

This property should not be confused with [System.Kind](https://msdn.microsoft.com/library/Bb787521(v=VS.85).aspx), which is a high-level, user-friendly kind name. For example, for a .doc document file, the various properties are as shown here:



| Property                                               | Value                   |
|--------------------------------------------------------|-------------------------|
| [System.Kind](https://msdn.microsoft.com/library/Bb787521(v=VS.85).aspx)                 | Document                |
| [System.ItemType](https://msdn.microsoft.com/library/Bb760781(v=VS.85).aspx)         | .doc                    |
| [System.ItemTypeText](https://msdn.microsoft.com/library/Bb760783(v=VS.85).aspx) | Microsoft Word Document |



 

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

 

 



