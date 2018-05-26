---
Description: Identifies the default save location for a library for non-owners of the library.
ms.assetid: e6fe96de-4895-477e-a442-746fd34a7433
title: System.IsDefaultNonOwnerSaveLocation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.IsDefaultNonOwnerSaveLocation

Identifies the default save location for a library for non-owners of the library.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.IsDefaultNonOwnerSaveLocation
   shellPKey = PKEY_IsDefaultNonOwnerSaveLocation
   formatID = 5D76B67F-9B3D-44BB-B6AE-25DA4F638A67
   propID = 5
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
      EnumeratedList
         UseValueForDefault = True
         enum
            name = DefaultPublicSave
            value = #TRUE#
            text = Public save location
            defineToken = ISDEFAULTPUBLICSAVE_YES
         enum
            name = NotDefaultPublicSave
            value = #FALSE#
            text
            defineToken = ISDEFAULTPUBLICSAVE_NO
```

## Windows 7

```
propertyDescription
   name = System.IsDefaultNonOwnerSaveLocation
   shellPKey = PKEY_IsDefaultNonOwnerSaveLocation
   formatID = 5D76B67F-9B3D-44BB-B6AE-25DA4F638A67
   propID = 5
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
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

 

 



