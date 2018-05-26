---
title: GetSupportedOperations method of the MSFT\_SMReplicationCapabilities class
description: Retrieves the supported operations for the specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e2511e92-df05-4952-b546-768e5d085094
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedOperations method
- GetSupportedOperations method, MSFT_SMReplicationCapabilities class
- MSFT_SMReplicationCapabilities class, GetSupportedOperations method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationCapabilities.GetSupportedOperations
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedOperations method of the MSFT\_SMReplicationCapabilities class

Retrieves the supported operations for the specified replication type.

## Syntax


```mof
uint32 GetSupportedOperations(
  [in]            uint16                ReplicationType,
  [out]           uint16                SupportedOperations[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Indicates the replication type for which to retrieve supported operations.

The possible values are:

<dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>

**Synchronous Mirror Local** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>

**Asynchronous Mirror Local** (3)


</dt> <dd></dd> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>

**Synchronous Mirror Remote** (4)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>

**Asynchronous Mirror Remote** (5)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Synchronous Snapshot Local** (6)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Asynchronous Snapshot Local** (7)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Synchronous Snapshot Remote** (8)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Asynchronous Snapshot Remote** (9)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>

**Synchronous Clone Local** (10)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>

**Asynchronous Clone Local** (11)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>

**Synchronous Clone Remote** (12)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>

**Asynchronous Clone Remote** (13)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Local"></span><span id="synchronous_tokenizedclone_local"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Synchronous TokenizedClone Local** (14)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Local"></span><span id="asynchronous_tokenizedclone_local"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Asynchronous TokenizedClone Local** (15)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Remote"></span><span id="synchronous_tokenizedclone_remote"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Synchronous TokenizedClone Remote** (16)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Remote"></span><span id="asynchronous_tokenizedclone_remote"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Asynchronous TokenizedClone Remote** (17)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Local"></span><span id="adaptive_mirror_local"></span><span id="ADAPTIVE_MIRROR_LOCAL"></span>

**Adaptive Mirror Local** (18)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Remote"></span><span id="adaptive_mirror_remote"></span><span id="ADAPTIVE_MIRROR_REMOTE"></span>

**Adaptive Mirror Remote** (19)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Local"></span><span id="adaptive_snapshot_local"></span><span id="ADAPTIVE_SNAPSHOT_LOCAL"></span>

**Adaptive Snapshot Local** (20)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Remote"></span><span id="adaptive_snapshot_remote"></span><span id="ADAPTIVE_SNAPSHOT_REMOTE"></span>

**Adaptive Snapshot Remote** (21)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Local"></span><span id="adaptive_clone_local"></span><span id="ADAPTIVE_CLONE_LOCAL"></span>

**Adaptive Clone Local** (22)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Remote"></span><span id="adaptive_clone_remote"></span><span id="ADAPTIVE_CLONE_REMOTE"></span>

**Adaptive Clone Remote** (23)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Local"></span><span id="adaptive_tokenizedclone_local"></span><span id="ADAPTIVE_TOKENIZEDCLONE_LOCAL"></span>

**Adaptive TokenizedClone Local** (24)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Remote"></span><span id="adaptive_tokenizedclone_remote"></span><span id="ADAPTIVE_TOKENIZEDCLONE_REMOTE"></span>

**Adaptive TokenizedClone Remote** (25)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (32768)


</dt> <dd></dd> </dl> </dd> <dt>

*SupportedOperations* \[out\]
</dt> <dd>

An array that contains the supported operations for the replication type.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

**Abort** (2)


</dt> <dd></dd> <dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

**Activate Consistency** (3)


</dt> <dd></dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

**Activate** (4)


</dt> <dd></dd> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>

**AddSyncPair** (5)


</dt> <dd></dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

**Deactivate Consistency** (6)


</dt> <dd></dd> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>

**Deactivate** (7)


</dt> <dd></dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

**Detach** (8)


</dt> <dd></dd> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>

**Dissolve** (9)


</dt> <dd></dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

**Failover** (10)


</dt> <dd></dd> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>

**Failback** (11)


</dt> <dd></dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

**Fracture** (12)


</dt> <dd></dd> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>

**RemoveSyncPair** (13)


</dt> <dd></dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

**Resync Replica** (14)


</dt> <dd></dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

**Restore from Replica** (15)


</dt> <dd></dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

**Resume** (16)


</dt> <dd></dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

**Reset To Sync** (17)


</dt> <dd></dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

**Reset To Async** (18)


</dt> <dd></dd> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>

**Return To ResourcePool** (19)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>

**Reverse Roles** (20)


</dt> <dd></dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

**Split** (21)


</dt> <dd></dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

**Suspend** (22)


</dt> <dd></dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

**Unprepare** (23)


</dt> <dd></dd> <dt>

<span id="Prepare"></span><span id="prepare"></span><span id="PREPARE"></span>

**Prepare** (24)


</dt> <dd></dd> <dt>

<span id="Reset_To_Adaptive"></span><span id="reset_to_adaptive"></span><span id="RESET_TO_ADAPTIVE"></span>

**Reset To Adaptive** (25)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate the SMI-S provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate the SMI-S provider.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

When this method returns, this parameter contains a [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains detailed status information about the results of this operation.

</dd> </dl>

## Return value

The possible values are:

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 ...)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMReplicationCapabilities**](msft-smreplicationcapabilities.md)
</dt> </dl>

 

 





