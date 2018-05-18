---
Description: 'The exposure time for the photo, in seconds, as read from the Exchangeable Image File (EXIF) information.'
ms.assetid: '44f7e6d5-c4d9-4b41-b6c6-15145abb7983'
title: 'System.Photo.ExposureTime'
---

# System.Photo.ExposureTime

The exposure time for the photo, in seconds, as read from the Exchangeable Image File (EXIF) information. This property is calculated from [System.Photo.ExposureTimeNumerator](shell.props_System_Photo_ExposureTimeNumerator) and [System.Photo.ExposureTimeDenominator](shell.props_System_Photo_ExposureTimeDenominator).

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

[Exchangeable Image File Format for Digital Still Cameras: Exif Version 2.2](http://www.exif.org/Exif2-2.PDF)
</dt> <dt>

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

 

 



