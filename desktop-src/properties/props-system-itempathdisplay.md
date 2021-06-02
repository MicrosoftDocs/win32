---
description: The user-friendly display path to the item.
ms.assetid: 27e4490b-7914-4b38-9799-e9d5dc407f13
title: System.ItemPathDisplay
ms.topic: article
ms.date: 05/31/2018
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

Unlike [System.ItemUrl](./props-system-itemurl.md), this property value does not include the URL scheme. To parse an item path, use System.ItemUrl or [System.ParsingPath](./props-system-parsingpath.md). To reference Shell namespace items using Shell APIs, use System.ParsingPath.

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

 

 
