---
title: DnsServerMemoryStatistics class
description: DNS server statistics related to memory usage for different operations on the server.
audience: developer
ms.assetid: 'fe841ce6-cdfb-446e-89a2-64878dd7b5cb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerMemoryStatistics class", "DnsServerMemoryStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerMemoryStatistics
- DnsServerMemoryStatistics.Memory
- DnsServerMemoryStatistics.Alloc
- DnsServerMemoryStatistics.Free
- DnsServerMemoryStatistics.StdUsed
- DnsServerMemoryStatistics.StdReturn
- DnsServerMemoryStatistics.StdInUse
- DnsServerMemoryStatistics.StdMemory
- DnsServerMemoryStatistics.StdToHeapAlloc
- DnsServerMemoryStatistics.StdToHeapFree
- DnsServerMemoryStatistics.StdToHeapInUse
- DnsServerMemoryStatistics.StdToHeapMemory
- DnsServerMemoryStatistics.StdBlockAlloc
- DnsServerMemoryStatistics.StdBlockUsed
- DnsServerMemoryStatistics.StdBlockReturn
- DnsServerMemoryStatistics.StdBlockInUse
- DnsServerMemoryStatistics.StdBlockFreeList
- DnsServerMemoryStatistics.StdBlockFreeListMemory
- DnsServerMemoryStatistics.StdBlockMemory
- DnsServerMemoryStatistics.MemTags
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerMemoryStatistics class

DNS server statistics related to memory usage for different operations on the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerMemoryStatistics
{
  uint32                    Memory;
  uint32                    Alloc;
  uint32                    Free;
  uint32                    StdUsed;
  uint32                    StdReturn;
  uint32                    StdInUse;
  uint32                    StdMemory;
  uint32                    StdToHeapAlloc;
  uint32                    StdToHeapFree;
  uint32                    StdToHeapInUse;
  uint32                    StdToHeapMemory;
  uint32                    StdBlockAlloc;
  uint32                    StdBlockUsed;
  uint32                    StdBlockReturn;
  uint32                    StdBlockInUse;
  uint32                    StdBlockFreeList;
  uint32                    StdBlockFreeListMemory;
  uint32                    StdBlockMemory;
  DnsServerMemtagStatistics MemTags[];
};
```

## Members

The **DnsServerMemoryStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerMemoryStatistics** class has these properties.

<dl> <dt>

**Alloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times memory was allocated by the server.

</dd> <dt>

**Free**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times memory was released by the server.

</dd> <dt>

**Memory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total memory currently allocated by the servers, in bytes.

</dd> <dt>

**MemTags**
</dt> <dd> <dl> <dt>

Data type: **DnsServerMemtagStatistics** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerMemtagStatistics**](dnsservermemtagstatistics.md)")
</dt> </dl>

Memory statistics for various server operations.

</dd> <dt>

**StdBlockAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of common-size blocks allocated by the server.

</dd> <dt>

**StdBlockFreeList**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of common-size blocks currently on internal free lists.

</dd> <dt>

**StdBlockFreeListMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of memory, in bytes, of common size blocks currently on internal free lists.

</dd> <dt>

**StdBlockInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of common-size blocks currently being used.

</dd> <dt>

**StdBlockMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of memory, in bytes, of all currently allocated blocks.

</dd> <dt>

**StdBlockReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of common-size blocks returned from an internal free list.

</dd> <dt>

**StdBlockUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of common-size blocks allocated from an internal free list.

</dd> <dt>

**StdInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of common-size blocks of allocated memory currently used by the server.

</dd> <dt>

**StdMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size, in bytes, of common-size blocks that are currently being used by the server.

</dd> <dt>

**StdReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times a common-size block of memory was released by the server.

</dd> <dt>

**StdToHeapAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of arbitrary-size blocks of memory allocated from system memory.

</dd> <dt>

**StdToHeapFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of arbitrary-size blocks of memory released to system memory.

</dd> <dt>

**StdToHeapInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of arbitrary-size blocks of memory currently in use.

</dd> <dt>

**StdToHeapMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of memory, in bytes, currently used by non-standard sized blocks.

</dd> <dt>

**StdUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of times a common-size block of memory was allocated by the server.

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

 

 





