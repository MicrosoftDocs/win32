---
title: DnsServerNetBiosStatistics class
description: DNS server statistics related to NBSTAT buffers usage.
audience: developer
ms.assetid: '1b06b559-64bd-4233-99bd-b5eaa632dca0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerNetBiosStatistics class", "DnsServerNetBiosStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerNetBiosStatistics
- DnsServerNetBiosStatistics.NbstatAlloc
- DnsServerNetBiosStatistics.NbstatFree
- DnsServerNetBiosStatistics.NbstatNetAllocs
- DnsServerNetBiosStatistics.NbstatMemory
- DnsServerNetBiosStatistics.NbstatUsed
- DnsServerNetBiosStatistics.NbstatReturn
- DnsServerNetBiosStatistics.NbstatInUse
- DnsServerNetBiosStatistics.NbstatInFreeList
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerNetBiosStatistics class

DNS server statistics related to NBSTAT buffers usage.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerNetBiosStatistics
{
  uint32 NbstatAlloc;
  uint32 NbstatFree;
  uint32 NbstatNetAllocs;
  uint32 NbstatMemory;
  uint32 NbstatUsed;
  uint32 NbstatReturn;
  uint32 NbstatInUse;
  uint32 NbstatInFreeList;
};
```

## Members

The **DnsServerNetBiosStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerNetBiosStatistics** class has these properties.

<dl> <dt>

**NbstatAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of NetBIOS packet buffers allocated by the server from system memory.

</dd> <dt>

**NbstatFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of NetBIOS packet buffers returned by the server to system memory.

</dd> <dt>

**NbstatInFreeList**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of NetBIOS buffers currently in a free list.

</dd> <dt>

**NbstatInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of NetBIOS buffers currently being used by the server to service queries or being held in a free list.

</dd> <dt>

**NbstatMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total memory used by the NetBIOS packet buffers currently allocated by the server.

</dd> <dt>

**NbstatNetAllocs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of NetBIOS packet buffers currently allocated by the server.

</dd> <dt>

**NbstatReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of NetBIOS buffers freed or returned by the server to a free list.

</dd> <dt>

**NbstatUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of NetBIOS buffers currently in use by the server either servicing queries or in a free list.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





