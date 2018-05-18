---
Description: 'The user-friendly display path to the item.'
ms.assetid: '5dd44e13-bc5c-4e32-b5eb-2c7c40e10dfb'
title: 'System.ItemPathDisplayNarrow'
---

# System.ItemPathDisplayNarrow

The user-friendly display path to the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemPathDisplayNarrow
   shellPKey = PKEY_ItemPathDisplayNarrow
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 8
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

To optimize for a narrow viewing column, the format of the string should be tailored so that the name comes first.

If the item is a file, the property value excludes the file extension, but includes localized names if they are present. If the item is a message, the value includes the [System.ItemNamePrefix](shell.props_System_ItemNamePrefix). To parse an item path, use [System.ItemUrl](shell.props_System_ItemUrl) or [System.ParsingPath](shell.props_System_ParsingPath).

Example values:



| Path                                   | ItemPathDisplayName                 |
|----------------------------------------|-------------------------------------|
| c:\\mydir\\bar\\hello.txt              | hello (c:\\mydir\\bar)              |
| \\\\server\\share\\mydir\\goodnews.doc | goodnews (\\\\server\\share\\mydir) |
| \\\\server\\share\\folder              | folder (\\\\server\\share)          |
| c:\\MyDir\\MyFolder                    | MyFolder (c:\\mydir)                |
| /Mailbox Account/Inbox/'Re: Hello!'    | Re: Hello! (/Mailbox Account/Inbox) |



 

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

 

 



