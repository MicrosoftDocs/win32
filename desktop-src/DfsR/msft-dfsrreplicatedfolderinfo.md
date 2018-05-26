---
title: MSFT\_DfsrReplicatedFolderInfo class
description: This class provides statistical and operational information for each replicated folder hosted on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1d9127e5-8eaa-4d85-80b2-62ace8b4a9d0
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrReplicatedFolderInfo class Distributed File System Replication
- MSFT_DfsrReplicatedFolderInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrReplicatedFolderInfo
- MSFT_DfsrReplicatedFolderInfo.ReplicatedFolderGuid
- MSFT_DfsrReplicatedFolderInfo.ReplicatedFolderName
- MSFT_DfsrReplicatedFolderInfo.ReplicationGroupGuid
- MSFT_DfsrReplicatedFolderInfo.ReplicationGroupName
- MSFT_DfsrReplicatedFolderInfo.MemberGuid
- MSFT_DfsrReplicatedFolderInfo.MemberName
- MSFT_DfsrReplicatedFolderInfo.LastConflictCleanupTime
- MSFT_DfsrReplicatedFolderInfo.LastTombstoneCleanupTime
- MSFT_DfsrReplicatedFolderInfo.CurrentStageSizeInMb
- MSFT_DfsrReplicatedFolderInfo.CurrentConflictSizeInMb
- MSFT_DfsrReplicatedFolderInfo.State
- MSFT_DfsrReplicatedFolderInfo.LastErrorCode
- MSFT_DfsrReplicatedFolderInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrReplicatedFolderInfo class

This class provides statistical and operational information for each replicated folder hosted on the local computer.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrReplicatedFolderInfo
{
  string   ReplicatedFolderGuid;
  string   ReplicatedFolderName;
  string   ReplicationGroupGuid;
  string   ReplicationGroupName;
  string   MemberGuid;
  string   MemberName;
  datetime LastConflictCleanupTime;
  datetime LastTombstoneCleanupTime;
  uint32   CurrentStageSizeInMb;
  uint32   CurrentConflictSizeInMb;
  uint8    State;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **MSFT\_DfsrReplicatedFolderInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrReplicatedFolderInfo** class has these methods.



| Method                                                                                                   | Description                                                                                                                  |
|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**CleanupConflictDirectory**](cleanupconflictdirectory-msft-dfsrreplicatedfolderinfo.md)               | Starts the Conflict and Deleted folder cleanup process.<br/>                                                           |
| [**Fence**](fence-msft-dfsrreplicatedfolderinfo.md)                                                     | Applies a fence to a specific file or folder.<br/>                                                                     |
| [**GetOutboundBacklogFileCount**](getoutboundbacklogfilecount-msft-dfsrreplicatedfolderinfo.md)         | Retrieves the number of files scheduled to be replicated to an outbound partner given its version vector.<br/>         |
| [**GetOutboundBacklogFileIdRecords**](getoutboundbacklogfileidrecords-msft-dfsrreplicatedfolderinfo.md) | Retrieves the list of files that are scheduled to be replicated to the outbound partner given its version vector.<br/> |
| [**GetStatus**](getstatus-msft-dfsrreplicatedfolderinfo.md)                                             | This method is reserved for system use.<br/>                                                                           |
| [**GetVersionVector**](getversionvector-msft-dfsrreplicatedfolderinfo.md)                               | Retrieves the current version vector chain of this member.<br/>                                                        |



 

### Properties

The **MSFT\_DfsrReplicatedFolderInfo** class has these properties.

<dl> <dt>

**CurrentConflictSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Conflict and Deleted Folder Size in MB")
</dt> </dl>

The current size of the Conflict and Deleted folder, in MB.

</dd> <dt>

**CurrentStageSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Staging Folder Size in MB")
</dt> </dl>

The current size of the staging folder, in MB.

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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The **GUID** of the member that hosts this replicated folder.

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

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID")
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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
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

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





