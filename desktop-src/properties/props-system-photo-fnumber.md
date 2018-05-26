---
Description: The FNumber value when the photo was taken, as read from the Exchangeable Image File (EXIF) information.
ms.assetid: 914dc34d-34e9-4283-be26-203da945d3e9
title: System.Photo.FNumber
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.FNumber

The FNumber value when the photo was taken, as read from the Exchangeable Image File (EXIF) information.This property is calculated from [System.Photo.FNumberNumerator](shell.props_System_Photo_FNumberNumerator) and [System.Photo.FNumberDenominator](shell.props_System_Photo_FNumberDenominator).

The following are possible values as taken from the EXIF 2.2 specification.

-   1
-   1.4
-   2
-   2.8
-   4
-   5.6
-   8
-   11
-   16
-   22
-   32

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.FNumber
   shellPKey = PKEY_Photo_FNumber
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 33437
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
   name = System.Photo.FNumber
   shellPKey = PKEY_Photo_FNumber
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 33437
   SearchInfo
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

 

 



