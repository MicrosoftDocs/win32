---
description: The user-friendly type name of the item.
ms.assetid: 5d4c86da-6317-4a34-88d6-caf794aaa165
title: System.ItemTypeText
ms.topic: article
ms.date: 05/31/2018
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

If [System.ItemType](./props-system-itemtype.md) is VT\_EMPTY, the value of this property is also VT\_EMPTY. If the item is a file, the value of this property is the same as if you passed the file's System.ItemType value to [**PSFormatForDisplay**](/windows/win32/api/propsys/nf-propsys-psformatfordisplay).

This property should not be confused with [System.Kind](./props-system-kind.md), which is a high-level, user-friendly kind name. For example, for a .doc document file, the various properties are as shown here:



| Property                                               | Value                   |
|--------------------------------------------------------|-------------------------|
| [System.Kind](./props-system-kind.md)                 | Document                |
| [System.ItemType](./props-system-itemtype.md)         | .doc                    |
| [System.ItemTypeText]() | Microsoft Word Document |



 

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

 

 
