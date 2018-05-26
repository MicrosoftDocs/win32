---
Description: Indicates the status of the attendee during the event. User can choose to set the status as free, busy, tentative or out of office.
ms.assetid: ce2a1ab8-2937-446e-ac84-313649a4134d
title: System.Calendar.ShowTimeAs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Calendar.ShowTimeAs

Indicates the status of the attendee during the event. User can choose to set the status as free, busy, tentative or out of office.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Calendar.ShowTimeAs
   shellPKey = PKEY_Calendar_ShowTimeAs
   formatID = 5BF396D4-5EB2-466F-BDE9-2FB3F2361D6E
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Free
            value = 0
            text = Free
            defineToken = CALENDAR_SHOWTIMEAS_FREE
         enum
            name = Tentative
            value = 1
            text = Tentative
            defineToken = CALENDAR_SHOWTIMEAS_TENTATIVE
         enum
            name = Busy
            value = 2
            text = Busy
            defineToken = CALENDAR_SHOWTIMEAS_BUSY
         enum
            name = OOF
            value = 3
            text = OOF
            defineToken = CALENDAR_SHOWTIMEAS_OOF
            mnemonics = Out of Office
```

## Windows Vista

```
propertyDescription
   name = System.Calendar.ShowTimeAs
   shellPKey = PKEY_Calendar_ShowTimeAs
   formatID = 5BF396D4-5EB2-466F-BDE9-2FB3F2361D6E
   propID = 100
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Free
            defineName = CALENDAR_SHOWTIMEAS_FREE
         enum
            value = 1
            text = Tentative
            defineName = CALENDAR_SHOWTIMEAS_TENTATIVE
         enum
            value = 2
            text = Busy
            defineName = CALENDAR_SHOWTIMEAS_BUSY
         enum
            value = 3
            text = OOF
            defineName = CALENDAR_SHOWTIMEAS_OOF
            mnemonics = Out of Office
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

 

 



