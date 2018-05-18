---
title: MSFT\_ReplicationGroup class
description: Represents a consistency grouping of storage replicas.
ms.assetid: 'C828E13D-0AC5-4E83-9BEE-982B4BB1D729'
keywords: ["MSFT_ReplicationGroup class Windows Storage Management API", "MSFT_ReplicationGroup class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup
- MSFT_ReplicationGroup.FriendlyName
- MSFT_ReplicationGroup.Description
- MSFT_ReplicationGroup.HealthStatus
- MSFT_ReplicationGroup.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_ReplicationGroup class

Represents a consistency grouping of storage replicas.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationGroup : MSFT_StorageObject
{
  String FriendlyName;
  String Description;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_ReplicationGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ReplicationGroup** class has these methods.



| Method                                                                                 | Description                                                               |
|:---------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**AddMember**](msft-replicationgroup-addmember.md)                                   | Adds members to this replication group.<br/>                        |
| [**CreateReplica**](msft-replicationgroup-createreplica.md)                           | Creates a replication relationship between replication groups.<br/> |
| [**DeleteObject**](msft-replicationgroup-deleteobject.md)                             | Deletes an empty replication group.<br/>                            |
| [**GetReplicationSettings**](msft-replicationgroup-getreplicationsettings.md)         | Returns the replication settings for this replication group.<br/>   |
| [**RemoveMember**](msft-replicationgroup-removemember.md)                             | Remove members from this replication group.<br/>                    |
| [**SetFriendlyName**](msft-replicationgroup-setfriendlyname.md)                       | Sets the friendly name for the replication group.<br/>              |
| [**SetReplicationRelationship**](msft-replicationgroup-setreplicationrelationship.md) | Modifies the relationship between replication groups.<br/>          |
| [**SetReplicationSettings**](msft-replicationgroup-setreplicationsettings.md)         | Specifies the replication settings for this replication group.<br/> |



 

### Properties

The **MSFT\_ReplicationGroup** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly string representing the description of the replication group.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly string representing the name of the replication group.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Denotes the current health status of the replication group. The health of a group is derived from the health of the backing storage replicas.



| Value                                                                                                                                                                                                                               | Meaning                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span><dl> <dt>**Healthy**</dt> <dt>0</dt> </dl>         | All replicas are in a healthy state.<br/>                                                 |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>1</dt> </dl>         | The majority of replicas are healthy, but one or more may be not fully synchronized.<br/> |
| <span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span><dl> <dt>**Unhealthy**</dt> <dt>2</dt> </dl> | The majority of replicas are unhealthy or in a failed state.<br/>                         |
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>5</dt> </dl>         |                                                                                                 |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current operating conditions of the group. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this group, and can contain multiple values.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (2)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)
</dt> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)
</dt> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>**Relocating** (19)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





