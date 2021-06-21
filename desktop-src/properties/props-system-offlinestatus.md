---
description: System.OfflineStatus
ms.assetid: 0badb5dd-6342-4110-b7a9-0b291dfe8578
title: System.OfflineStatus
ms.topic: article
ms.date: 05/31/2018
---

# System.OfflineStatus

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.OfflineStatus
   shellPKey = PKEY_OfflineStatus
   formatID = 6D24888F-4718-4BDA-AFED-EA0FB4386CD8
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
            name = Online
            value = 0
            text = Online
            defineToken = OFFLINESTATUS_ONLINE
         enum
            name = Offline
            value = 1
            text = Offline
            defineToken = OFFLINESTATUS_OFFLINE
         enum
            name = OfflineForced
            value = 2
            text = Offline (working offline)
            defineToken = OFFLINESTATUS_OFFLINE_FORCED
         enum
            name = OfflineSlow
            value = 3
            text = Offline (background sync)
            defineToken = OFFLINESTATUS_OFFLINE_SLOW
         enum
            name = OfflineError
            value = 4
            text = Offline (not connected)
            defineToken = OFFLINESTATUS_OFFLINE_ERROR
         enum
            name = OfflineConflict
            value = 5
            text = Offline (need to sync)
            defineToken = OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT
         enum
            name = OfflineSuspended
            value = 6
            text = Offline (always)
            defineToken = OFFLINESTATUS_OFFLINE_SUSPENDED
```

## Windows 7

```
propertyDescription
   name = System.OfflineStatus
   shellPKey = PKEY_OfflineStatus
   formatID = 6D24888F-4718-4BDA-AFED-EA0FB4386CD8
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
            name = Online
            value = 0
            text = Online
            defineToken = OFFLINESTATUS_ONLINE
         enum
            name = Offline
            value = 1
            text = Offline
            defineToken = OFFLINESTATUS_OFFLINE
         enum
            name = OfflineForced
            value = 2
            text = Offline (working offline)
            defineToken = OFFLINESTATUS_OFFLINE_FORCED
         enum
            name = OfflineSlow
            value = 3
            text = Offline (slow connection)
            defineToken = OFFLINESTATUS_OFFLINE_SLOW
         enum
            name = OfflineError
            value = 4
            text = Offline (not connected)
            defineToken = OFFLINESTATUS_OFFLINE_ERROR
         enum
            name = OfflineConflict
            value = 5
            text = Offline (need to sync)
            defineToken = OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT
         enum
            name = OfflineSuspended
            value = 6
            text = Offline (always)
            defineToken = OFFLINESTATUS_OFFLINE_SUSPENDED
```

## Windows Vista

```
propertyDescription
   name = System.OfflineStatus
   shellPKey = PKEY_OfflineStatus
   formatID = 6D24888F-4718-4BDA-AFED-EA0FB4386CD8
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
            text = Online
            defineName = OFFLINESTATUS_ONLINE
         enum
            value = 1
            text = Offline
            defineName = OFFLINESTATUS_OFFLINE
         enum
            value = 2
            text = Offline (working offline)
            defineName = OFFLINESTATUS_OFFLINE_FORCED
         enum
            value = 3
            text = Offline (slow connection)
            defineName = OFFLINESTATUS_OFFLINE_SLOW
         enum
            value = 4
            text = Offline (not connected)
            defineName = OFFLINESTATUS_OFFLINE_ERROR
         enum
            value = 5
            text = Offline (need to sync)
            defineName = OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT
         enum
            value = 6
            text = Offline (always)
            defineName = OFFLINESTATUS_OFFLINE_SUSPENDED
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> </dl>

 

 
