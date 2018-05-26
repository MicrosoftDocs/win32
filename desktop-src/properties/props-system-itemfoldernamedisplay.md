---
Description: The user-friendly display name of an items parent folder.
ms.assetid: 4049b6cb-41a1-4df6-89d1-a2022d3a285d
title: System.ItemFolderNameDisplay
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ItemFolderNameDisplay

The user-friendly display name of an item's parent folder.

This is derived from [System.ItemFolderPathDisplay](shell.props_System_ItemFolderPathDisplay). If that property is VT\_EMPTY, then this property should be too.

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

If [System.ItemFolderPathDisplay](shell.props_System_ItemFolderPathDisplay) is VT\_EMPTY, then this property should also be empty. Otherwise, it should be derived appropriately by the data source from System.ItemFolderPathDisplay.

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

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> </dl>

 

 



