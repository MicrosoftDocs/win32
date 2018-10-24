---
Description: The display name in &\#0034;most complete&\#0034; form.
ms.assetid: fdb6b0fa-0741-4edc-8902-763a461313b9
title: System.ItemNameDisplay
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemNameDisplay

The display name in "most complete" form. It is the unique representation of the item name most appropriate for end users.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemNameDisplay
   shellPKey = PKEY_ItemNameDisplay
   formatID = B725F130-47EF-101A-A5F1-02608C9EEBAC
   propID = 10
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

This value is the concatentation of [System.ItemNamePrefix](https://msdn.microsoft.com/library/Bb760772(v=VS.85).aspx) and [System.ItemName](https://msdn.microsoft.com/library/Bb760768(v=VS.85).aspx).

If the item is a file, this property includes the extension in all cases and is localized if a localized name is available. There are acceptable cases when [System.FileName](https://msdn.microsoft.com/library/Bb760703(v=VS.85).aspx) is given but the value of this property is completely different. E-mail messages are a good example. If the item is an e-mail message, the item name is normally the subject. In that case, the value must be the concatenation of [System.ItemNamePrefix](https://msdn.microsoft.com/library/Bb760772(v=VS.85).aspx) and [System.ItemName](https://msdn.microsoft.com/library/Bb760768(v=VS.85).aspx). Since the value of System.ItemNamePrefix excludes any trailing spaces, the concatenation must include a space when generating [System.ItemNameDisplay](https://msdn.microsoft.com/library/Bb760770(v=VS.85).aspx). Note that this property is not guaranteed to be unique, but is designed to promote the most likely candidate that can be unique and also makes sense to end users.

For example, for documents, the [System.Title](https://msdn.microsoft.com/library/Bb787584(v=VS.85).aspx) could be used as the [System.ItemNameDisplay](https://msdn.microsoft.com/library/Bb760770(v=VS.85).aspx), but in practice the title of the documents may not be useful or unique enough to function as the sole System.ItemNameDisplay. Instead, providing [System.FileName](https://msdn.microsoft.com/library/Bb760703(v=VS.85).aspx) as the value of System.ItemNameDisplay is a better choice. In Windows Mail, e-mail is stored in the file system as .eml files. The System.FileName values for those files are not human-friendly as they are GUIDs. In this example, promoting [System.Subject](https://msdn.microsoft.com/library/Bb787576(v=VS.85).aspx) as System.ItemNameDisplay makes more sense.

**Compatibility notes:**

-   Shell folder implementations on Windows Vista: use PKEY\_ItemNameDisplay for the name column when you want Windows Explorer to call [**IShellFolder::GetDisplayNameOf**](https://msdn.microsoft.com/en-us/library/Bb775071(v=VS.85).aspx)(SHGDN\_NORMAL) to get the value of the name. Use another PKEY, such as PKEY\_ItemName, when you want Windows Explorer to call either the folder's property store or [**IShellFolder2::GetDetailsEx**](https://msdn.microsoft.com/en-us/library/Bb775051(v=VS.85).aspx) to get the value of the name.
-   Shell folder implementations on Windows XP: the first column must be the name column, and Windows Explorer calls [**IShellFolder::GetDisplayNameOf**](https://msdn.microsoft.com/en-us/library/Bb775071(v=VS.85).aspx) to get the value of the name. The PKEY/SCID does not matter.



| Item type     | Example                   |
|---------------|---------------------------|
| File          | hello.txt                 |
| Message       | Re: Where is the meeting? |
| Device folder | song.wma                  |
| Folder        | Documents                 |



 

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

 

 



