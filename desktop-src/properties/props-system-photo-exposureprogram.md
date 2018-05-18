---
Description: 'The Exposure Program mode of the camera at the time the photo was taken, as read from the Exchangeable Image File (EXIF) information.'
ms.assetid: 'd27003b4-f30a-4c48-b32f-933b2f29182a'
title: 'System.Photo.ExposureProgram'
---

# System.Photo.ExposureProgram

The Exposure Program mode of the camera at the time the photo was taken, as read from the Exchangeable Image File (EXIF) information.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.ExposureProgram
   shellPKey = PKEY_Photo_ExposureProgram
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 34850
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Unknown
            value = 0
            text = Unknown
            defineToken = PHOTO_EXPOSUREPROGRAM_UNKNOWN
         enum
            name = Manual
            value = 1
            text = Manual
            defineToken = PHOTO_EXPOSUREPROGRAM_MANUAL
         enum
            name = Normal
            value = 2
            text = Normal
            defineToken = PHOTO_EXPOSUREPROGRAM_NORMAL
         enum
            name = Aperture
            value = 3
            text = Aperture Priority
            defineToken = PHOTO_EXPOSUREPROGRAM_APERTURE
         enum
            name = Shutter
            value = 4
            text = Shutter Priority
            defineToken = PHOTO_EXPOSUREPROGRAM_SHUTTER
         enum
            name = Creative
            value = 5
            text = Creative Program (biased toward depth of field)
            defineToken = PHOTO_EXPOSUREPROGRAM_CREATIVE
         enum
            name = Action
            value = 6
            text = Action Program (biased toward shutter speed)
            defineToken = PHOTO_EXPOSUREPROGRAM_ACTION
         enum
            name = Portrait
            value = 7
            text = Portrait Mode
            defineToken = PHOTO_EXPOSUREPROGRAM_PORTRAIT
         enum
            name = Landscape
            value = 8
            text = Landscape Mode
            defineToken = PHOTO_EXPOSUREPROGRAM_LANDSCAPE
```

## Windows Vista

```
propertyDescription
   name = System.Photo.ExposureProgram
   shellPKey = PKEY_Photo_ExposureProgram
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 34850
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Unknown
            defineName = PHOTO_EXPOSUREPROGRAM_UNKNOWN
         enum
            value = 1
            text = Manual
            defineName = PHOTO_EXPOSUREPROGRAM_MANUAL
         enum
            value = 2
            text = Normal
            defineName = PHOTO_EXPOSUREPROGRAM_NORMAL
         enum
            value = 3
            text = Aperture Priority
            defineName = PHOTO_EXPOSUREPROGRAM_APERTURE
         enum
            value = 4
            text = Shutter Priority
            defineName = PHOTO_EXPOSUREPROGRAM_SHUTTER
         enum
            value = 5
            text = Creative Program (biased toward depth of field)
            defineName = PHOTO_EXPOSUREPROGRAM_CREATIVE
         enum
            value = 6
            text = Action Program (biased toward shutter speed)
            defineName = PHOTO_EXPOSUREPROGRAM_ACTION
         enum
            value = 7
            text = Portrait Mode
            defineName = PHOTO_EXPOSUREPROGRAM_PORTRAIT
         enum
            value = 8
            text = Landscape Mode
            defineName = PHOTO_EXPOSUREPROGRAM_LANDSCAPE
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

 

 



