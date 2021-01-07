---
description: The exposure time for the photo, in seconds, as read from the Exchangeable Image File (EXIF) information.
ms.assetid: 44f7e6d5-c4d9-4b41-b6c6-15145abb7983
title: System.Photo.ExposureTime
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.ExposureTime

The exposure time for the photo, in seconds, as read from the Exchangeable Image File (EXIF) information. This property is calculated from [System.Photo.ExposureTimeNumerator](./props-system-photo-exposuretimenumerator.md) and [System.Photo.ExposureTimeDenominator](./props-system-photo-exposuretimedenominator.md).

The following is a list of possible values taken from the EXIF 2.2 specification.

-   30
-   15
-   8
-   4
-   2
-   1
-   1/2
-   1/4
-   1/8
-   1/15
-   1/30
-   1/60
-   1/125
-   1/250
-   1/500
-   1/1000
-   1/2000

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Photo.ExposureTime
   shellPKey = PKEY_Photo_ExposureTime
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 33434
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Double
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Exchangeable Image File Format for Digital Still Cameras: Exif Version 2.2](https://www.exif.org/Exif2-2.PDF)
</dt> <dt>

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

 

 
