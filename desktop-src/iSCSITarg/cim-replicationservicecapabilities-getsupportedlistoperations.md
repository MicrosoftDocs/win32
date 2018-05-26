---
title: GetSupportedListOperations method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType returns the supported Operations on a list of StorageSynchronized or GroupSynchronized associations that can be supplied to the ModifyListSynchronization method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b2c64784-9758-4359-af7c-5c470faea415
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedListOperations method iSCSI Software Target API
- GetSupportedListOperations method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedListOperations method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedListOperations
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedListOperations method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType returns the supported Operations on a list of StorageSynchronized or GroupSynchronized associations that can be supplied to the ModifyListSynchronization method.

## Syntax


```mof
uint32 GetSupportedListOperations(
  [in]  uint16 ReplicationType,
  [in]  uint16 SynchronizationType,
  [out] uint16 SupportedListOperations[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*SynchronizationType* \[in\]
</dt> <dd>

Specifies the supported operations as they apply to a list of StorageSynchronized or GroupSynchronized. If this parameter is not specified, StorageSynchronized is assumed.

<dt>

<span id="StorageSynchronized"></span><span id="storagesynchronized"></span><span id="STORAGESYNCHRONIZED"></span>

**StorageSynchronized** (2)


</dt> <dd></dd> <dt>

<span id="GroupSynchronized"></span><span id="groupsynchronized"></span><span id="GROUPSYNCHRONIZED"></span>

**GroupSynchronized** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SupportedListOperations* \[out\]
</dt> <dd>

An array of Supported group Operations. Abort: Abort the copy operation if it is possible.

Activate: Activate an inactive or prepared source and target association.

Deactivate: Deactivate a source and target association. The writes to the target are deleted in the case of a snapshot.

Detach: Remove the association between source and target.

Dissolve: Dissolve the synchronization between two storage objects, however, the target element continues to exist.

Failover: Switch to target element instead of source.

Failback: Reverses the effects of failover.

Fracture: Separate target element from source element.

Resync Replica: Synchronize a fractured/split source and target elements.

Restore from Replica: Copy data from a fractured target back to source.

Resume: Continue an association that was suspended.

Reset To Sync: Change mode to synchronous.

Reset To Async: Change mode to asynchronous.

Reverse Roles: Make target the source and source the target.

Return To ResourcePool: Applies to Snapshot -- delete the target element and its replication association.

Split: Similar to Fracture, however, the provider needs to make sure wether there are pending I/O in transit before fracturing the connection.

Suspend: Stop the copy operations to the target element.

Continue when the operations is resumed.

Unprepare: Causes the synchronization to be reinitialized and stop in Prepared state.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

**Abort** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (3)


</dt> <dd></dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

**Activate** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (6)


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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (13)


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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>24 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

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

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





