---
Description: Indicates the direction of sharpness processing applied by the camera when the photo was taken.
ms.assetid: ee3dca97-a094-4de8-aacd-729abcef4965
title: System.Photo.Sharpness
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.Sharpness

Indicates the direction of sharpness processing applied by the camera when the photo was taken.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.Sharpness
   shellPKey = PKEY_Photo_Sharpness
   formatID = FC6976DB-8349-4970-AE97-B3C5316A08F0
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Normal
            value = 0
            text = Normal
            defineToken = PHOTO_SHARPNESS_NORMAL
         enum
            name = Soft
            value = 1
            text = Soft
            defineToken = PHOTO_SHARPNESS_SOFT
         enum
            name = Hard
            value = 2
            text = Hard
            defineToken = PHOTO_SHARPNESS_HARD
```

## Windows Vista

```
propertyDescription
   name = System.Photo.Sharpness
   shellPKey = PKEY_Photo_Sharpness
   formatID = FC6976DB-8349-4970-AE97-B3C5316A08F0
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Normal
            defineName = PHOTO_SHARPNESS_NORMAL
         enum
            value = 1
            text = Soft
            defineName = PHOTO_SHARPNESS_SOFT
         enum
            value = 2
            text = Hard
            defineName = PHOTO_SHARPNESS_HARD
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

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

 

 



