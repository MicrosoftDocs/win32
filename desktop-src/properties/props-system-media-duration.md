---
description: Represents the actual play time of a media file and is measured in 100ns units, not milliseconds.
ms.assetid: 5548f421-6475-4419-b677-5d9eb625a373
title: System.Media.Duration
ms.topic: article
ms.date: 05/31/2018
---

# System.Media.Duration

Represents the actual play time of a media file and is measured in 100ns units, not milliseconds.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Media.Duration
   shellPKey = PKEY_Media_Duration
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 3
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = VeryShort
            minValue = 0
            setValue = 0
            text = Very Short (under 1 min)
            defineToken = MEDIA_DURATION_VERYSHORT
            mnemonics = Very Short
         enumRange
            name = Short
            minValue = 600000000
            setValue = 600000000
            text = Short (1 - 5 mins)
            defineToken = MEDIA_DURATION_SHORT
            mnemonics = Short
         enumRange
            name = Medium
            minValue = 3000000000
            setValue = 3000000000
            text = Medium (5 - 30 mins)
            defineToken = MEDIA_DURATION_MEDIUM
            mnemonics = Medium
         enumRange
            name = Long
            minValue = 18000000000
            setValue = 18000000000
            text = Long (30 - 60 mins)
            defineToken = MEDIA_DURATION_LONG
            mnemonics = Long
         enumRange
            name = VeryLong
            minValue = 36000000000
            setValue = 36000000000
            text = Very Long (over 60 mins)
            defineToken = MEDIA_DURATION_VERYLONG
            mnemonics = Very Long
```

## Windows Vista

```
propertyDescription
   name = System.Media.Duration
   shellPKey = PKEY_Media_Duration
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 3
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = Very Short (under 1 min)
         enumRange
            minValue = 600000000
            setValue = 600000000
            text = Short (1 - 5 mins)
         enumRange
            minValue = 3000000000
            setValue = 3000000000
            text = Medium (5 - 30 mins
         enumRange
            minValue = 18000000000
            setValue = 18000000000
            text = Long (30 - 60 mins)
         enumRange
            minValue = 36000000000
            setValue = 36000000000
            text = Very Long (over 60 mins)
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

 

 
