---
Description: .
ms.assetid: 43f81cb5-7f2e-4f8f-ad31-8aad71765f60
title: System.Priority
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Priority

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Priority
   shellPKey = PKEY_Priority
   formatID = 9C1FCF74-2D97-41BA-B4AE-CB2E3661A6E4
   propID = 5
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Low
            value = 0
            text = Low
            defineToken = PRIORITY_PROP_LOW
         enum
            name = Normal
            value = 1
            text = Normal
            defineToken = PRIORITY_PROP_NORMAL
         enum
            name = High
            value = 2
            text = High
            defineToken = PRIORITY_PROP_HIGH
```

## Windows Vista

```
propertyDescription
   name = System.Priority
   shellPKey = PKEY_Priority
   formatID = 9C1FCF74-2D97-41BA-B4AE-CB2E3661A6E4
   propID = 5
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Low
            defineName = PRIORITY_PROP_LOW
         enum
            value = 1
            text = Normal
            defineName = PRIORITY_PROP_NORMAL
         enum
            value = 2
            text = High
            defineName = PRIORITY_PROP_HIGH
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

 

 



