---
Description: Identifies the file extension of the file-based item, including the leading period.
ms.assetid: b72c695e-bdbd-471d-b902-9e30a62facd4
title: System.FileExtension
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

If [System.FileName](shell.props_System_FileName) is VT\_EMPTY, this property should also be empty. Otherwise, this property should be derived appropriately by the data source from System.FileName. If System.FileName does not include a file extension, [System.FileExtension](shell.props_System_FileExtension) should be VT\_EMPTY. To obtain the type of any item (including an item that is not a file), use [System.ItemType](shell.props_System_ItemType).

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

 

 



