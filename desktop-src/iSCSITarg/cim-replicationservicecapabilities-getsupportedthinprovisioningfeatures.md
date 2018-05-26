---
title: GetSupportedThinProvisioningFeatures method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType returns the supported features related to thin provisioning.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 030fc9fd-ada9-4033-99fb-a0c5d5dbfa4e
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedThinProvisioningFeatures method iSCSI Software Target API
- GetSupportedThinProvisioningFeatures method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedThinProvisioningFeatures method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedThinProvisioningFeatures
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedThinProvisioningFeatures method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType returns the supported features related to thin provisioning.

## Syntax


```mof
uint32 GetSupportedThinProvisioningFeatures(
  [in]  uint16 ReplicationType,
  [out] uint16 SupportedThinProvisioningFeatures[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*SupportedThinProvisioningFeatures* \[out\]
</dt> <dd>

An array of Supported Thin Provisioning Features.

Thin provisioning is not supported: Feature is unavailable.

Zeros written in unused allocated blocks of target: In copying thin to full, the unused blocks of target will be written with zeros.

Unused allocated blocks of target are not initialized: In copying thin to full, the unused blocks of target will remain uninitialized.

See the property ReplicationSettingData.ThinProvisioningPolicy for a list of possible options for a copy operation.

<dt>

<span id="Thin_provisioning_is_not_supported"></span><span id="thin_provisioning_is_not_supported"></span><span id="THIN_PROVISIONING_IS_NOT_SUPPORTED"></span>

**Thin provisioning is not supported** (1)


</dt> <dd></dd> <dt>

<span id="Zeros_written_in_unused_allocated_blocks_of_target"></span><span id="zeros_written_in_unused_allocated_blocks_of_target"></span><span id="ZEROS_WRITTEN_IN_UNUSED_ALLOCATED_BLOCKS_OF_TARGET"></span>

**Zeros written in unused allocated blocks of target** (2)


</dt> <dd></dd> <dt>

<span id="Unused_allocated_blocks_of_target_are_not_initialized"></span><span id="unused_allocated_blocks_of_target_are_not_initialized"></span><span id="UNUSED_ALLOCATED_BLOCKS_OF_TARGET_ARE_NOT_INITIALIZED"></span>

**Unused allocated blocks of target are not initialized** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

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

 

 





