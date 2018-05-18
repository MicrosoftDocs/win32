---
Description: 'The user-friendly display path to the item.'
ms.assetid: '27e4490b-7914-4b38-9799-e9d5dc407f13'
title: 'System.ItemPathDisplay'
---

# System.ItemPathDisplay

The user-friendly display path to the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemPathDisplay
   shellPKey = PKEY_ItemPathDisplay
   formatID = E3E0584C-B788-4A5A-BB20-7F5A44C9ACDD
   propID = 7
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If the item is a file or folder, this property includes the extension in all cases, and is localized if a localized name is available. For other items, this is the user-friendly equivalent, assuming that the item exists in hierarchical storage.

Unlike [System.ItemUrl](shell.props_System_ItemUrl), this property value does not include the URL scheme. To parse an item path, use System.ItemUrl or [System.ParsingPath](shell.props_System_ParsingPath). To reference Shell namespace items using Shell APIs, use System.ParsingPath.

Example values:



| Path                                   | ItemPathDisplay                        |
|----------------------------------------|----------------------------------------|
| c:\\mydir\\bar\\hello.txt              | c:\\mydir\\bar\\hello.txt              |
| \\\\server\\share\\mydir\\goodnews.doc | \\\\server\\share\\mydir\\goodnews.doc |
| \\\\server\\share\\numbers.xls         | \\\\server\\share\\numbers.xls         |
| c:\\mydir\\MyFolder                    | c:\\mydir\\MyFolder                    |
| /Mailbox Account/Inbox/'Re: Hello!'    | /Mailbox Account/Inbox/'Re: Hello!'    |



 

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

 

 



