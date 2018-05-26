---
title: DnsServerMemtagStatistics class
description: DNS server statistics related to memory allocations for a given purpose.
audience: developer
ms.assetid: 09a051c3-b671-454d-be53-1644a314648b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerMemtagStatistics class
- DnsServerMemtagStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerMemtagStatistics
- DnsServerMemtagStatistics.NumberOfMemoryAllocations
- DnsServerMemtagStatistics.NumberOfMemoryFrees
- DnsServerMemtagStatistics.MemoryUsedBytes
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerMemtagStatistics class

DNS server statistics related to memory allocations for a given purpose.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerMemtagStatistics
{
  uint32 NumberOfMemoryAllocations;
  uint32 NumberOfMemoryFrees;
  uint32 MemoryUsedBytes;
};
```

## Members

The **DnsServerMemtagStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerMemtagStatistics** class has these properties.

<dl> <dt>

**MemoryUsedBytes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of memory, in bytes, currently in use for a given purpose.

</dd> <dt>

**NumberOfMemoryAllocations**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times memory allocations have been performed for a given purpose.

</dd> <dt>

**NumberOfMemoryFrees**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times memory has been released for a given purpose.

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

 

 





