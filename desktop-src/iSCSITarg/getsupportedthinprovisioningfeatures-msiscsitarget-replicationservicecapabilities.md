---
title: GetSupportedThinProvisioningFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the supported features that are related to thin provisioning for a specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6903f65b-7daa-498b-b668-27911103277a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedThinProvisioningFeatures method iSCSI Software Target API", "GetSupportedThinProvisioningFeatures method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedThinProvisioningFeatures method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedThinProvisioningFeatures
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSupportedThinProvisioningFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the supported features that are related to thin provisioning for a specified replication type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedThinProvisioningFeatures(
  [in]  uint16 ReplicationType,
  [out] uint16 SupportedThinProvisioningFeatures[]
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

*SupportedThinProvisioningFeatures* \[out\]
</dt> <dd>

On return, contains the list of supported thin provisioning features. For a list of possible options for a copy operation, see the **CIM\_ReplicationSettingData.ThinProvisioningPolicy** property on the [DMTF](http://schemas.dmtf.org/wbem/cim-html/2.31.0+/CIM_ReplicationSettingData.mdl) website at http://schemas.dmtf.org/wbem/cim-html/2.31.0+/CIM\_ReplicationSettingData.html.

The possible values are.

<dt>

<span id="Thin_provisioning_is_not_supported"></span><span id="thin_provisioning_is_not_supported"></span><span id="THIN_PROVISIONING_IS_NOT_SUPPORTED"></span>

<span id="Thin_provisioning_is_not_supported"></span><span id="thin_provisioning_is_not_supported"></span><span id="THIN_PROVISIONING_IS_NOT_SUPPORTED"></span>**Thin provisioning is not supported** (1)


</dt> <dd>

The feature is unavailable.

</dd> <dt>

<span id="Zeros_written_in_unused_allocated_blocks_of_target"></span><span id="zeros_written_in_unused_allocated_blocks_of_target"></span><span id="ZEROS_WRITTEN_IN_UNUSED_ALLOCATED_BLOCKS_OF_TARGET"></span>

<span id="Zeros_written_in_unused_allocated_blocks_of_target"></span><span id="zeros_written_in_unused_allocated_blocks_of_target"></span><span id="ZEROS_WRITTEN_IN_UNUSED_ALLOCATED_BLOCKS_OF_TARGET"></span>**Zeros written in unused allocated blocks of target** (2)


</dt> <dd>

In copying thin to full, the unused blocks of target element are written with zeros.

</dd> <dt>

<span id="Unused_allocated_blocks_of_target_are_not_initialized"></span><span id="unused_allocated_blocks_of_target_are_not_initialized"></span><span id="UNUSED_ALLOCATED_BLOCKS_OF_TARGET_ARE_NOT_INITIALIZED"></span>

<span id="Unused_allocated_blocks_of_target_are_not_initialized"></span><span id="unused_allocated_blocks_of_target_are_not_initialized"></span><span id="UNUSED_ALLOCATED_BLOCKS_OF_TARGET_ARE_NOT_INITIALIZED"></span>**Unused allocated blocks of target are not initialized** (3)


</dt> <dd>

In copying thin to full, the unused blocks of target element remain uninitialized.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> </dl>

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
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





