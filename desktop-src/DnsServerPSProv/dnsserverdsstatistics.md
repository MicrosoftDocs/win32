---
title: DnsServerDsStatistics class
description: Represents DNS server statistics related to directory server processing.
audience: developer
ms.assetid: 9e265dd0-7495-433d-a0fe-50001c77ddb8
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerDsStatistics class
- DnsServerDsStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerDsStatistics
- DnsServerDsStatistics.DsTotalNodesRead
- DnsServerDsStatistics.DsTotalRecordsRead
- DnsServerDsStatistics.DsNodesLoaded
- DnsServerDsStatistics.DsRecordsLoaded
- DnsServerDsStatistics.DsTombstonesRead
- DnsServerDsStatistics.DsUpdateSearches
- DnsServerDsStatistics.DsUpdateNodesRead
- DnsServerDsStatistics.DsUpdateRecordsRead
- DnsServerDsStatistics.UpdateLists
- DnsServerDsStatistics.UpdateNodes
- DnsServerDsStatistics.UpdateSuppressed
- DnsServerDsStatistics.UpdateWrites
- DnsServerDsStatistics.UpdateTombstones
- DnsServerDsStatistics.UpdateRecordChange
- DnsServerDsStatistics.UpdateAginRefresh
- DnsServerDsStatistics.UpdateAgingOn
- DnsServerDsStatistics.UpdateAgingOff
- DnsServerDsStatistics.UpdatePacket
- DnsServerDsStatistics.UpdatePacketPrecon
- DnsServerDsStatistics.UpdateAdmin
- DnsServerDsStatistics.UpdateAutoConfig
- DnsServerDsStatistics.UpdateScavenge
- DnsServerDsStatistics.DsNodesAdded
- DnsServerDsStatistics.DsNodesModified
- DnsServerDsStatistics.DsNodesTombstoned
- DnsServerDsStatistics.DsNodesDeleted
- DnsServerDsStatistics.DsRecordsAdded
- DnsServerDsStatistics.DsRecordsReplaced
- DnsServerDsStatistics.DsWriteSuppressed
- DnsServerDsStatistics.DsSerialWrites
- DnsServerDsStatistics.LdapTimedWrites
- DnsServerDsStatistics.LdapWriteTimeTotal
- DnsServerDsStatistics.LdapWriteAverage
- DnsServerDsStatistics.LdapWriteMax
- DnsServerDsStatistics.LdapWriteBucket0
- DnsServerDsStatistics.LdapWriteBucket1
- DnsServerDsStatistics.LdapWriteBucket2
- DnsServerDsStatistics.LdapWriteBucket3
- DnsServerDsStatistics.LdapWriteBucket4
- DnsServerDsStatistics.LdapWriteBucket5
- DnsServerDsStatistics.LdapSearchTime
- DnsServerDsStatistics.FailedDeleteDsEntries
- DnsServerDsStatistics.FailedReadRecords
- DnsServerDsStatistics.FailedLdapModify
- DnsServerDsStatistics.FailedLdapAdd
- DnsServerDsStatistics.PollingPassesWithDsErrors
- DnsServerDsStatistics.LdapReconnects
- DnsServerDsStatistics.DsWriteType
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerDsStatistics class

