---
description: The canonical type of the item.
ms.assetid: 530ba98a-09fd-438b-8872-9eee47f0cf54
title: System.ItemType
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemType

The canonical type of the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemType
   shellPKey = PKEY_ItemType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 11
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

The value for System.ItemType is intended to be programmatically parsed, and can be either:

-   A file extension that points to a ProgID value (HKEY\_CLASSES\_ROOT\\<ProgID>) holding the display name for the type.
-   A ProgID value (HKEY\_CLASSES\_RROOT\\<ProgID>), containing the display name for the type.

The FriendlyTypeName element of a ProgID should be a localized version of the application name (@winword.dll,-42), while the default value of the ProgID key is a non-localized name (Word.Document.12).

If there is no canonical type, the value is VT\_EMPTY. If the item is a file ([System.FileName](./props-system-filename.md) is not VT\_EMPTY), the value is the same as [System.FileExtension](./props-system-fileextension.md). Use [System.ItemTypeText](./props-system-itemtypetext.md) when you want to display the type to end users in a view.

> [!Note]  
> If the item is a file, passing the [System.ItemType]() value to [**PSFormatForDisplay**](/windows/win32/api/propsys/nf-propsys-psformatfordisplay) results in the same value as [System.ItemTypeText](./props-system-itemtypetext.md).

 

Example values:



| Path                                   | ItemType         |
|----------------------------------------|------------------|
| c:\\mydir\\bar\\hello.txt              | .txt             |
| \\\\server\\share\\mydir\\goodnews.doc | .doc             |
| \\\\server\\share\\folder              | Directory        |
| c:\\MyDir\\MyFolder                    | Directory        |
| \[desktop\]                            | Folder           |
| /Mailbox Account/Inbox/'Re: Hello!'    | MAPI/IPM.Message |



 

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
</dt> <dt>

[Programmatic Identifiers](../shell/fa-progids.md)
</dt> </dl>

 

 
