---
title: GetSupportedGroupFeatures method of the CIM\_ReplicationServiceCapabilities class
description: This method, for a given ReplicationType, returns the supported group features.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'df6611d3-f289-4487-9f74-599949c7e157'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedGroupFeatures method iSCSI Software Target API", "GetSupportedGroupFeatures method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedGroupFeatures method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedGroupFeatures
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedGroupFeatures method of the CIM\_ReplicationServiceCapabilities class

This method, for a given ReplicationType, returns the supported group features.

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

A value representing the ReplicationType.

</dd> <dt>

*GroupFeatures* \[out\]
</dt> <dd>

An array of Supported Features.

One-to-many replication: One source element and multiple targets elements in a group.

Many-to-many: One or more elements in the source group and one or more elements in the target group.

Consistency enabled for all groups: All groups are considered consistent by default.

Empty replication groups allowed: A replication group can have zero elements.

Source group must have more than one element: A group with only one element is not allowed.

Composite Groups: Elements of a group may be from different arrays.

Multi-hop group replication: A group that is the target of a copy operation can be the source of another copy operation at the same time.

Multi-hop elements must have same SyncType: The SyncType of each hop must be the same as previous hop, e.g., mirror, snapshot, clone.

Group can only have one single relationship active: Only one StorageSynchronized association within a group can be active at a given time.

Source element can be removed from group: A source element can be removed even when the group is associated with another replication group.

Target element can be removed from group: A target element can be removed even when the group is associated with another replication group.

Group can be temporary: Group can have a persistence of false, which means the group -- not its elements, may be deleted if it no longer participates in a replication operation.

Group is nameable: In creating a group, it is possible to name the group.

Supports target element count: It is possible to supply one source element and request more than one target element copies.

Synchronized clone target detaches automatically: The clone target group detaches automatically when the target group becomes synchronized; otherwise, the client needs to explicitly request a detach operation.

Reverse Roles operation requires Read Only source: The Reverse Roles operation requires the source element to be in the Read Only mode.

Reverse Roles operation requires resync: For the copy operation to continue, resync of source and target elements is required.

Restore operation requires fracture: The copy operation has completed; however, the synchronization relationship must be fractured.

Resync operation requires activate: For the copy operation to continue, the synchronization relationship must be activated.

Copy operation requires offline source: Instrumentation requires the source element to be offline (not-ready) to ensure data does not change before starting the copy operation.

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

<span id="Multi-hop_elements_must_have_same_SyncType"></span><span id="multi-hop_elements_must_have_same_synctype"></span><span id="MULTI-HOP_ELEMENTS_MUST_HAVE_SAME_SYNCTYPE"></span>

**Multi-hop elements must have same SyncType** (9)


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


</dt> <dd>22–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> </dl>

## Return value

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

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





