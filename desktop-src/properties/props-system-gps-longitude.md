---
Description: 'Indicates the longitude.'
ms.assetid: 'ef28141f-1b63-4694-b6df-fcc11ce7e50b'
title: 'System.GPS.Longitude'
---

# System.GPS.Longitude

Indicates the longitude. This is an array of three values, as follows: Index 0 is the degrees, index 1 is the minutes, index 2 is the seconds. Each is calculated from the values in PKEY\_GPS\_LongitudeNumerator and PKEY\_GPS\_LongitudeDenominator.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.GPS.Longitude
   shellPKey = PKEY_GPS_Longitude
   formatID = C4C4DBB2-B593-466B-BBDA-D03D27D5E43A
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Multivalue Double
      IsInnate = true
```

## Windows 7, Windows Vista

```
propertyDescription
   name = System.GPS.Longitude
   shellPKey = PKEY_GPS_Longitude
   formatID = C4C4DBB2-B593-466B-BBDA-D03D27D5E43A
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Multivalue Double
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

The requirement of a specific indirect string reference for the `label` attribute of **labelInfo** was added for Windows Vista with Service Pack 1 (SP1).

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

 

 



