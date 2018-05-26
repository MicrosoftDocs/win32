---
Description: The shutter speed of the camera when the photo was taken. This is given in APEX units.
ms.assetid: 7f51b3b9-d701-4e7a-80bd-87c1a60e56f7
title: System.Photo.ShutterSpeed
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.ShutterSpeed

The shutter speed of the camera when the photo was taken. This is given in APEX units. This property is calculated from [System.Photo.ShutterSpeedNumerator](shell.props_System_Photo_ShutterSpeedNumerator) and [System.Photo.ShutterSpeedDenominator](shell.props_System_Photo_ShutterSpeedDenominator).

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.ShutterSpeed
   shellPKey = PKEY_Photo_ShutterSpeed
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 37377
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Double
      IsInnate = true
```

## Windows Vista

```
propertyDescription
   name = System.Photo.ShutterSpeed
   shellPKey = PKEY_Photo_ShutterSpeed
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 37377
   SearchInfo
      IsColumn = true
   typeInfo
      type = Double
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

See the Exchangeable Image File (EXIF) 2.2 specification, Annex C, for the conversion of this value to exposure time. Use [System.Photo.ExposureTime](shell.props_System_Photo_ExposureTime) in any Shell views instead of [System.Photo.ShutterSpeed](shell.props_System_Photo_ShutterSpeed).

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

 

 



