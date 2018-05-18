---
title: DnsServerTimeoutStatistics class
description: Represents statistics for timeout operations on a DNS server.
audience: developer
ms.assetid: '77f4a1e9-990b-420f-87c8-0c580705c311'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerTimeoutStatistics class", "DnsServerTimeoutStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerTimeoutStatistics
- DnsServerTimeoutStatistics.SetTotal
- DnsServerTimeoutStatistics.SetDirect
- DnsServerTimeoutStatistics.SetFromDereference
- DnsServerTimeoutStatistics.SetFromChildDelete
- DnsServerTimeoutStatistics.AlreadyInSystem
- DnsServerTimeoutStatistics.Checks
- DnsServerTimeoutStatistics.RecentAccess
- DnsServerTimeoutStatistics.ActiveRecord
- DnsServerTimeoutStatistics.CanNotDelete
- DnsServerTimeoutStatistics.Deleted
- DnsServerTimeoutStatistics.ArrayBlocksCreated
- DnsServerTimeoutStatistics.ArrayBlocksDeleted
- DnsServerTimeoutStatistics.DelayedFreesQueued
- DnsServerTimeoutStatistics.DelayedFreesQueuedWithFunction
- DnsServerTimeoutStatistics.DelayedFreesExecuted
- DnsServerTimeoutStatistics.DelayedFreesExecutedWithFunction
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerTimeoutStatistics class

Represents statistics for timeout operations on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerTimeoutStatistics
{
  uint32 SetTotal;
  uint32 SetDirect;
  uint32 SetFromDereference;
  uint32 SetFromChildDelete;
  uint32 AlreadyInSystem;
  uint32 Checks;
  uint32 RecentAccess;
  uint32 ActiveRecord;
  uint32 CanNotDelete;
  uint32 Deleted;
  uint32 ArrayBlocksCreated;
  uint32 ArrayBlocksDeleted;
  uint32 DelayedFreesQueued;
  uint32 DelayedFreesQueuedWithFunction;
  uint32 DelayedFreesExecuted;
  uint32 DelayedFreesExecutedWithFunction;
};
```

## Members

The **DnsServerTimeoutStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerTimeoutStatistics** class has these properties.

<dl> <dt>

**ActiveRecord**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times while performing checks the server encountered a cache node that had records present while checking nodes for deletion.

</dd> <dt>

**AlreadyInSystem**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server marked a node as being eligible for deletion when it is no longer in use by the cache when the node was already so marked.

</dd> <dt>

**ArrayBlocksCreated**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server created a block to hold more references to cache nodes eligible for deletion.

</dd> <dt>

**ArrayBlocksDeleted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server deleted a block to hold references to cache nodes eligible for deletion.

</dd> <dt>

**CanNotDelete**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server encountered a cache node that was marked for deletion that could not be deleted because it had been recently accessed or because it had active records or child nodes.

</dd> <dt>

**Checks**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server performed any node timeout marking operation.

</dd> <dt>

**DelayedFreesExecuted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server released a block of memory that had previously been entered into an internal list of memory blocks that may be freed at some time in the future.

</dd> <dt>

**DelayedFreesExecutedWithFunction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server released a block of memory that had previously been entered into an internal list of memory blocks that may be freed at some time in the future, where a function other than the standard memory free function was used for release.

</dd> <dt>

**DelayedFreesQueued**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server entered a block of memory into an internal list of memory blocks that may be freed at some time in the future.

</dd> <dt>

**DelayedFreesQueuedWithFunction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server entered a block of memory into an internal list of memory blocks that may be freed at some time in the future where the block must be freed using a function other than the standard memory free function.

</dd> <dt>

**Deleted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server successfully deleted a cache node that was marked as eligible for deletion.

</dd> <dt>

**RecentAccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server encountered a cache node that it could not delete because the node had recently been accessed.

</dd> <dt>

**SetDirect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server marked a node as being eligible for deletion when it is no longer in use by the cache, by directly referencing the node.

</dd> <dt>

**SetFromChildDelete**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server marked a node as being eligible for deletion when it is no longer in use by the cache because the node's last child was deleted.

</dd> <dt>

**SetFromDereference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server marked a node as being eligible for deletion when it is no longer in use by the cache because the last reference was deleted.

</dd> <dt>

**SetTotal**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of times the server marked a node as being eligible for deletion when it is no longer in use by the cache.

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

 

 





