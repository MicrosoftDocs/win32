---
Description: 'Total free storage space on the device, as a percentage.'
ms.assetid: 'ede845c6-abd8-4bb1-b0d8-c1f3facffa41'
title: 'System.Devices.StorageFreeSpacePercent'
---

# System.Devices.StorageFreeSpacePercent

Total free storage space on the device, as a percentage.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Devices.StorageFreeSpacePercent
   shellPKey = PKEY_Devices_StorageFreeSpacePercent
   formatID = 49CD1F76-5626-4B17-A4E8-18B4AA1A2213
   propID = 14
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = StorageSpaceFull
            minValue = 0
            setValue = 0
            text = Storage space full
            defineToken = STORAGESPACE_FULL
         enumRange
            name = 5PercentFree
            minValue = 5
            setValue = 5
            text = 5% free space
            defineToken = STORAGESPACE_5_PERCENT
         enumRange
            name = 10PercentFree
            minValue = 10
            setValue = 10
            text = 10% free space
            defineToken = STORAGESPACE_10_PERCENT
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

 

 



