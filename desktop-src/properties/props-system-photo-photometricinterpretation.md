---
Description: 'The pixel composition.'
ms.assetid: 'e2bb7f82-10dc-4fa0-875d-fc58c133024d'
title: 'System.Photo.PhotometricInterpretation'
---

# System.Photo.PhotometricInterpretation

The pixel composition. In JPEG compressed data, a JPEG marker is used instead of this property.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.PhotometricInterpretation
   shellPKey = PKEY_Photo_PhotometricInterpretation
   formatID = 341796F1-1DF9-4B1C-A564-91BDEFA43877
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt16
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = RGB
            value = 2
            text = RGB
            defineToken = PHOTO_PHOTOMETRIC_RGB
         enum
            name = YCbCr
            value = 6
            text = YCbCr
            defineToken = PHOTO_PHOTOMETRIC_YCBCR
```

## Windows Vista

```
propertyDescription
   name = System.Photo.PhotometricInterpretation
   shellPKey = PKEY_Photo_PhotometricInterpretation
   formatID = 341796F1-1DF9-4B1C-A564-91BDEFA43877
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt16
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 2
            text = RGB
            defineName = PHOTO_PHOTOMETRIC_RGB
         enum
            value = 6
            text = YCbCr
            defineName = PHOTO_PHOTOMETRIC_YCBCR
```

## Remarks

PKEY values are defined in Propkey.h.

The default value of the `isInnate` attribute of the **typeInfo** element was changed from **false** to **true** as of Windows Vista with Service Pack 1 (SP1).

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

 

 



