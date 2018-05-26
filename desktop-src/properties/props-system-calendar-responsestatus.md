---
Description: Stores the status of a users responses to meetings in the calendar.
ms.assetid: 5cbc0306-20c7-4f12-bb8b-3889b93dfd69
title: System.Calendar.ResponseStatus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Calendar.ResponseStatus

Stores the status of a user's responses to meetings in the calendar.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Calendar.ResponseStatus
   shellPKey = PKEY_Calendar_ResponseStatus
   formatID = 188C1F91-3C40-4132-9EC5-D8B03B72A8A2
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = None
            value = 0
            text = None
            defineToken = CALENDAR_RESPONSESTATUS_NONE
         enum
            name = Organized
            value = 1
            text = Organized
            defineToken = CALENDAR_RESPONSESTATUS_ORGANIZED
         enum
            name = Tentative
            value = 2
            text = Tentative
            defineToken = CALENDAR_RESPONSESTATUS_TENTATIVE
         enum
            name = Accepted
            value = 3
            text = Accepted
            defineToken = CALENDAR_RESPONSESTATUS_ACCEPTED
         enum
            name = Declined
            value = 4
            text = Declined
            defineToken = CALENDAR_RESPONSESTATUS_DECLINED
         enum
            name = NotResponded
            value = 5
            text = Not Responded
            defineToken = CALENDAR_RESPONSESTATUS_NOTRESPONDED
```

## Windows Vista

```
propertyDescription
   name = System.Calendar.ResponseStatus
   shellPKey = PKEY_Calendar_ResponseStatus
   formatID = 188C1F91-3C40-4132-9EC5-D8B03B72A8A2
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = None
            defineName = CALENDAR_RESPONSESTATUS_NONE
         enum
            value = 1
            text = Organized
            defineName = CALENDAR_RESPONSESTATUS_ORGANIZED
         enum
            value = 2
            text = Tentative
            defineName = CALENDAR_RESPONSESTATUS_TENTATIVE
         enum
            value = 3
            text = Accepted
            defineName = CALENDAR_RESPONSESTATUS_ACCEPTED
         enum
            value = 4
            text = Declined
            defineName = CALENDAR_RESPONSESTATUS_DECLINED
         enum
            value = 5
            text = Not Responded
            defineName = CALENDAR_RESPONSESTATUS_NOTRESPONDED
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

 

 



