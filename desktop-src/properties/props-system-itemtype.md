---
Description: The canonical type of the item.
ms.assetid: 530ba98a-09fd-438b-8872-9eee47f0cf54
title: System.ItemType
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemType

The canonical type of the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemType
   shellPKey = PKEY_ItemType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 11
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

The value for System.ItemType is intended to be programmatically parsed, and can be either:

-   A file extension that points to a ProgID value (HKEY\_CLASSES\_ROOT\\<ProgID>) holding the display name for the type.
-   A ProgID value (HKEY\_CLASSES\_RROOT\\<ProgID>), containing the display name for the type.

The FriendlyTypeName element of a ProgID should be a localized version of the application name (@winword.dll,-42), while the default value of the ProgID key is a non-localized name (Word.Document.12).

If there is no canonical type, the value is VT\_EMPTY. If the item is a file ([System.FileName](https://msdn.microsoft.com/library/Bb760703(v=VS.85).aspx) is not VT\_EMPTY), the value is the same as [System.FileExtension](https://msdn.microsoft.com/library/Bb760699(v=VS.85).aspx). Use [System.ItemTypeText](https://msdn.microsoft.com/library/Bb760783(v=VS.85).aspx) when you want to display the type to end users in a view.

> [!Note]  
> If the item is a file, passing the [System.ItemType](https://msdn.microsoft.com/library/Bb760781(v=VS.85).aspx) value to [**PSFormatForDisplay**](https://msdn.microsoft.com/library/Bb776496(v=VS.85).aspx) results in the same value as [System.ItemTypeText](https://msdn.microsoft.com/library/Bb760783(v=VS.85).aspx).

 

Example values:



| Path                                   | ItemType         |
|----------------------------------------|------------------|
| c:\\mydir\\bar\\hello.txt              | .txt             |
| \\\\server\\share\\mydir\\goodnews.doc | .doc             |
| \\\\server\\share\\folder              | Directory        |
| c:\\MyDir\\MyFolder                    | Directory        |
| \[desktop\]                            | Folder           |
| /Mailbox Account/Inbox/'Re: Hello!'    | MAPI/IPM.Message |



 

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
</dt> <dt>

[Programmatic Identifiers](https://msdn.microsoft.com/en-us/library/Cc144152(v=VS.85).aspx)
</dt> </dl>

 

 



