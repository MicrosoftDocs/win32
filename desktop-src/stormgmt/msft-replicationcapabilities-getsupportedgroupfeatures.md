---
title: GetSupportedGroupFeatures method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported group features.
ms.assetid: 'A7037D94-1196-4F10-9084-F797A75C7C8D'
keywords: ["GetSupportedGroupFeatures method Windows Storage Management API", "GetSupportedGroupFeatures method Windows Storage Management API , MSFT_ReplicationCapabilities class", "MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedGroupFeatures method"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities.GetSupportedGroupFeatures
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetSupportedGroupFeatures method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported group features.

## Syntax


```mof
UInt32 GetSupportedGroupFeatures(
  [in]  UInt16 ReplicationType,
  [out] UInt16 Features[],
  [out] String ExtendedStatus
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

<span id="One-to-many_replication"></span><span id="one-to-many_replication"></span><span id="ONE-TO-MANY_REPLICATION"></span>**One-to-many replication** (2)
</dt> <dt>

<span id="Many-to-many_groups"></span><span id="many-to-many_groups"></span><span id="MANY-TO-MANY_GROUPS"></span>**Many-to-many groups** (3)
</dt> <dt>

<span id="Consistency_enabled_for_all_groups"></span><span id="consistency_enabled_for_all_groups"></span><span id="CONSISTENCY_ENABLED_FOR_ALL_GROUPS"></span>**Consistency enabled for all groups** (4)
</dt> <dt>

<span id="Empty_replication_groups_allowed"></span><span id="empty_replication_groups_allowed"></span><span id="EMPTY_REPLICATION_GROUPS_ALLOWED"></span>**Empty replication groups allowed** (5)
</dt> <dt>

<span id="Source_group_must_have_more_than_one_element"></span><span id="source_group_must_have_more_than_one_element"></span><span id="SOURCE_GROUP_MUST_HAVE_MORE_THAN_ONE_ELEMENT"></span>**Source group must have more than one element** (6)
</dt> <dt>

<span id="Composite_groups"></span><span id="composite_groups"></span><span id="COMPOSITE_GROUPS"></span>**Composite groups** (7)
</dt> <dt>

<span id="Multihop_element_replication"></span><span id="multihop_element_replication"></span><span id="MULTIHOP_ELEMENT_REPLICATION"></span>**Multihop element replication** (8)
</dt> <dt>

<span id="Multi-hop_elements_must_have_same_SyncType"></span><span id="multi-hop_elements_must_have_same_synctype"></span><span id="MULTI-HOP_ELEMENTS_MUST_HAVE_SAME_SYNCTYPE"></span>**Multi-hop elements must have same SyncType** (9)
</dt> <dt>

<span id="Group_can_only_have_one_single_relationship_active"></span><span id="group_can_only_have_one_single_relationship_active"></span><span id="GROUP_CAN_ONLY_HAVE_ONE_SINGLE_RELATIONSHIP_ACTIVE"></span>**Group can only have one single relationship active** (10)
</dt> <dt>

<span id="Source_element_can_be_removed_from_group"></span><span id="source_element_can_be_removed_from_group"></span><span id="SOURCE_ELEMENT_CAN_BE_REMOVED_FROM_GROUP"></span>**Source element can be removed from group** (11)
</dt> <dt>

<span id="Target_element_can_be_removed_from_group"></span><span id="target_element_can_be_removed_from_group"></span><span id="TARGET_ELEMENT_CAN_BE_REMOVED_FROM_GROUP"></span>**Target element can be removed from group** (12)
</dt> <dt>

<span id="Group_can_be_temporary"></span><span id="group_can_be_temporary"></span><span id="GROUP_CAN_BE_TEMPORARY"></span>**Group can be temporary** (13)
</dt> <dt>

<span id="Group_is_nameable"></span><span id="group_is_nameable"></span><span id="GROUP_IS_NAMEABLE"></span>**Group is nameable** (14)
</dt> <dt>

<span id="Supports_target_element_count"></span><span id="supports_target_element_count"></span><span id="SUPPORTS_TARGET_ELEMENT_COUNT"></span>**Supports target element count** (15)
</dt> <dt>

<span id="Synchronized_clone_target_detaches_automatically"></span><span id="synchronized_clone_target_detaches_automatically"></span><span id="SYNCHRONIZED_CLONE_TARGET_DETACHES_AUTOMATICALLY"></span>**Synchronized clone target detaches automatically** (16)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_read_only_source"></span><span id="reverse_roles_operation_requires_read_only_source"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_READ_ONLY_SOURCE"></span>**Reverse Roles operation requires read only source** (17)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_subsequent_resync"></span><span id="reverse_roles_operation_requires_subsequent_resync"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SUBSEQUENT_RESYNC"></span>**Reverse Roles operation requires subsequent resync** (18)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_fracture"></span><span id="restore_operation_requires_subsequent_fracture"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_FRACTURE"></span>**Restore operation requires subsequent fracture** (19)
</dt> <dt>

<span id="Resync_operation_requires_subsequent_activate"></span><span id="resync_operation_requires_subsequent_activate"></span><span id="RESYNC_OPERATION_REQUIRES_SUBSEQUENT_ACTIVATE"></span>**Resync operation requires subsequent activate** (20)
</dt> <dt>

<span id="Copy_operation_requires_offline_source"></span><span id="copy_operation_requires_offline_source"></span><span id="COPY_OPERATION_REQUIRES_OFFLINE_SOURCE"></span>**Copy operation requires offline source** (21)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_detach"></span><span id="restore_operation_requires_subsequent_detach"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_DETACH"></span>**Restore operation requires subsequent detach** (22)
</dt> <dt>

<span id="Element_can_be_member_of_multiple_groups"></span><span id="element_can_be_member_of_multiple_groups"></span><span id="ELEMENT_CAN_BE_MEMBER_OF_MULTIPLE_GROUPS"></span>**Element can be member of multiple groups** (23)
</dt> <dt>

<span id="Elements_of_group_can_be_mix_of_thin_and_thick"></span><span id="elements_of_group_can_be_mix_of_thin_and_thick"></span><span id="ELEMENTS_OF_GROUP_CAN_BE_MIX_OF_THIN_AND_THICK"></span>**Elements of group can be mix of thin and thick** (24)
</dt> <dt>

<span id="TokenizedClone_ConsistentPointInTime"></span><span id="tokenizedclone_consistentpointintime"></span><span id="TOKENIZEDCLONE_CONSISTENTPOINTINTIME"></span>**TokenizedClone ConsistentPointInTime** (25)
</dt> <dt>

<span id="Target_elements_can_be_added_to_collections"></span><span id="target_elements_can_be_added_to_collections"></span><span id="TARGET_ELEMENTS_CAN_BE_ADDED_TO_COLLECTIONS"></span>**Target elements can be added to collections** (26)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Synchronized_state"></span><span id="reverse_roles_operation_requires_synchronized_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SYNCHRONIZED_STATE"></span>**Reverse Roles operation requires Synchronized state** (27)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Fractured_state"></span><span id="reverse_roles_operation_requires_fractured_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_FRACTURED_STATE"></span>**Reverse Roles operation requires Fractured state** (28)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Split_state"></span><span id="reverse_roles_operation_requires_split_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SPLIT_STATE"></span>**Reverse Roles operation requires Split state** (29)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_FailedOver_state"></span><span id="reverse_roles_operation_requires_failedover_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_FAILEDOVER_STATE"></span>**Reverse Roles operation requires FailedOver state** (30)
</dt> <dt>

<span id="Reverse_Roles_operation_requires_Suspended_state"></span><span id="reverse_roles_operation_requires_suspended_state"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_SUSPENDED_STATE"></span>**Reverse Roles operation requires Suspended state** (31)
</dt> <dt>

<span id="Provider_can_manage_remote_source_group"></span><span id="provider_can_manage_remote_source_group"></span><span id="PROVIDER_CAN_MANAGE_REMOTE_SOURCE_GROUP"></span>**Provider can manage remote source group** (32)
</dt> <dt>

<span id="Provider_can_manage_remote_target_group"></span><span id="provider_can_manage_remote_target_group"></span><span id="PROVIDER_CAN_MANAGE_REMOTE_TARGET_GROUP"></span>**Provider can manage remote target group** (33)
</dt> <dt>

<span id="TargetGroup_shall_not_be_supplied"></span><span id="targetgroup_shall_not_be_supplied"></span><span id="TARGETGROUP_SHALL_NOT_BE_SUPPLIED"></span>**TargetGroup shall not be supplied** (34)
</dt> <dt>

<span id="TargetPool_shall_not_be_supplied"></span><span id="targetpool_shall_not_be_supplied"></span><span id="TARGETPOOL_SHALL_NOT_BE_SUPPLIED"></span>**TargetPool shall not be supplied** (35)
</dt> <dt>

<span id="TargetSettingGoal_shall_not_be_supplied"></span><span id="targetsettinggoal_shall_not_be_supplied"></span><span id="TARGETSETTINGGOAL_SHALL_NOT_BE_SUPPLIED"></span>**TargetSettingGoal shall not be supplied** (36)
</dt> <dt>

<span id="Provider_can_create_remote_target_group"></span><span id="provider_can_create_remote_target_group"></span><span id="PROVIDER_CAN_CREATE_REMOTE_TARGET_GROUP"></span>**Provider can create remote target group** (37)
</dt> <dt>

<span id="Provider_can_create_local_target_group"></span><span id="provider_can_create_local_target_group"></span><span id="PROVIDER_CAN_CREATE_LOCAL_TARGET_GROUP"></span>**Provider can create local target group** (38)
</dt> <dt>

<span id="Provider_must_create_remote_group"></span><span id="provider_must_create_remote_group"></span><span id="PROVIDER_MUST_CREATE_REMOTE_GROUP"></span>**Provider must create remote group** (39)
</dt> <dt>

<span id="Creating_remote_elements_requires_TargetPool"></span><span id="creating_remote_elements_requires_targetpool"></span><span id="CREATING_REMOTE_ELEMENTS_REQUIRES_TARGETPOOL"></span>**Creating remote elements requires TargetPool** (40)
</dt> <dt>

<span id="Target_group_shall_be_supplied"></span><span id="target_group_shall_be_supplied"></span><span id="TARGET_GROUP_SHALL_BE_SUPPLIED"></span>**Target group shall be supplied** (41)
</dt> <dt>

<span id="CreateGroupReplica_only_accepts_empty_groups"></span><span id="creategroupreplica_only_accepts_empty_groups"></span><span id="CREATEGROUPREPLICA_ONLY_ACCEPTS_EMPTY_GROUPS"></span>**CreateGroupReplica only accepts empty groups** (42)
</dt> <dt>

<span id="One_replication_group_per_storage_pool"></span><span id="one_replication_group_per_storage_pool"></span><span id="ONE_REPLICATION_GROUP_PER_STORAGE_POOL"></span>**One replication group per storage pool** (43)
</dt> <dt>

<span id="Supports_ConsistencyExempt_when_adding_to_group"></span><span id="supports_consistencyexempt_when_adding_to_group"></span><span id="SUPPORTS_CONSISTENCYEXEMPT_WHEN_ADDING_TO_GROUP"></span>**Supports ConsistencyExempt when adding to group** (44)
</dt> <dt>

<span id="Add_or_Remove_to_group_requires_Fractured_state"></span><span id="add_or_remove_to_group_requires_fractured_state"></span><span id="ADD_OR_REMOVE_TO_GROUP_REQUIRES_FRACTURED_STATE"></span>**Add or Remove to group requires Fractured state** (45)
</dt> <dt>

<span id="Add_or_Remove_to_group_requires_Split_state"></span><span id="add_or_remove_to_group_requires_split_state"></span><span id="ADD_OR_REMOVE_TO_GROUP_REQUIRES_SPLIT_STATE"></span>**Add or Remove to group requires Split state** (46)
</dt> <dt>

<span id="Add_or_Remove_to_group_requires_Suspended_state"></span><span id="add_or_remove_to_group_requires_suspended_state"></span><span id="ADD_OR_REMOVE_TO_GROUP_REQUIRES_SUSPENDED_STATE"></span>**Add or Remove to group requires Suspended state** (47)
</dt> <dt>

<span id="Add_or_Remove_to_group_requires_FailedOver_state"></span><span id="add_or_remove_to_group_requires_failedover_state"></span><span id="ADD_OR_REMOVE_TO_GROUP_REQUIRES_FAILEDOVER_STATE"></span>**Add or Remove to group requires FailedOver state** (48)
</dt> <dt>

<span id="Supports_SynchronizationAspect_of_replication_group"></span><span id="supports_synchronizationaspect_of_replication_group"></span><span id="SUPPORTS_SYNCHRONIZATIONASPECT_OF_REPLICATION_GROUP"></span>**Supports SynchronizationAspect of replication group** (49)
</dt> <dt>

<span id="No_element_level_StorageSynchronized"></span><span id="no_element_level_storagesynchronized"></span><span id="NO_ELEMENT_LEVEL_STORAGESYNCHRONIZED"></span>**No element level StorageSynchronized** (50)
</dt> <dt>

<span id="Accepts_foreign_object_paths"></span><span id="accepts_foreign_object_paths"></span><span id="ACCEPTS_FOREIGN_OBJECT_PATHS"></span>**Accepts foreign object paths** (51)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_fracture"></span><span id="failover_operation_requires_subsequent_fracture"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_FRACTURE"></span>**Failover operation requires subsequent fracture** (52)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_split"></span><span id="failover_operation_requires_subsequent_split"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_SPLIT"></span>**Failover operation requires subsequent split** (53)
</dt> <dt>

<span id="Restore_operation_requires_subsequent_resume"></span><span id="restore_operation_requires_subsequent_resume"></span><span id="RESTORE_OPERATION_REQUIRES_SUBSEQUENT_RESUME"></span>**Restore operation requires subsequent resume** (54)
</dt> <dt>

<span id="One_consistent_async_per_RemoteReplicationCollection"></span><span id="one_consistent_async_per_remotereplicationcollection"></span><span id="ONE_CONSISTENT_ASYNC_PER_REMOTEREPLICATIONCOLLECTION"></span>**One consistent async per RemoteReplicationCollection** (55)
</dt> <dt>

<span id="Client_can_supply_RelationshipName"></span><span id="client_can_supply_relationshipname"></span><span id="CLIENT_CAN_SUPPLY_RELATIONSHIPNAME"></span>**Client can supply RelationshipName** (56)
</dt> <dt>

<span id="Implementation_decides_group_member_order"></span><span id="implementation_decides_group_member_order"></span><span id="IMPLEMENTATION_DECIDES_GROUP_MEMBER_ORDER"></span>**Implementation decides group member order** (57)
</dt> <dt>

<span id="Reverse_Roles_operation_does_not_change_CopyState"></span><span id="reverse_roles_operation_does_not_change_copystate"></span><span id="REVERSE_ROLES_OPERATION_DOES_NOT_CHANGE_COPYSTATE"></span>**Reverse Roles operation does not change CopyState** (58)
</dt> <dt>

<span id="Failover_operation_requires_subsequent_failback"></span><span id="failover_operation_requires_subsequent_failback"></span><span id="FAILOVER_OPERATION_REQUIRES_SUBSEQUENT_FAILBACK"></span>**Failover operation requires subsequent failback** (59)
</dt> <dt>

<span id="Planned_Failover_operation_requires_split_state"></span><span id="planned_failover_operation_requires_split_state"></span><span id="PLANNED_FAILOVER_OPERATION_REQUIRES_SPLIT_STATE"></span>**Planned Failover operation requires split state** (60)
</dt> <dt>

<span id="Planned_Failover_operation_requires_fractured_state"></span><span id="planned_failover_operation_requires_fractured_state"></span><span id="PLANNED_FAILOVER_OPERATION_REQUIRES_FRACTURED_STATE"></span>**Planned Failover operation requires fractured state** (61)
</dt> <dt>

<span id="Target_element_requires_resource_pool_reserved_for_replication"></span><span id="target_element_requires_resource_pool_reserved_for_replication"></span><span id="TARGET_ELEMENT_REQUIRES_RESOURCE_POOL_RESERVED_FOR_REPLICATION"></span>**Target element requires resource pool reserved for replication** (62)
</dt> <dt>

<span id="AddSyncPair_requires_Synchronized_mirror_pair"></span><span id="addsyncpair_requires_synchronized_mirror_pair"></span><span id="ADDSYNCPAIR_REQUIRES_SYNCHRONIZED_MIRROR_PAIR"></span>**AddSyncPair requires Synchronized mirror pair** (63)
</dt> <dt>

<span id="Provider_can_create_remote_elements_using_TargetPools"></span><span id="provider_can_create_remote_elements_using_targetpools"></span><span id="PROVIDER_CAN_CREATE_REMOTE_ELEMENTS_USING_TARGETPOOLS"></span>**Provider can create remote elements using TargetPools** (64)
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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> </dl>

 

 





