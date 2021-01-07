---
description: The user-friendly display name of an item's parent folder.
ms.assetid: 4049b6cb-41a1-4df6-89d1-a2022d3a285d
title: System.ItemFolderNameDisplay
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemFolderNameDisplay

The user-friendly display name of an item's parent folder.

This is derived from [System.ItemFolderPathDisplay](./props-system-itemfolderpathdisplay.md). If that property is VT\_EMPTY, then this property should be too.

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

If [System.ItemFolderPathDisplay](./props-system-itemfolderpathdisplay.md) is VT\_EMPTY, then this property should also be empty. Otherwise, it should be derived appropriately by the data source from System.ItemFolderPathDisplay.

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

 

 
