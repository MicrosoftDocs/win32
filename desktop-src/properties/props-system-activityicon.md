---
description: The string corresponding to a glyph in the Segoe Fluent Icons font that represents the activity described in System.ActivityInfo.
ms.assetid: 9c4e7a2b-f1d8-4e3c-a9b7-6f2e8d4c1a5e
title: System.ActivityIcon
ms.topic: reference
ms.date: 07/25/2025
---

# System.ActivityIcon

The string corresponding to a glyph in the Segoe Fluent Icons font that represents the activity described in [System.ActivityInfo](./props-system-activityinfo.md).

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.ActivityIcon
   shellPKey = PKEY_ActivityIcon
   formatID = 30C8EEF4-A832-41E2-AB32-E3C3CA28FD29
   propID = 24
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
      IsInnate = false
```

## Remarks

PKEY values are defined in Propkey.h.

For example, "\xE70F" for a file that was recently edited, or "\xE716" for a file that was recently shared.

If [System.ActivityInfo](./props-system-activityinfo.md) is VT_EMPTY, then this property should be too.

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
