---
Description: Helps display as an icon whether or not a location is the default save location for owner and/or non-owners of a library.
ms.assetid: 42375796-bf95-4092-bce0-c77e7b5bfeea
title: System.DefaultSaveLocationDisplay
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.DefaultSaveLocationDisplay

Helps display as an icon whether or not a location is the default save location for owner and/or non-owners of a library

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.DefaultSaveLocationDisplay
   shellPKey = PKEY_DefaultSaveLocationDisplay
   formatID = 5D76B67F-9B3D-44BB-B6AE-25DA4F638A67
   propID = 10
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            name = DefaultSaveNone
            value = 0
            text
            defineToken = ISDEFAULTSAVE_NONE
         enum
            name = DefaultSaveOwner
            value = 1
            text = Default save location
            defineToken = ISDEFAULTSAVE_OWNER
         enum
            name = DefaultSavePublic
            value = 2
            text = Public save location
            defineToken = ISDEFAULTSAVE_NONOWNER
         enum
            name = DefaultSaveBoth
            value = 3
            text = Default and public save location
            defineToken = ISDEFAULTSAVE_BOTH
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

 

 



