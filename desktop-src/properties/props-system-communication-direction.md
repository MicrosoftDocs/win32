---
Description: Indicates whether a communication was incoming or outgoing.
ms.assetid: b41f185b-f8b3-433b-9aed-8e71d59e4602
title: System.Communication.Direction
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Communication.Direction

Indicates whether a communication was incoming or outgoing

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507

```
propertyDescription
   name = System.Communication.Direction
   shellPKey = PKEY_Communication_Direction
   formatID = 8E531030-B960-4346-AE0D-66BC9A86FB94
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Unknown
            value = 0
            text = Unknown
            defineToken = COMMUNICATION_DIRECTION_UNKNOWN
         enum
            name = Incoming
            value = 1
            text = Incoming
            defineToken = COMMUNICATION_DIRECTION_INCOMING
         enum
            name = Outgoing
            value = 2
            text = Outgoing
            defineToken = COMMUNICATION_DIRECTION_OUTGOING
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

 

 



