---
Description: The brightness value of the image, in APEX units, usually in the range of -99.99 to 99.99.
ms.assetid: 533f6934-dec8-455a-937c-d4e144be4335
title: System.Photo.Brightness
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.Brightness

The brightness value of the image, in APEX units, usually in the range of -99.99 to 99.99.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Photo.Brightness
   shellPKey = PKEY_Photo_Brightness
   formatID = 1A701BF6-478C-4361-83AB-3701BB053C58
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Double
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

See the EXIF 2.2 specification, Annex C, for a comparison of [System.Photo.Brightness](shell.props_System_Photo_Brightness) numbers and Foot-Lambert measurements. This property is calculated from [System.Photo.BrightnessNumerator](shell.props_System_Photo_BrightnessNumerator) and [System.Photo.BrightnessDenominator](shell.props_System_Photo_BrightnessDenominator). If the numerator of the recorded value is FFFFFFFF.H, "Unknown" should be indicated.

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

 

 



