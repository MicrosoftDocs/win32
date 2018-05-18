---
Description: 'The user-friendly type name of the item.'
ms.assetid: '5d4c86da-6317-4a34-88d6-caf794aaa165'
title: 'System.ItemTypeText'
---

# System.ItemTypeText

The user-friendly type name of the item. This value is not intended to be programmatically parsed.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemTypeText
   shellPKey = PKEY_ItemTypeText
   formatID = B725F130-47EF-101A-A5F1-02608C9EEBAC
   propID = 4
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If [System.ItemType](shell.props_System_ItemType) is VT\_EMPTY, the value of this property is also VT\_EMPTY. If the item is a file, the value of this property is the same as if you passed the file's System.ItemType value to [**PSFormatForDisplay**](shell.PSFormatForDisplay).

This property should not be confused with [System.Kind](shell.props_System_Kind), which is a high-level, user-friendly kind name. For example, for a .doc document file, the various properties are as shown here:



| Property                                               | Value                   |
|--------------------------------------------------------|-------------------------|
| [System.Kind](shell.props_System_Kind)                 | Document                |
| [System.ItemType](shell.props_System_ItemType)         | .doc                    |
| [System.ItemTypeText](shell.props_System_ItemTypeText) | Microsoft Word Document |



 

Example values:



| Path                                   | ItemTypeText            |
|----------------------------------------|-------------------------|
| c:\\mydir\\bar\\hello.txt              | Text File               |
| \\\\server\\share\\mydir\\goodnews.doc | Microsoft Word Document |
| \\\\server\\share\\folder              | File Folder             |
| c:\\MyDir\\MyFolder                    | File Folder             |
| /Mailbox Account/Inbox/'Re: Hello!'    | Outlook E-Mail Message  |



 

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

 

 



