---
title: MSFT\_SMReplicationGroup class
description: A replication group represents a consistency grouping of storage replicas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e57f2b26-0cdd-4e07-b075-58b4ceee199b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMReplicationGroup class
- MSFT_SMReplicationGroup class, described
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroup
- MSFT_SMReplicationGroup.ObjectId
- MSFT_SMReplicationGroup.Identifier
- MSFT_SMReplicationGroup.DisplayName
- MSFT_SMReplicationGroup.Description
- MSFT_SMReplicationGroup.HealthStatus
- MSFT_SMReplicationGroup.OperationalStatus
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMReplicationGroup class

A replication group represents a consistency grouping of storage replicas.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicationGroup : MSFT_SMStorageObject
{
  String ObjectId;
  String Identifier;
  String DisplayName;
  String Description;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_SMReplicationGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMReplicationGroup** class has these methods.



| Method                                                                                   | Description                                                            |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**AddMembers**](addmembers-msft-smreplicationgroup.md)                                 | Adds members to the replication group.<br/>                      |
| [**CreateReplica**](createreplica-msft-smreplicationgroup.md)                           | Creates a replica relationship between replication groups.<br/>  |
| [**Delete**](delete-msft-smreplicationgroup.md)                                         | Deletes an empty replication group.<br/>                         |
| [**GetReplicationSettings**](getreplicationsettings-msft-smreplicationgroup.md)         | Retrieves the replication settings for a replication group.<br/> |
| [**RemoveMembers**](removemembers-msft-smreplicationgroup.md)                           | Removes members from the replication group.<br/>                 |
| [**SetFriendlyName**](setfriendlyname-msft-smreplicationgroup.md)                       | Updates the user friendly name of a replication group.<br/>      |
| [**SetReplicationRelationship**](setreplicationrelationship-msft-smreplicationgroup.md) | Updates the relationship between replication groups.<br/>        |
| [**SetReplicationSettings**](setreplicationsettings-msft-smreplicationgroup.md)         | Updates the replication settings for a replication group.<br/>   |



 

### Properties

The **MSFT\_SMReplicationGroup** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the replication group.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The name of the replication group.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The health status of the replication group.

The possible values are:

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the current operating status of the hardware, software, and infrastructure of the replication group.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** (4)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

**In Service** (11)


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (14)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

**Supporting Entity in Error** (16)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (17)


</dt> <dd></dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

**Power Mode** (18)


</dt> <dd></dd> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>

**Relocating** (19)


</dt> <dd></dd> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>

**Microsoft Reserved**


</dt> <dd>20 ...</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



 

 





