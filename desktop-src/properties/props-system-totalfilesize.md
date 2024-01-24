---
description: System.TotalFileSize
ms.assetid: 10e1f806-e408-48ab-8fe7-1d7a4d41f320
title: System.TotalFileSize
ms.topic: article
ms.date: 05/31/2018
---

# System.TotalFileSize

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.TotalFileSize
   shellPKey = PKEY_TotalFileSize
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 14
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = Empty
            minValue = 0
            setValue = 0
            text = Zero
            defineToken = TOTALFILESIZE_EMPTY
            mnemonics = empty
         enumRange
            name = Tiny
            minValue = 1
            setValue = 1
            text = Tiny (0 - 10 KB)
            defineToken = TOTALFILESIZE_TINY
            mnemonics = tiny
         enumRange
            name = Small
            minValue = 10241
            setValue = 10241
            text = Small (10 - 100 KB)
            defineToken = TOTALFILESIZE_SMALL
            mnemonics = small
         enumRange
            name = Medium
            minValue = 102401
            setValue = 102401
            text = Medium (100 KB - 1 MB)
            defineToken = TOTALFILESIZE_MEDIUM
            mnemonics = medium
         enumRange
            name = Large
            minValue = 1048577
            setValue = 1048577
            text = Large (1 - 16 MB)
            defineToken = TOTALFILESIZE_LARGE
            mnemonics = large
         enumRange
            name = Huge
            minValue = 16777217
            setValue = 16777217
            text = Huge (16 - 128 MB)
            defineToken = TOTALFILESIZE_HUGE
            mnemonics = huge
         enumRange
            name = Gigantic
            minValue = 134217729
            setValue = 134217729
            text = Gigantic (>129 MB)
            defineToken = TOTALFILESIZE_GIGANTIC
            mnemonics = gigantic
```

## Windows Vista

```
propertyDescription
   name = System.TotalFileSize
   shellPKey = PKEY_TotalFileSize
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 14
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = Zero
            mnemonics = empty
         enumRange
            minValue = 1
            setValue = 1
            text = Tiny (0 - 10 KB)
            mnemonics = tiny
         enumRange
            minValue = 10241
            setValue = 10241
            text = Small (10 - 100 KB)
            mnemonics = small
         enumRange
            minValue = 102401
            setValue = 102401
            text = Medium (100 KB - 1 MB)
            mnemonics = medium
         enumRange
            minValue = 1048577
            setValue = 1048577
            text = Large (1 - 16 MB)
            mnemonics = large
         enumRange
            minValue = 16777217
            setValue = 16777217
            text = Huge (16 - 128 MB)
            mnemonics = huge
         enumRange
            minValue = 134217729
            setValue = 134217729
            text = Gigantic (>129 MB)
            mnemonics = gigantic
```

## Remarks

PKEY values are defined in Propkey.h.

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

 

 
