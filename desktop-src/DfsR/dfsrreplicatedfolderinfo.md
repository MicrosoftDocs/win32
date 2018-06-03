---
title: DfsrReplicatedFolderInfo class
description: This class provides statistical and operational information for each replicated folder hosted on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: edeed173-8a1c-4a4f-be03-c658eee6e73b
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrReplicatedFolderInfo class Distributed File System Replication
- DfsrReplicatedFolderInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrReplicatedFolderInfo
- DfsrReplicatedFolderInfo.Caption
- DfsrReplicatedFolderInfo.Description
- DfsrReplicatedFolderInfo.InstallDate
- DfsrReplicatedFolderInfo.Name
- DfsrReplicatedFolderInfo.Status
- DfsrReplicatedFolderInfo.ReplicatedFolderGuid
- DfsrReplicatedFolderInfo.ReplicatedFolderName
- DfsrReplicatedFolderInfo.ReplicationGroupGuid
- DfsrReplicatedFolderInfo.ReplicationGroupName
- DfsrReplicatedFolderInfo.MemberGuid
- DfsrReplicatedFolderInfo.MemberName
- DfsrReplicatedFolderInfo.LastConflictCleanupTime
- DfsrReplicatedFolderInfo.LastTombstoneCleanupTime
- DfsrReplicatedFolderInfo.CurrentStageSizeInMb
- DfsrReplicatedFolderInfo.CurrentConflictSizeInMb
- DfsrReplicatedFolderInfo.State
- DfsrReplicatedFolderInfo.LastErrorCode
- DfsrReplicatedFolderInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DfsrReplicatedFolderInfo class

This class provides statistical and operational information for each replicated folder hosted on the local computer.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrReplicatedFolderInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       ReplicatedFolderGuid;
  string       ReplicatedFolderName;
  string       ReplicationGroupGuid;
  string       ReplicationGroupName;
  string       MemberGuid;
  string       MemberName;
  datetime     LastConflictCleanupTime;
  datetime     LastTombstoneCleanupTime;
  uint32       CurrentStageSizeInMb;
  uint32       CurrentConflictSizeInMb;
  uint8        State;
  uint32       LastErrorCode;
  uint32       LastErrorMessageId;
};
```

## Members

The **DfsrReplicatedFolderInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrReplicatedFolderInfo** class has these methods.



| Method                                                                                              | Description                                                                                                                  |
|:----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**CleanupConflictDirectory**](cleanupconflictdirectory-dfsrreplicatedfolderinfo.md)               | Starts the Conflict and Deleted folder cleanup process.<br/>                                                           |
| [**Fence**](fence-dfsrreplicatedfolderinfo.md)                                                     | Applies a fence to a specific file or folder.<br/>                                                                     |
| [**GetOutboundBacklogFileCount**](getoutboundbacklogfilecount-dfsrreplicatedfolderinfo.md)         | Retrieves the number of files scheduled to be replicated to an outbound partner given its version vector.<br/>         |
| [**GetOutboundBacklogFileIdRecords**](getoutboundbacklogfileidrecords-dfsrreplicatedfolderinfo.md) | Retrieves the list of files that are scheduled to be replicated to the outbound partner given its version vector.<br/> |
| [**GetStatus**](dfsrreplicatedfolderinfo-getstatus.md)                                             | This method is reserved for system use.<br/>                                                                           |
| [**GetVersionVector**](getversionvector-dfsrreplicatedfolderinfo.md)                               | Retrieves the current version vector chain of this member.<br/>                                                        |



 

### Properties

The **DfsrReplicatedFolderInfo** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**CurrentConflictSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Conflict and Deleted Folder Size in MB"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB")
</dt> </dl>

The current size of the Conflict and Deleted folder, in MB.

</dd> <dt>

**CurrentStageSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Staging Folder Size in MB"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB")
</dt> </dl>

The current size of the staging folder, in MB.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**LastConflictCleanupTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Conflict Cleanup Time")
</dt> </dl>

The last time the conflict cleanup process ran on this replicated folder.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Code")
</dt> </dl>

The last error code.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

The event log message identifier that corresponds to the last error code.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**LastTombstoneCleanupTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Tombstone Cleanup Time")
</dt> </dl>

The last time the tombstone cleanup process ran on this replicated folder.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The GUID of the member that hosts this replicated folder.

</dd> <dt>

**MemberName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member Name")
</dt> </dl>

The name of the member that hosts this replicated folder.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The identifier of the local replicated folder.

</dd> <dt>

**ReplicatedFolderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder Name")
</dt> </dl>

The friendly name of the replicated folder. The name is not required to be unique.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique replication group identifier.

</dd> <dt>

**ReplicationGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Name")
</dt> </dl>

The name of the replication group that contains this replicated folder.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder State")
</dt> </dl>

The current replicated folder state for this member.

<dt>

<span id="Uninitialized"></span><span id="uninitialized"></span><span id="UNINITIALIZED"></span>

**Uninitialized** (0)


</dt> <dd></dd> <dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (1)


</dt> <dd></dd> <dt>

<span id="Initial_Sync"></span><span id="initial_sync"></span><span id="INITIAL_SYNC"></span>

**Initial Sync** (2)


</dt> <dd></dd> <dt>

<span id="Auto_Recovery"></span><span id="auto_recovery"></span><span id="AUTO_RECOVERY"></span>

**Auto Recovery** (3)


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (4)


</dt> <dd></dd> <dt>

<span id="In_Error"></span><span id="in_error"></span><span id="IN_ERROR"></span>

**In Error** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> </dl>

## Examples

The [Get-DFSRBacklog](https://Gallery.TechNet.Microsoft.Com/dac62790-219d-4325-a57b-e79c2aa6b58e) PowerShell code sample on TechNet Gallery uses DfsrReplicatedFolderInfo to retrieve DFSR backlog for replication groups of the targeted server.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





