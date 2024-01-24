---
description: A rating system that uses a range of integer values between 0 and 5.
ms.assetid: 50353ba9-86dd-4172-91b4-1898c8fc5522
title: System.SimpleRating
ms.topic: article
ms.date: 05/31/2018
---

# System.SimpleRating

A rating system that uses a range of integer values between 0 and 5.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.SimpleRating
   shellPKey = PKEY_SimpleRating
   formatID = A09F084E-AD41-489F-8076-AA5BE3082BCA
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

For compatibility with the Windows Vista Shell rating system, your property handler should also populate the [System.Rating](./props-system-rating.md) property with the mapping as described for that property.

Use the following table to convert from [System.Rating](./props-system-rating.md) to [System.SimpleRating]().



| System.Rating | System.SimpleRating |
|---------------|---------------------|
| 0             | 0                   |
| 1-12          | 1                   |
| 13-37         | 2                   |
| 38-62         | 3                   |
| 63-87         | 4                   |
| 88-99         | 5                   |



 

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

 

 
