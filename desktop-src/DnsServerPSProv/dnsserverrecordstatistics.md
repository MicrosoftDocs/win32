---
title: DnsServerRecordStatistics class
description: Represents DNS server statistics related to record usage.
audience: developer
ms.assetid: 6ddd06b9-b054-4658-8d1e-a2ea2caa310d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRecordStatistics class
- DnsServerRecordStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerRecordStatistics
- DnsServerRecordStatistics.InUse
- DnsServerRecordStatistics.Used
- DnsServerRecordStatistics.Return
- DnsServerRecordStatistics.Memory
- DnsServerRecordStatistics.CacheTotal
- DnsServerRecordStatistics.CacheCurrent
- DnsServerRecordStatistics.CacheTimeouts
- DnsServerRecordStatistics.SlowFreeQueued
- DnsServerRecordStatistics.SlowFreeFinished
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerRecordStatistics class

Represents DNS server statistics related to record usage.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRecordStatistics
{
  uint32 InUse;
  uint32 Used;
  uint32 Return;
  uint32 Memory;
  uint32 CacheTotal;
  uint32 CacheCurrent;
  uint32 CacheTimeouts;
  uint32 SlowFreeQueued;
  uint32 SlowFreeFinished;
};
```

## Members

The **DnsServerRecordStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRecordStatistics** class has these properties.

<dl> <dt>

**CacheCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of resource records currently cached by the server.

</dd> <dt>

**CacheTimeouts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of resource records that have been freed from the DNS server's cache.

</dd> <dt>

**CacheTotal**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number resource records cached by the server.

</dd> <dt>

**InUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of resource records currently allocated by the server.

</dd> <dt>

**Memory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of memory, in bytes, currently allocated for resource records by the server.

</dd> <dt>

**Return**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of resource records freed by the server.

</dd> <dt>

**SlowFreeFinished**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of slow frees that have been completed.

</dd> <dt>

**SlowFreeQueued**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Some cached record types, such as NS and SOA, are not immediately freed to the pool of allocated records. Instead they are placed in a timeout queue and returned after the timeout expires. This is the cumulative count of such slow-free records that have been entered into the timeout queue.

</dd> <dt>

**Used**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of resource records allocated by the server

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





