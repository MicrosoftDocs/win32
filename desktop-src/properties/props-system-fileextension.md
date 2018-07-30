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

If [System.FileName](https://msdn.microsoft.com/library/Bb760703(v=VS.85).aspx) is VT\_EMPTY, this property should also be empty. Otherwise, this property should be derived appropriately by the data source from System.FileName. If System.FileName does not include a file extension, [System.FileExtension](https://msdn.microsoft.com/library/Bb760699(v=VS.85).aspx) should be VT\_EMPTY. To obtain the type of any item (including an item that is not a file), use [System.ItemType](https://msdn.microsoft.com/library/Bb760781(v=VS.85).aspx).

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

 

 



