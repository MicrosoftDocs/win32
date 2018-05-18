---
Description: 'The amount of total storage space, expressed in bytes.'
ms.assetid: '14cd6b5d-0534-4527-8439-e7ba8cdef8da'
title: 'System.Capacity'
---

# System.Capacity

The amount of total storage space, expressed in bytes. This property is mainly used to indicate the capacity of storage media such as hard drives.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Capacity
   shellPKey = PKEY_Capacity
   formatID = 9B174B35-40FF-11D2-A27E-00C04FC30871
   propID = 3
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = Empty
            minValue = 0
            setValue = 0
            text = 0 GB
            defineToken = CAPACITY_EMPTY
            mnemonics = empty
         enumRange
            name = Tiny
            minValue = 1
            setValue = 1
            text = 0 - 16 GB
            defineToken = CAPACITY_TINY
            mnemonics = tiny
         enumRange
            name = Small
            minValue = 17179869185
            setValue = 17179869185
            text = 16 - 80 GB
            defineToken = CAPACITY_SMALL
            mnemonics = small
         enumRange
            name = Medium
            minValue = 85899345921
            setValue = 85899345921
            text = 80 - 250 GB
            defineToken = CAPACITY_MEDIUM
            mnemonics = medium
         enumRange
            name = Large
            minValue = 274877906945
            setValue = 274877906945
            text = 250 - 500 GB
            defineToken = CAPACITY_LARGE
            mnemonics = large
         enumRange
            name = Huge
            minValue = 549755813889
            setValue = 549755813889
            text = 500 - 1 TB
            defineToken = CAPACITY_HUGE
            mnemonics = huge
         enumRange
            name = Gigantic
            minValue = 1099511627777
            setValue = 1099511627777
            text = >1 TB
            defineToken = CAPACITY_GIGANTIC
            mnemonics = gigantic
```

## Windows Vista

```
propertyDescription
   name = System.Capacity
   shellPKey = PKEY_Capacity
   formatID = 9B174B35-40FF-11D2-A27E-00C04FC30871
   propID = 3
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = 0 GB
            mnemonics = empty
         enumRange
            minValue = 1
            setValue = 1
            text = 0 - 2 GB
            mnemonics = tiny
         enumRange
            minValue = 2147483649
            setValue = 2147483649
            text = 2 - 10 GB
            mnemonics = small
         enumRange
            minValue = 10737418241
            setValue = 10737418241
            text = 10 - 40 GB
            mnemonics = medium
         enumRange
            minValue = 42949672961
            setValue = 42949672961
            text = 40 - 80 GB
            mnemonics = large
         enumRange
            minValue = 85899345921
            setValue = 85899345921
            text = 80 - 120 GB
            mnemonics = huge
         enumRange
            minValue = 137438953473
            setValue = 137438953473
            text = >120 GB
            mnemonics = gigantic
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

 

 



