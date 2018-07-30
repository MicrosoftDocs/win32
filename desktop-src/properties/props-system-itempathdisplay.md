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

Unlike [System.ItemUrl](https://msdn.microsoft.com/library/Bb760785(v=VS.85).aspx), this property value does not include the URL scheme. To parse an item path, use System.ItemUrl or [System.ParsingPath](https://msdn.microsoft.com/library/Bb787547(v=VS.85).aspx). To reference Shell namespace items using Shell APIs, use System.ParsingPath.

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

 

 



