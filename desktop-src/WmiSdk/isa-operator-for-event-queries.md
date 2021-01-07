---
description: The ISA operator is a WQL-specific operator that can be used in event queries. When ISA is included in the WHERE clause of an event query, it requests notification of events for all classes within a class hierarchy, rather than a specific event class.
ms.assetid: 68b7a903-a206-4491-95c4-4a412537f6f5
ms.tgt_platform: multiple
title: ISA Operator for Event Queries
ms.topic: article
ms.date: 05/31/2018
---

# ISA Operator for Event Queries

The ISA operator is a WQL-specific operator that can be used in event queries. When ISA is included in the [WHERE clause](where-clause.md) of an event query, it requests notification of events for all classes within a class hierarchy, rather than a specific event class.

The following example requests notification every 10 minutes of instance modification events for all instances that are members of any class derived from the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.


```sql
SELECT * FROM __InstanceModificationEvent WITHIN 600
WHERE TargetInstance ISA "Win32_LogicalDisk"
```



For more information on using ISA with an event query, see [Creating a Timer Event with Win32\_LocalTime or Win32\_UTCTime](./creating-a-timer-event-with-win32-localtime-or-win32-utctime.md).

 

 
