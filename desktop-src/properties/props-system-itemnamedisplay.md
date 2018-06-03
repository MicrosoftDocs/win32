---
Description: The display name in &\#0034;most complete&\#0034; form.
ms.assetid: fdb6b0fa-0741-4edc-8902-763a461313b9
title: System.ItemNameDisplay
ms.technology: desktop
ms.prod: windows
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

This value is the concatentation of [System.ItemNamePrefix](https://www.bing.com/search?q=System.ItemNamePrefix) and [System.ItemName](https://www.bing.com/search?q=System.ItemName).

If the item is a file, this property includes the extension in all cases and is localized if a localized name is available. There are acceptable cases when [System.FileName](https://www.bing.com/search?q=System.FileName) is given but the value of this property is completely different. E-mail messages are a good example. If the item is an e-mail message, the item name is normally the subject. In that case, the value must be the concatenation of [System.ItemNamePrefix](https://www.bing.com/search?q=System.ItemNamePrefix) and [System.ItemName](https://www.bing.com/search?q=System.ItemName). Since the value of System.ItemNamePrefix excludes any trailing spaces, the concatenation must include a space when generating [System.ItemNameDisplay](https://www.bing.com/search?q=System.ItemNameDisplay). Note that this property is not guaranteed to be unique, but is designed to promote the most likely candidate that can be unique and also makes sense to end users.

For example, for documents, the [System.Title](https://www.bing.com/search?q=System.Title) could be used as the [System.ItemNameDisplay](https://www.bing.com/search?q=System.ItemNameDisplay), but in practice the title of the documents may not be useful or unique enough to function as the sole System.ItemNameDisplay. Instead, providing [System.FileName](https://www.bing.com/search?q=System.FileName) as the value of System.ItemNameDisplay is a better choice. In Windows Mail, e-mail is stored in the file system as .eml files. The System.FileName values for those files are not human-friendly as they are GUIDs. In this example, promoting [System.Subject](https://www.bing.com/search?q=System.Subject) as System.ItemNameDisplay makes more sense.

**Compatibility notes:**

-   Shell folder implementations on Windows Vista: use PKEY\_ItemNameDisplay for the name column when you want Windows Explorer to call [**IShellFolder::GetDisplayNameOf**](https://msdn.microsoft.com/windows/desktop/2164bbe6-e030-4a64-85db-9ee1cd3c136d)(SHGDN\_NORMAL) to get the value of the name. Use another PKEY, such as PKEY\_ItemName, when you want Windows Explorer to call either the folder's property store or [**IShellFolder2::GetDetailsEx**](https://msdn.microsoft.com/windows/desktop/f006828c-980d-4e36-be68-3b3c238cd884) to get the value of the name.
-   Shell folder implementations on Windows XP: the first column must be the name column, and Windows Explorer calls [**IShellFolder::GetDisplayNameOf**](https://msdn.microsoft.com/windows/desktop/2164bbe6-e030-4a64-85db-9ee1cd3c136d) to get the value of the name. The PKEY/SCID does not matter.



| Item type     | Example                   |
|---------------|---------------------------|
| File          | hello.txt                 |
| Message       | Re: Where is the meeting? |
| Device folder | song.wma                  |
| Folder        | Documents                 |



 

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

 

 



