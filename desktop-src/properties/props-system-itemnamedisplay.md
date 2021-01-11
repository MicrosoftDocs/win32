---
description: The display name in &\#0034;most complete&\#0034; form.
ms.assetid: fdb6b0fa-0741-4edc-8902-763a461313b9
title: System.ItemNameDisplay
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

This value is the concatentation of [System.ItemNamePrefix](./props-system-itemnameprefix.md) and [System.ItemName](./props-system-itemname.md).

If the item is a file, this property includes the display name as shown in File Explorer. There are acceptable cases when [System.FileName](./props-system-filename.md) is given but the value of this property is completely different. E-mail messages are a good example. If the item is an e-mail message, the item name is normally the subject. In that case, the value must be the concatenation of [System.ItemNamePrefix](./props-system-itemnameprefix.md) and [System.ItemName](./props-system-itemname.md). Since the value of System.ItemNamePrefix excludes any trailing spaces, the concatenation must include a space when generating [System.ItemNameDisplay](). Note that this property is not guaranteed to be unique, but is designed to promote the most likely candidate that can be unique and also makes sense to end users.

For example, for documents, the [System.Title](./props-system-title.md) could be used as the [System.ItemNameDisplay](), but in practice the title of the documents may not be useful or unique enough to function as the sole System.ItemNameDisplay. Instead, providing [System.FileName](./props-system-filename.md) as the value of System.ItemNameDisplay is a better choice. In Windows Mail, e-mail is stored in the file system as .eml files. The System.FileName values for those files are not human-friendly as they are GUIDs. In this example, promoting [System.Subject](./props-system-subject.md) as System.ItemNameDisplay makes more sense.

**Compatibility notes:**

-   Shell folder implementations on Windows Vista: use PKEY\_ItemNameDisplay for the name column when you want Windows Explorer to call [**IShellFolder::GetDisplayNameOf**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof)(SHGDN\_NORMAL) to get the value of the name. Use another PKEY, such as PKEY\_ItemName, when you want Windows Explorer to call either the folder's property store or [**IShellFolder2::GetDetailsEx**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder2-getdetailsex) to get the value of the name.
-   Shell folder implementations on Windows XP: the first column must be the name column, and Windows Explorer calls [**IShellFolder::GetDisplayNameOf**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) to get the value of the name. The PKEY/SCID does not matter.



| Item type     | Example                   |
|---------------|---------------------------|
| File          | hello.txt                 |
| Message       | Re: Where is the meeting? |
| Device folder | song.wma                  |
| Folder        | Documents                 |



 

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> </dl>

 

 
