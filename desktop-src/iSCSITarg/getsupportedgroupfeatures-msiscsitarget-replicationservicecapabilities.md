---
title: GetSupportedGroupFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the supported group features for a specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c9240c5d-1185-4996-bbc0-114824bac9d9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedGroupFeatures method iSCSI Software Target API", "GetSupportedGroupFeatures method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedGroupFeatures method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedGroupFeatures
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSupportedGroupFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the supported group features for a specified replication type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedGroupFeatures(
  [in]  uint16 ReplicationType,
  [out] uint16 GroupFeatures[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Specifies the replication type.

The [**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md).**SupportedReplicationTypes** property values are.

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


</dt> <dd>14–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*GroupFeatures* \[out\]
</dt> <dd>

On return, contains a list of the supported group features.

The possible values are.

<dt>

<span id="One-to-many_replication"></span><span id="one-to-many_replication"></span><span id="ONE-TO-MANY_REPLICATION"></span>

**One-to-many replication** (2)


</dt> <dd></dd> <dt>

<span id="Many-to-many_groups"></span><span id="many-to-many_groups"></span><span id="MANY-TO-MANY_GROUPS"></span>

**Many-to-many groups** (3)


</dt> <dd></dd> <dt>

<span id="Consistency_enabled_for_all_groups"></span><span id="consistency_enabled_for_all_groups"></span><span id="CONSISTENCY_ENABLED_FOR_ALL_GROUPS"></span>

**Consistency enabled for all groups** (4)


</dt> <dd></dd> <dt>

<span id="Empty_replication_groups_allowed"></span><span id="empty_replication_groups_allowed"></span><span id="EMPTY_REPLICATION_GROUPS_ALLOWED"></span>

**Empty replication groups allowed** (5)


</dt> <dd></dd> <dt>

<span id="Source_group_must_have_more_than_one_element"></span><span id="source_group_must_have_more_than_one_element"></span><span id="SOURCE_GROUP_MUST_HAVE_MORE_THAN_ONE_ELEMENT"></span>

**Source group must have more than one element** (6)


</dt> <dd></dd> <dt>

<span id="Composite_Groups"></span><span id="composite_groups"></span><span id="COMPOSITE_GROUPS"></span>

**Composite Groups** (7)


</dt> <dd></dd> <dt>

<span id="Multihop_element_replication"></span><span id="multihop_element_replication"></span><span id="MULTIHOP_ELEMENT_REPLICATION"></span>

**Multihop element replication** (8)


</dt> <dd></dd> <dt>

<span id="Multihop_elements_must_have_same_SyncType"></span><span id="multihop_elements_must_have_same_synctype"></span><span id="MULTIHOP_ELEMENTS_MUST_HAVE_SAME_SYNCTYPE"></span>

**Multihop elements must have same SyncType** (9)


</dt> <dd></dd> <dt>

<span id="Group_can_only_have_one_single_relationship_active"></span><span id="group_can_only_have_one_single_relationship_active"></span><span id="GROUP_CAN_ONLY_HAVE_ONE_SINGLE_RELATIONSHIP_ACTIVE"></span>

**Group can only have one single relationship active** (10)


</dt> <dd></dd> <dt>

<span id="Source_element_can_be_removed_from_group"></span><span id="source_element_can_be_removed_from_group"></span><span id="SOURCE_ELEMENT_CAN_BE_REMOVED_FROM_GROUP"></span>

**Source element can be removed from group** (11)


</dt> <dd></dd> <dt>

<span id="Target_element_can_be_removed_from_group"></span><span id="target_element_can_be_removed_from_group"></span><span id="TARGET_ELEMENT_CAN_BE_REMOVED_FROM_GROUP"></span>

**Target element can be removed from group** (12)


</dt> <dd></dd> <dt>

<span id="Group_can_be_temporary"></span><span id="group_can_be_temporary"></span><span id="GROUP_CAN_BE_TEMPORARY"></span>

**Group can be temporary** (13)


</dt> <dd></dd> <dt>

<span id="Group_is_nameable"></span><span id="group_is_nameable"></span><span id="GROUP_IS_NAMEABLE"></span>

**Group is nameable** (14)


</dt> <dd></dd> <dt>

<span id="Supports_target_element_count"></span><span id="supports_target_element_count"></span><span id="SUPPORTS_TARGET_ELEMENT_COUNT"></span>

**Supports target element count** (15)


</dt> <dd></dd> <dt>

<span id="Synchronized_clone_target_detaches_automatically"></span><span id="synchronized_clone_target_detaches_automatically"></span><span id="SYNCHRONIZED_CLONE_TARGET_DETACHES_AUTOMATICALLY"></span>

**Synchronized clone target detaches automatically** (16)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles_operation_requires_Read_Only_source"></span><span id="reverse_roles_operation_requires_read_only_source"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_READ_ONLY_SOURCE"></span>

**Reverse Roles operation requires Read Only source** (17)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles_operation_requires_resync"></span><span id="reverse_roles_operation_requires_resync"></span><span id="REVERSE_ROLES_OPERATION_REQUIRES_RESYNC"></span>

**Reverse Roles operation requires resync** (18)


</dt> <dd></dd> <dt>

<span id="Restore_operation_requires_fracture"></span><span id="restore_operation_requires_fracture"></span><span id="RESTORE_OPERATION_REQUIRES_FRACTURE"></span>

**Restore operation requires fracture** (19)


</dt> <dd></dd> <dt>

<span id="Resync_operation_requires_activate"></span><span id="resync_operation_requires_activate"></span><span id="RESYNC_OPERATION_REQUIRES_ACTIVATE"></span>

**Resync operation requires activate** (20)


</dt> <dd></dd> <dt>

<span id="Copy_operation_requires_offline_source"></span><span id="copy_operation_requires_offline_source"></span><span id="COPY_OPERATION_REQUIRES_OFFLINE_SOURCE"></span>

**Copy operation requires offline source** (21)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>22–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> </dl>

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

**DMTF Reserved** (7–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> </dl>

 

 





