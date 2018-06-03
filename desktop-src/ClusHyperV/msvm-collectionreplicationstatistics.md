---
title: Msvm\_CollectionReplicationStatistics class
description: Provides replication statistics for a virtual system collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ff2154a-e766-4969-9af1-a03a0c53bcda
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_CollectionReplicationStatistics class
- Msvm_CollectionReplicationStatistics class, described
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationStatistics
- Msvm_CollectionReplicationStatistics.InstanceID
- Msvm_CollectionReplicationStatistics.Caption
- Msvm_CollectionReplicationStatistics.Description
- Msvm_CollectionReplicationStatistics.ElementName
- Msvm_CollectionReplicationStatistics.StartStatisticTime
- Msvm_CollectionReplicationStatistics.EndStatisticTime
- Msvm_CollectionReplicationStatistics.ReplicationWALSuccessCount
- Msvm_CollectionReplicationStatistics.ReplicationWALMissCount
- Msvm_CollectionReplicationStatistics.ReplicationSize
- Msvm_CollectionReplicationStatistics.MaxReplicationSize
- Msvm_CollectionReplicationStatistics.PendingReplicationSize
- Msvm_CollectionReplicationStatistics.NetworkFailureCount
- Msvm_CollectionReplicationStatistics.ReplicationFailureCount
- Msvm_CollectionReplicationStatistics.ApplicationConsistentSnapshotFailureCount
- Msvm_CollectionReplicationStatistics.ReplicationHealth
- Msvm_CollectionReplicationStatistics.MaxReplicationLatency
- Msvm_CollectionReplicationStatistics.LastWALReplicationTime
- Msvm_CollectionReplicationStatistics.LastTestFailoverTime
api_location:
- clushyperv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_CollectionReplicationStatistics class

Provides replication statistics for a virtual system collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionReplicationStatistics : CIM_ManagedElement
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  DateTime StartStatisticTime;
  DateTime EndStatisticTime;
  uint32   ReplicationWALSuccessCount;
  uint32   ReplicationWALMissCount;
  uint64   ReplicationSize;
  uint64   MaxReplicationSize;
  uint64   PendingReplicationSize;
  uint32   NetworkFailureCount;
  uint32   ReplicationFailureCount;
  uint32   ApplicationConsistentSnapshotFailureCount;
  uint32   ReplicationHealth;
  uint32   MaxReplicationLatency;
  DateTime LastWALReplicationTime;
  DateTime LastTestFailoverTime;
};
```

## Members

The **Msvm\_CollectionReplicationStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectionReplicationStatistics** class has these properties.

<dl> <dt>

**ApplicationConsistentSnapshotFailureCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total error count for VSS snapshot failures.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**EndStatisticTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the Hyper-V Replica service stopped gathering replication statistics data. At this time new replication statistics cycle starts.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**LastTestFailoverTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time test replica collection was created for a replication enabled virtual system collection on recovery server.

</dd> <dt>

**LastWALReplicationTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the last successful WAL consistent DR cycle was performed.

</dd> <dt>

**MaxReplicationLatency**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum time taken to complete a single replication cycle.

</dd> <dt>

**MaxReplicationSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum replication data transferred to the recovery.

</dd> <dt>

**NetworkFailureCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total network error count for the replication channel with the recovery host system.

</dd> <dt>

**PendingReplicationSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The pending replication data size.

</dd> <dt>

**ReplicationFailureCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The replication error count. This includes errors for replication operation.

</dd> <dt>

**ReplicationHealth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current replication.

</dd> <dt>

**ReplicationSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total replication data transferred to the recovery.

</dd> <dt>

**ReplicationWALMissCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of missed WAL replication cycles. This can be because of heavy workload, network issues or replication errors.

</dd> <dt>

**ReplicationWALSuccessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total successful WAL replication count.

</dd> <dt>

**StartStatisticTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the Hyper-V Replica service started gathering replication statistics data.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Clushyperv.dll</dt> </dl>              |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





