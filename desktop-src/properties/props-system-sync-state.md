---
description: State of the system synch.
ms.assetid: e7659752-ba8c-4b3b-bd1e-2f5044a3ab47
title: System.Sync.State
ms.topic: article
ms.date: 05/31/2018
---

# System.Sync.State

State of the system synch.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Sync.State
   shellPKey = PKEY_Sync_State
   formatID = 7BD5533E-AF15-44DB-B8C8-BD6624E1D032
   propID = 24
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotSetup
            value = 0
            text = Setup sync
            defineToken = SYNC_STATE_NOTSETUP
         enum
            name = NotRun
            value = 1
            text = Not synced yet
            defineToken = SYNC_STATE_SYNCNOTRUN
         enum
            name = Idle
            value = 2
            text = Not synced yet
            defineToken = SYNC_STATE_IDLE
         enum
            name = SyncErrors
            value = 3
            text = Synced with errors
            defineToken = SYNC_STATE_ERROR
         enum
            name = Pending
            value = 4
            text = Sync pending
            defineToken = SYNC_STATE_PENDING
         enum
            name = Syncing
            value = 5
            text = Syncing
            defineToken = SYNC_STATE_SYNCING
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

 

 
