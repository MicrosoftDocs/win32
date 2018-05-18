---
title: GetSupportedWaitForCopyStates method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the copy states that are valid in the WaitForCopyState parameter of the specified method for a specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b9e6b222-2315-48cb-a021-9eece9f089b4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedWaitForCopyStates method iSCSI Software Target API", "GetSupportedWaitForCopyStates method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedWaitForCopyStates method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedWaitForCopyStates
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSupportedWaitForCopyStates method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the copy states that are valid in the *WaitForCopyState* parameter of the specified method for a specified replication type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedWaitForCopyStates(
  [in]  uint16 ReplicationType,
  [in]  uint16 MethodName,
  [out] uint16 SupportedCopyStates[]
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

*MethodName* \[in\]
</dt> <dd>

Specifies the method name.

The possible values are.

<dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>

**CreateElementReplica** (2)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>

**CreateGroupReplica** (3)


</dt> <dd></dd> <dt>

<span id="ModifyReplicaSynchronization"></span><span id="modifyreplicasynchronization"></span><span id="MODIFYREPLICASYNCHRONIZATION"></span>

**ModifyReplicaSynchronization** (4)


</dt> <dd></dd> <dt>

<span id="ModifyListSynchronization"></span><span id="modifylistsynchronization"></span><span id="MODIFYLISTSYNCHRONIZATION"></span>

**ModifyListSynchronization** (5)


</dt> <dd></dd> <dt>

<span id="ModifySettingsDefineState"></span><span id="modifysettingsdefinestate"></span><span id="MODIFYSETTINGSDEFINESTATE"></span>

**ModifySettingsDefineState** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>7–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SupportedCopyStates* \[out\]
</dt> <dd>

On return, contains the list of supported copy states.

The **CIM\_Synchronized.CopyState** property values are.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span>

**Unsynchronized** (3)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (4)


</dt> <dd></dd> <dt>

<span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span>

**Broken** (5)


</dt> <dd></dd> <dt>

<span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span>

**Fractured** (6)


</dt> <dd></dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

**Split** (7)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (8)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** (9)


</dt> <dd></dd> <dt>

<span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span>

**Failedover** (10)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (11)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (12)


</dt> <dd></dd> <dt>

<span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span>

**Skewed** (13)


</dt> <dd></dd> <dt>

<span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>

**Mixed** (14)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (15)


</dt> <dd></dd> <dt>

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>

**Partitioned** (16)


</dt> <dd></dd> <dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

**Invalid** (17)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>18–0x7FFF</dd> <dt>

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

 

 





