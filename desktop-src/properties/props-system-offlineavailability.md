---
Description: .
ms.assetid: 4d0c880b-923d-4f83-91da-dd99bf111f13
title: System.OfflineAvailability
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.OfflineAvailability

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.OfflineAvailability
   shellPKey = PKEY_OfflineAvailability
   formatID = A94688B6-7D9F-4570-A648-E3DFC0AB2B3F
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotAvailable
            value = 0
            text = Online-only
            defineToken = OFFLINEAVAILABILITY_NOT_AVAILABLE
         enum
            name = Available
            value = 1
            text = Available
            defineToken = OFFLINEAVAILABILITY_AVAILABLE
         enum
            name = AlwaysAvailable
            value = 2
            text = Available offline
            defineToken = OFFLINEAVAILABILITY_ALWAYS_AVAILABLE
```

## Windows 8, Windows 7

```
propertyDescription
   name = System.OfflineAvailability
   shellPKey = PKEY_OfflineAvailability
   formatID = A94688B6-7D9F-4570-A648-E3DFC0AB2B3F
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotAvailable
            value = 0
            text = Not available
            defineToken = OFFLINEAVAILABILITY_NOT_AVAILABLE
         enum
            name = Available
            value = 1
            text = Available
            defineToken = OFFLINEAVAILABILITY_AVAILABLE
         enum
            name = AlwaysAvailable
            value = 2
            text = Always available
            defineToken = OFFLINEAVAILABILITY_ALWAYS_AVAILABLE
```

## Windows Vista

```
propertyDescription
   name = System.OfflineAvailability
   shellPKey = PKEY_OfflineAvailability
   formatID = A94688B6-7D9F-4570-A648-E3DFC0AB2B3F
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Not available
            defineName = OFFLINEAVAILABILITY_NOT_AVAILABLE
         enum
            value = 1
            text = Available
            defineName = OFFLINEAVAILABILITY_AVAILABLE
         enum
            value = 2
            text = Always available
            defineName = OFFLINEAVAILABILITY_ALWAYS_AVAILABLE
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

 

 



