---
Description: The user-friendly display path to the item.
ms.assetid: 5dd44e13-bc5c-4e32-b5eb-2c7c40e10dfb
title: System.ItemPathDisplayNarrow
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

If the item is a file, the property value excludes the file extension, but includes localized names if they are present. If the item is a message, the value includes the [System.ItemNamePrefix](https://msdn.microsoft.com/library/Bb760772(v=VS.85).aspx). To parse an item path, use [System.ItemUrl](https://msdn.microsoft.com/library/Bb760785(v=VS.85).aspx) or [System.ParsingPath](https://msdn.microsoft.com/library/Bb787547(v=VS.85).aspx).

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

 

 



