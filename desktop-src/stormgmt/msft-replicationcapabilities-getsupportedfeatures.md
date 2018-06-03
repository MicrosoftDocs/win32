---
title: GetSupportedFeatures method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported features.
ms.assetid: 0DA00822-1931-47CA-874E-6192895F5124
keywords:
- GetSupportedFeatures method Windows Storage Management API
- GetSupportedFeatures method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedFeatures method
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities.GetSupportedFeatures
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedFeatures method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported features.

## Syntax


```mof
UInt32 GetSupportedFeatures(
  [in]  UInt16 ReplicationType,
  [out] UInt16 Features[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

</dd> <dt>

*Features* \[out\]
</dt> <dd>

An array of supported features.

<dl> <dt>

<span id="Replication_groups"></span><span id="replication_groups"></span><span id="REPLICATION_GROUPS"></span>**Replication groups** (2)
</dt> <dt>

<span id="Multi-hop_element_replication"></span><span id="multi-hop_element_replication"></span><span id="MULTI-HOP_ELEMENT_REPLICATION"></span>**Multi-hop element replication** (3)
</dt> <dt>

<span id="Multi-hop_elements_must_have_same_SyncType"></span><span id="multi-hop_elements_must_have_same_synctype"></span><span id="MULTI-HOP_ELEMENTS_MUST_HAVE_SAME_SYNCTYPE"></span>**Multi-hop elements must have same SyncType** (4)
</dt> <dt>

<span id="Multi-hop_requires_advance_notice"></span><span id="multi-hop_requires_advance_notice"></span><span id="MULTI-HOP_REQUIRES_ADVANCE_NOTICE"></span>**Multi-hop requires advance notice** (5)
</dt> <dt>

<span id="Requires_full_discovery_of_target_ComputerSystem"></span><span id="requires_full_discovery_of_target_computersystem"></span><span id="REQUIRES_FULL_DISCOVERY_OF_TARGET_COMPUTERSYSTEM"></span>**Requires full discovery of target ComputerSystem** (6)
</dt> <dt>

<span id="Service_suspends_source_I_O_when_necessary"></span><span id="service_suspends_source_i_o_when_necessary"></span><span id="SERVICE_SUSPENDS_SOURCE_I_O_WHEN_NECESSARY"></span>**Service suspends source I/O when necessary** (7)
</dt> <dt>

<span id="Targets_allocated_from_any_storage_pool"></span><span id="targets_allocated_from_any_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_ANY_STORAGE_POOL"></span>**Targets allocated from any storage pool** (8)
</dt> <dt>

<span id="Targets_allocated_from_shared_storage_pool"></span><span id="targets_allocated_from_shared_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_SHARED_STORAGE_POOL"></span>**Targets allocated from shared storage pool** (9)
</dt> <dt>

<span id="Targets_allocated_from_exclusive_storage_pool"></span><span id="targets_allocated_from_exclusive_storage_pool"></span><span id="TARGETS_ALLOCATED_FROM_EXCLUSIVE_STORAGE_POOL"></span>**Targets allocated from exclusive storage pool** (10)
</dt> <dt>

<span id="Targets_allocated_from_multiple_storage_pools"></span><span id="targets_allocated_from_multiple_storage_pools"></span><span id="TARGETS_ALLOCATED_FROM_MULTIPLE_STORAGE_POOLS"></span>**Targets allocated from multiple storage pools** (11)
</dt> <dt>

<span id="Targets_require_reserved_elements"></span><span id="targets_require_reserved_elements"></span><span id="TARGETS_REQUIRE_RESERVED_ELEMENTS"></span>**Targets require reserved elements** (12)
</dt> <dt>

<span id="Target_is_associated_to_SynchronizationAspect"></span><span id="target_is_associated_to_synchronizationaspect"></span><span id="TARGET_IS_ASSOCIATED_TO_SYNCHRONIZATIONASPECT"></span>**Target is associated to SynchronizationAspect** (13)
</dt> <dt>

<span id="Source_is_associated_to_SynchronizationAspect"></span><span id="source_is_associated_to_synchronizationaspect"></span><span id="SOURCE_IS_ASSOCIATED_TO_SYNCHRONIZATIONASPECT"></span>**Source is associated to SynchronizationAspect** (14)
</dt> <dt>

<span id="Error_recovery_from_Broken_state_Automatic"></span><span id="error_recovery_from_broken_state_automatic"></span><span id="ERROR_RECOVERY_FROM_BROKEN_STATE_AUTOMATIC"></span>**Error recovery from Broken state Automatic** (15)
</dt> <dt>

<span id="Target_must_remain_associated_to_source"></span><span id="target_must_remain_associated_to_source"></span><span id="TARGET_MUST_REMAIN_ASSOCIATED_TO_SOURCE"></span>**Target must remain associated to source** (16)
</dt> <dt>

<span id="Remote_resource_requires_remote_CIMOM"></span><span id="remote_resource_requires_remote_cimom"></span><span id="REMOTE_RESOURCE_REQUIRES_REMOTE_CIMOM"></span>**Remote resource requires remote CIMOM** (17)
</dt> <dt>

<span id="Synchronized_clone_target_detaches_automatically"></span><span id="synchronized_clone_target_detaches_automatically"></span><span id="SYNCHRONIZED_CLONE_TARGET_DETACHES_AUTOMATICALLY"></span>**Synchronized clone target detaches automatically** (18)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_read_only_source"></span><span id="reverse_roles_operation_requires_read_only_source"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_READ_ONLY_SOURCE"></span>**Reverse Roles operation requires read only source** (19)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_subsequent_resync"></span><span id="reverse_roles_operation_requires_subsequent_resync"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SUBSEQUENT_RESYNC"></span>**Reverse Roles operation requires subsequent resync** (20)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_fracture"></span><span id="restore_operation_requires_subsequent_fracture"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_FRACTURE"></span>**Restore operation requires subsequent fracture** (21)
</dt> <dt>

<span id="Resync_operation_requires_subsequent_activate"></span><span id="resync_operation_requires_subsequent_activate"></span><span id="RESYNC_OPERATION_REQUIRES_SUBSEQUENT_ACTIVATE"></span>**Resync operation requires subsequent activate** (22)
</dt> <dt>

<span id="Copy_operation_requires_offline_source"></span><span id="copy_operation_requires_offline_source"></span><span id="COPY_OPERATION_REQUIRES_OFFLINE_SOURCE"></span>**Copy operation requires offline source** (23)
</dt> <dt>

<span id="Adjustable_CopyPriority"></span><span id="adjustable_copypriority"></span><span id="ADJUSTABLE_COPYPRIORITY"></span>**Adjustable CopyPriority** (24)
</dt> <dt>

<span id="Source_requires_reserved_element"></span><span id="source_requires_reserved_element"></span><span id="SOURCE_REQUIRES_RESERVED_ELEMENT"></span>**Source requires reserved element** (25)
</dt> <dt>

<span id="Supports_undiscovered_resources"></span><span id="supports_undiscovered_resources"></span><span id="SUPPORTS_UNDISCOVERED_RESOURCES"></span>**Supports undiscovered resources** (26)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_detach"></span><span id="restore_operation_requires_subsequent_detach"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_DETACH"></span>**Restore operation requires subsequent detach** (27)
</dt> <dt>

<span id="Target_element_can_be_added_to_collections"></span><span id="target_element_can_be_added_to_collections"></span><span id="TARGET_ELEMENT_CAN_BE_ADDED_TO_COLLECTIONS"></span>**Target element can be added to collections** (28)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Synchronized_state"></span><span id="reverse_roles_operation_requires_synchronized_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SYNCHRONIZED_STATE"></span>**Reverse Roles operation requires Synchronized state** (29)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Fractured_state"></span><span id="reverse_roles_operation_requires_fractured_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_FRACTURED_STATE"></span>**Reverse Roles operation requires Fractured state** (30)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Split_state"></span><span id="reverse_roles_operation_requires_split_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SPLIT_STATE"></span>**Reverse Roles operation requires Split state** (31)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_FailedOver_state"></span><span id="reverse_roles_operation_requires_failedover_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_FAILEDOVER_STATE"></span>**Reverse Roles operation requires FailedOver state** (32)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Suspended_state"></span><span id="reverse_roles_operation_requires_suspended_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SUSPENDED_STATE"></span>**Reverse Roles operation requires Suspended state** (33)
</dt> <dt>

<span id="Provider_can_manage_remote_source"></span><span id="provider_can_manage_remote_source"></span><span id="PROVIDER_CAN_MANAGE_REMOTE_SOURCE"></span>**Provider can manage remote source** (34)
</dt> <dt>

<span id="Provider_can_manage_remote_target"></span><span id="provider_can_manage_remote_target"></span><span id="PROVIDER_CAN_MANAGE_REMOTE_TARGET"></span>**Provider can manage remote target** (35)
</dt> <dt>

<span id="Supports_temporary_ReplicationEntity"></span><span id="supports_temporary_replicationentity"></span><span id="SUPPORTS_TEMPORARY_REPLICATIONENTITY"></span>**Supports temporary ReplicationEntity** (36)
</dt> <dt>

<span id="Supports_persistent_ReplicationEntity"></span><span id="supports_persistent_replicationentity"></span><span id="SUPPORTS_PERSISTENT_REPLICATIONENTITY"></span>**Supports persistent ReplicationEntity** (37)
</dt> <dt>

<span id="ReplicationEntity_supports_embedded_instance"></span><span id="replicationentity_supports_embedded_instance"></span><span id="REPLICATIONENTITY_SUPPORTS_EMBEDDED_INSTANCE"></span>**ReplicationEntity supports embedded instance** (38)
</dt> <dt>

<span id="TargetElement_shall_not_be_supplied"></span><span id="targetelement_shall_not_be_supplied"></span><span id="TARGETELEMENT_SHALL_NOT_BE_SUPPLIED"></span>**TargetElement shall not be supplied** (39)
</dt> <dt>

<span id="TargetPool_shall_not_be_supplied"></span><span id="targetpool_shall_not_be_supplied"></span><span id="TARGETPOOL_SHALL_NOT_BE_SUPPLIED"></span>**TargetPool shall not be supplied** (40)
</dt> <dt>

<span id="TargetGoal_shall_not_be_supplied"></span><span id="targetgoal_shall_not_be_supplied"></span><span id="TARGETGOAL_SHALL_NOT_BE_SUPPLIED"></span>**TargetGoal shall not be supplied** (41)
</dt> <dt>

<span id="Provider_can_create_remote_elements"></span><span id="provider_can_create_remote_elements"></span><span id="PROVIDER_CAN_CREATE_REMOTE_ELEMENTS"></span>**Provider can create remote elements** (42)
</dt> <dt>

<span id="Creating_remote_elements_requires_TargetPool"></span><span id="creating_remote_elements_requires_targetpool"></span><span id="CREATING_REMOTE_ELEMENTS_REQUIRES_TARGETPOOL"></span>**Creating remote elements requires TargetPool** (43)
</dt> <dt>

<span id="Local_targets_allocated_from_sources_resource_pool"></span><span id="local_targets_allocated_from_sources_resource_pool"></span><span id="LOCAL_TARGETS_ALLOCATED_FROM_SOURCES_RESOURCE_POOL"></span>**Local targets allocated from sources resource pool** (44)
</dt> <dt>

<span id="Supports_SynchronizationAspect"></span><span id="supports_synchronizationaspect"></span><span id="SUPPORTS_SYNCHRONIZATIONASPECT"></span>**Supports SynchronizationAspect** (45)
</dt> <dt>

<span id="Accepts_foreign_object_paths"></span><span id="accepts_foreign_object_paths"></span><span id="ACCEPTS_FOREIGN_OBJECT_PATHS"></span>**Accepts foreign object paths** (46)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_fracture"></span><span id="failover_operation_requires_subsequent_fracture"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_FRACTURE"></span>**Failover operation requires subsequent fracture** (47)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_split"></span><span id="failover_operation_requires_subsequent_split"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_SPLIT"></span>**Failover operation requires subsequent split** (48)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_resume"></span><span id="restore_operation_requires_subsequent_resume"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_RESUME"></span>**Restore operation requires subsequent resume** (49)
</dt> <dt>

<span id="GetPeerSystems_can_return_access_points"></span><span id="getpeersystems_can_return_access_points"></span><span id="GETPEERSYSTEMS_CAN_RETURN_ACCESS_POINTS"></span>**GetPeerSystems can return access points** (50)
</dt> <dt>

<span id="Client_can_supply_target_ElementName"></span><span id="client_can_supply_target_elementname"></span><span id="CLIENT_CAN_SUPPLY_TARGET_ELEMENTNAME"></span>**Client can supply target ElementName** (51)
</dt> <dt>

<span id="Reverse_Roles_operation_does_not_change_CopyState"></span><span id="reverse_roles_operation_does_not_change_copystate"></span><span id="REVERSE_ROLES_OPERATION_DOES_NOT_CHANGE_COPYSTATE"></span>**Reverse Roles operation does not change CopyState** (52)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_failback"></span><span id="failover_operation_requires_subsequent_failback"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_FAILBACK"></span>**Failover operation requires subsequent failback** (53)
</dt> <dt>

<span id="Planned_Failover_operation_requires_fractured_state"></span><span id="planned_failover_operation_requires_fractured_state"></span><span id="PLANNED_FAILOVER_OPERATION_REQUIRES_FRACTURED_STATE"></span>**Planned Failover operation requires fractured state** (54)
</dt> <dt>

<span id="Target_element_requires_resource_pool_reserved_for_replication"></span><span id="target_element_requires_resource_pool_reserved_for_replication"></span><span id="TARGET_ELEMENT_REQUIRES_RESOURCE_POOL_RESERVED_FOR_REPLICATION"></span>**Target element requires resource pool reserved for replication** (55)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..0xFFFF)
</dt> </dl> </dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (0x8000..)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> </dl>

 

 





