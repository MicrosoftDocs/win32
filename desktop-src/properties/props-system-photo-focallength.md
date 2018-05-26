---
Description: The focal length of the lens as recorded by the camera when the photo was taken, measured in millimeters.
ms.assetid: 1839485d-c933-4ca9-a45a-d44cbd29f9b5
title: System.Photo.FocalLength
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.FocalLength

The focal length of the lens as recorded by the camera when the photo was taken, measured in millimeters. This is the actual focal length without conversion to 35mm ([System.Photo.FocalLengthInFilm](shell.props_System_Photo_FocalLengthInFilm)). This property is calculated from [System.Photo.FocalLengthNumerator](shell.props_System_Photo_FocalLengthNumerator) and [System.Photo.FocalLengthDenominator](shell.props_System_Photo_FocalLengthDenominator).

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Photo.FocalLength
   shellPKey = PKEY_Photo_FocalLength
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 37386
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

 

 



