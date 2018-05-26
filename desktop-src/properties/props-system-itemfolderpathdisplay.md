---
Description: The user-friendly display path of an items parent folder.
ms.assetid: 16f67edc-ca8a-4c2e-9d9b-be8600446e51
title: System.ItemFolderPathDisplay
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ItemFolderPathDisplay

The user-friendly display path of an item's parent folder.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemFolderPathDisplay
   shellPKey = PKEY_ItemFolderPathDisplay
   formatID = E3E0584C-B788-4A5A-BB20-7F5A44C9ACDD
   propID = 6
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If [System.ItemPathDisplay](shell.props_System_ItemPathDisplay) is VT\_EMPTY, then this property should also be empty. Otherwise, it should be derived appropriately by the data source from System.ItemPathDisplay.

Example values:



| Path                                   | ItemFolderPathDisplay    |
|----------------------------------------|--------------------------|
| c:\\files\\personal\\hello.txt         | c:\\files\\personal      |
| \\\\server\\share\\mydir\\goodnews.doc | \\\\server\\share\\mydir |
| \\\\server\\share\\numbers.xls         | \\\\server\\share        |
| c:\\food\\MyFolder                     | c:\\food                 |
| /Mailbox Account/Inbox/'Re: Hello!'    | /Mailbox Account/Inbox   |



 

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

 

 



