---
Description: The file name, including its extension.
ms.assetid: 40940026-6c67-4196-aff6-5f846dc94f27
title: System.FileName
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.FileName

The file name, including its extension. System.FileExtension is derived from this property.

It is possible that the item might not exist on a filesystem (that is, it may not be opened using CreateFile). Nonetheless, if the item is represented as a file and its name follows standard Win32 file-naming syntax, then the data source should emit this property. If the item is not a file, then the data source should emit this property as VT\_EMPTY.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.FileName
   shellPKey = PKEY_FileName
   formatID = 41CF5AE0-F75A-4806-BD87-59C7D9248EB9
   propID = 100
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Windows Vista

```
propertyDescription
   name = System.FileName
   shellPKey = PKEY_FileName
   formatID = 41CF5AE0-F75A-4806-BD87-59C7D9248EB9
   propID = 100
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = 0-9
         enumRange
            minValue = A
            setValue = A
            text = A-H
         enumRange
            minValue = I
            setValue = I
            text = I-P
         enumRange
            minValue = Q
            setValue = Q
            text = Q-Z
```

## Remarks

PKEY values are defined in Propkey.h.

The item might not exist on a filesystem (that is, it may not be opened using CreateFile), but if the item is represented as a file from the logical sense and its name follows standard Win32 file-naming syntax, then the data source should emit this property. If an item is not a file, then the value for this property is VT\_EMPTY. See System.ItemNameDisplay. This has the same value as System.ParsingName for items that are provided by the Shell's file folder.

The following table lists examples of path and filename property values:



| Path                               | Property Value |
|------------------------------------|----------------|
| c:\\files\\personal\\hello.txt     | hello.txt      |
| \\\\server\\share\\mydir\\news.doc | news.doc       |
| \\\\server\\share\\numbers.xls     | numbers.xls    |
| c:\\Stuff\\MyFolder                | MyFolder       |
| \[email message\]                  | VT\_EMPTY      |
| \[song.wma on portable device\]    | song.wma       |



 

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

 

 