Represents DNS server statistics related to directory server processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDsStatistics
{
  uint32                 DsTotalNodesRead;
  uint32                 DsTotalRecordsRead;
  uint32                 DsNodesLoaded;
  uint32                 DsRecordsLoaded;
  uint32                 DsTombstonesRead;
  uint32                 DsUpdateSearches;
  uint32                 DsUpdateNodesRead;
  uint32                 DsUpdateRecordsRead;
  uint32                 UpdateLists;
  uint32                 UpdateNodes;
  uint32                 UpdateSuppressed;
  uint32                 UpdateWrites;
  uint32                 UpdateTombstones;
  uint32                 UpdateRecordChange;
  uint32                 UpdateAginRefresh;
  uint32                 UpdateAgingOn;
  uint32                 UpdateAgingOff;
  uint32                 UpdatePacket;
  uint32                 UpdatePacketPrecon;
  uint32                 UpdateAdmin;
  uint32                 UpdateAutoConfig;
  uint32                 UpdateScavenge;
  uint32                 DsNodesAdded;
  uint32                 DsNodesModified;
  uint32                 DsNodesTombstoned;
  uint32                 DsNodesDeleted;
  uint32                 DsRecordsAdded;
  uint32                 DsRecordsReplaced;
  uint32                 DsWriteSuppressed;
  uint32                 DsSerialWrites;
  uint32                 LdapTimedWrites;
  uint32                 LdapWriteTimeTotal;
  uint32                 LdapWriteAverage;
  uint32                 LdapWriteMax;
  uint32                 LdapWriteBucket0;
  uint32                 LdapWriteBucket1;
  uint32                 LdapWriteBucket2;
  uint32                 LdapWriteBucket3;
  uint32                 LdapWriteBucket4;
  uint32                 LdapWriteBucket5;
  uint32                 LdapSearchTime;
  uint32                 FailedDeleteDsEntries;
  uint32                 FailedReadRecords;
  uint32                 FailedLdapModify;
  uint32                 FailedLdapAdd;
  uint32                 PollingPassesWithDsErrors;
  uint32                 LdapReconnects;
  DnsServerRecordRequest DsWriteType[];
};
```

## Members

The **DnsServerDsStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDsStatistics** class has these properties.

<dl> <dt>

**DsNodesAdded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of new nodes added to the directory server.

</dd> <dt>

**DsNodesDeleted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of nodes deleted from the directory server.

</dd> <dt>

**DsNodesLoaded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of valid DNS nodes found in the directory server and loaded in memory by the server.

</dd> <dt>

**DsNodesModified**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of nodes modified in the directory server.

</dd> <dt>

**DsNodesTombstoned**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of nodes tombstoned in the directory server

</dd> <dt>

**DsRecordsAdded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of records added to the directory server.

</dd> <dt>

**DsRecordsLoaded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of resource records loaded in memory by the server.

</dd> <dt>

**DsRecordsReplaced**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of records modified or replaced in the directory server.

</dd> <dt>

**DsSerialWrites**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of records that had matching data and hence were not written to the directory server.

</dd> <dt>

**DsTombstonesRead**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of nodes read from the directory server and found in a tombstoned state.

</dd> <dt>

**DsTotalNodesRead**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of DNS nodes read from the directory server.

</dd> <dt>

**DsTotalRecordsRead**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of resource records read from the directory server.

</dd> <dt>

**DsUpdateNodesRead**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of DNS nodes that were read from the directory server and contained updated information.

</dd> <dt>

**DsUpdateRecordsRead**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of resource records that were read from the directory server and contained updated information.

</dd> <dt>

**DsUpdateSearches**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone update searches performed on the directory server.

</dd> <dt>

**DsWriteSuppressed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of records added to the directory server.

</dd> <dt>

**DsWriteType**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecordRequest** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecordRequest**](dnsserverrecordrequest.md)")
</dt> </dl>

An array of 32-bit unsigned integers that keeps track of update requests for different DNS record types.

</dd> <dt>

**FailedDeleteDsEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to delete entries from the directory server.

</dd> <dt>

**FailedLdapAdd**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to add entries to the directory server.

</dd> <dt>

**FailedLdapModify**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to modify records in the directory server.

</dd> <dt>

**FailedReadRecords**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to read records from the directory server.

</dd> <dt>

**LdapReconnects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server attempted to reconnect to the directory server.

</dd> <dt>

**LdapSearchTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative time, in milliseconds, consumed by server-performed LDAP searches.

</dd> <dt>

**LdapTimedWrites**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server performed a timed LDAP write operation.

</dd> <dt>

**LdapWriteAverage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The average time, in milliseconds, for all server performed timed LDAP write operations since the server was last restarted.

</dd> <dt>

**LdapWriteBucket0**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took less than 10 milliseconds.

</dd> <dt>

**LdapWriteBucket1**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took between 10 and 100 milliseconds.

</dd> <dt>

**LdapWriteBucket2**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took between 100 milliseconds and 1 second.

</dd> <dt>

**LdapWriteBucket3**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took between 1 and 10 seconds.

</dd> <dt>

**LdapWriteBucket4**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took between 10 and 100 seconds.

</dd> <dt>

**LdapWriteBucket5**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of LDAP write-operations that took more than 100 seconds.

</dd> <dt>

**LdapWriteMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The longest duration taken, in milliseconds, for any single server-performed timed LDAP write-operation.

</dd> <dt>

**LdapWriteTimeTotal**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative time, in milliseconds, consumed by server-performed timed LDAP write operations.

</dd> <dt>

**PollingPassesWithDsErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server hit failure while polling zones in the directory server.

</dd> <dt>

**UpdateAdmin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes modified as a result of administrator initiated changes.

</dd> <dt>

**UpdateAgingOff**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required aging to be disabled.

</dd> <dt>

**UpdateAgingOn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required aging to be enabled.

</dd> <dt>

**UpdateAginRefresh**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required an aging information refresh.

</dd> <dt>

**UpdateAutoConfig**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes modified as a result of an auto-configure operation.

</dd> <dt>

**UpdateLists**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes with an updated list of record.

</dd> <dt>

**UpdateNodes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required an update in the directory server.

</dd> <dt>

**UpdatePacket**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes modified as a result of update packets being received.

</dd> <dt>

**UpdatePacketPrecon**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes modified as a result of update packets being received with prerequisites.

</dd> <dt>

**UpdateRecordChange**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required record changes.

</dd> <dt>

**UpdateScavenge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes modified as a result of a scavenging cycle.

</dd> <dt>

**UpdateSuppressed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that did not require any write to the directory server

</dd> <dt>

**UpdateTombstones**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required tombstoning.

</dd> <dt>

**UpdateWrites**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in-memory nodes that required writing to the directory server.

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

 

 





