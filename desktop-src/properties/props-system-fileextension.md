---
description: Identifies the file extension of the file-based item, including the leading period.
ms.assetid: b72c695e-bdbd-471d-b902-9e30a62facd4
title: System.FileExtension
ms.topic: article
ms.date: 05/31/2018
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

If [System.FileName](./props-system-filename.md) is VT\_EMPTY, this property should also be empty. Otherwise, this property should be derived appropriately by the data source from System.FileName. If System.FileName does not include a file extension, [System.FileExtension]() should be VT\_EMPTY. To obtain the type of any item (including an item that is not a file), use [System.ItemType](./props-system-itemtype.md).

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

 

 
