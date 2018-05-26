---
title: GetSupportedFeatures method of the CIM\_ReplicationService class
description: Retrieves the supported copy states for a specified replication type and indicates if the target element is host accessible for each copy state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c3102d1-b537-421b-baba-124e4d690150
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedFeatures method iSCSI Software Target API
- GetSupportedFeatures method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , GetSupportedFeatures method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.GetSupportedFeatures
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedFeatures method of the CIM\_ReplicationService class

Retrieves the supported copy states for a specified replication type and indicates if the target element is host accessible for each copy state.

## Syntax


```mof
uint32 GetSupportedFeatures(
  [in]  uint16 ReplicationType,
  [out] uint16 Features[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Specifies the replication type.

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Features* \[out\]
</dt> <dd>

On return, contains the supported features.

The possible values are.

<dt>

<span id="Replication_groups"></span><span id="replication_groups"></span><span id="REPLICATION_GROUPS"></span>

**Replication groups** (2)


</dt> <dd></dd> <dt>

<span id="Multi-hop_element_replication"></span><span id="multi-hop_element_replication"></span><span id="MULTI-HOP_ELEMENT_REPLICATION"></span>

**Multi-hop element replication** (3)


</dt> <dd></dd> <dt>

<span id="Multi-hop_elements_must_have_same_SyncType"></span><span id="multi-hop_elements_must_have_same_synctype"></span><span id="MULTI-HOP_ELEMENTS_MUST_HAVE_SAME_SYNCTYPE"></span>

**Multi-hop elements must have same SyncType** (4)


</dt> <dd></dd> <dt>

<span id="Multi-hop_requires_advance_notice"></span><span id="multi-hop_requires_advance_notice"></span><span id="MULTI-HOP_REQUIRES_ADVANCE_NOTICE"></span>

**Multi-hop requires advance notice** (5)


</dt> <dd></dd> <dt>

<span id="Requires_full_discovery_of_target_ComputerSystem"></span><span id="requires_full_discovery_of_target_computersystem"></span><span id="REQUIRES_FULL_DISCOVERY_OF_TARGET_COMPUTERSYSTEM"></span>

**Requires full discovery of target ComputerSystem** (6)


</dt> <dd></dd> <dt>

<span id="Service_suspends_source_I_O_when_necessary"></span><span id="service_suspends_source_i_o_when_necessary"></span><span id="SERVICE_SUSPENDS_SOURCE_I_O_WHEN_NECESSARY"></span>

**Service suspends source I/O when necessary** (7)


</dt> <dd></dd> <dt>

<span id="Targets_allocated_from_Any_storage_pool"></span><span id="targets_allocated_from_any_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_ANY_STORAGE_POOL"></span>

**Targets allocated from Any storage pool** (8)


</dt> <dd></dd> <dt>

<span id="Targets_allocated_from_Shared_storage_pool"></span><span id="targets_allocated_from_shared_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_SHARED_STORAGE_POOL"></span>

**Targets allocated from Shared storage pool** (9)


</dt> <dd></dd> <dt>

<span id="Targets_allocated_from_Exclusive_storage_pool"></span><span id="targets_allocated_from_exclusive_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_EXCLUSIVE_STORAGE_POOL"></span>

**Targets allocated from Exclusive storage pool** (10)


</dt> <dd></dd> <dt>

<span id="Targets_allocated_from_Multiple_storage_pools"></span><span id="targets_allocated_from_multiple_storage_pools"></span><span id="TARGETS_ALLOCATED_FROM_MULTIPLE_STORAGE_POOLS"></span>

**Targets allocated from Multiple storage pools** (11)


</dt> <dd></dd> <dt>

<span id="Targets_require_reserved_elements"></span><span id="targets_require_reserved_elements"></span><span id="TARGETS_REQUIRE_RESERVED_ELEMENTS"></span>

**Targets require reserved elements** (12)


</dt> <dd></dd> <dt>

<span id="Target_is_associated_to_SynchronizationAspect"></span><span id="target_is_associated_to_synchronizationaspect"></span><span id="TARGET_IS_ASSOCIATED_TO_SYNCHRONIZATIONASPECT"></span>

**Target is associated to SynchronizationAspect** (13)


</dt> <dd></dd> <dt>

<span id="Source_is_associated_to_SynchronizationAspect"></span><span id="source_is_associated_to_synchronizationaspect"></span><span id="SOURCE_IS_ASSOCIATED_TO_SYNCHRONIZATIONASPECT"></span>

**Source is associated to SynchronizationAspect** (14)


</dt> <dd></dd> <dt>

<span id="Error_recovery_from_Broken_state_Automatic"></span><span id="error_recovery_from_broken_state_automatic"></span><span id="ERROR_RECOVERY_FROM_BROKEN_STATE_AUTOMATIC"></span>

**Error recovery from Broken state Automatic** (15)


</dt> <dd></dd> <dt>

<span id="Target_must_remain_associated_to_source"></span><span id="target_must_remain_associated_to_source"></span><span id="TARGET_MUST_REMAIN_ASSOCIATED_TO_SOURCE"></span>

**Target must remain associated to source** (16)


</dt> <dd></dd> <dt>

<span id="Remote_resource_requires_remote_CIMOM"></span><span id="remote_resource_requires_remote_cimom"></span><span id="REMOTE_RESOURCE_REQUIRES_REMOTE_CIMOM"></span>

**Remote resource requires remote CIMOM** (17)


</dt> <dd></dd> <dt>

<span id="Synchronized_clone_target_detaches_automatically"></span><span id="synchronized_clone_target_detaches_automatically"></span><span id="SYNCHRONIZED_CLONE_TARGET_DETACHES_AUTOMATICALLY"></span>

**Synchronized clone target detaches automatically** (18)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles_operation_requires_Read_Only_source"></span><span id="reverse_roles_operation_requires_read_only_source"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_READ_ONLY_SOURCE"></span>

**Reverse Roles operation requires Read Only source** (19)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles_operation_requires_resync"></span><span id="reverse_roles_operation_requires_resync"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_RESYNC"></span>

**Reverse Roles operation requires resync** (20)


</dt> <dd></dd> <dt>

<span id="Restore_operation_requires_fracture"></span><span id="restore_operation_requires_fracture"></span><span id="RESTORE_OPERATION_REQUIRES_FRACTURE"></span>

**Restore operation requires fracture** (21)


</dt> <dd></dd> <dt>

<span id="Resync_operation_requires_activate"></span><span id="resync_operation_requires_activate"></span><span id="RESYNC_OPERATION_REQUIRES_ACTIVATE"></span>

**Resync operation requires activate** (22)


</dt> <dd></dd> <dt>

<span id="Copy_operation_requires_offline_source"></span><span id="copy_operation_requires_offline_source"></span><span id="COPY_OPERATION_REQUIRES_OFFLINE_SOURCE"></span>

**Copy operation requires offline source** (23)


</dt> <dd></dd> <dt>

<span id="Adjustable_CopyPriority"></span><span id="adjustable_copypriority"></span><span id="ADJUSTABLE_COPYPRIORITY"></span>

**Adjustable CopyPriority** (24)


</dt> <dd></dd> <dt>

<span id="Source_requires_reserved_element"></span><span id="source_requires_reserved_element"></span><span id="SOURCE_REQUIRES_RESERVED_ELEMENT"></span>

**Source requires reserved element** (25)


</dt> <dd></dd> <dt>

<span id="Supports_undiscovered_resources"></span><span id="supports_undiscovered_resources"></span><span id="SUPPORTS_UNDISCOVERED_RESOURCES"></span>

**Supports undiscovered resources** (26)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>27 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 = *value* </dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

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

**Vendor Specific** (32768 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> </dl>

 

 





