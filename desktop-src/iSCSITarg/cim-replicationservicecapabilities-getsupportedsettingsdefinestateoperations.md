---
title: GetSupportedSettingsDefineStateOperations method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType returns the supported Operations on a SettingsDefineState association that can be supplied to the ModifySettingsDefineState method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ee300560-31dc-460a-b0f0-def55755f0e5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedSettingsDefineStateOperations method iSCSI Software Target API", "GetSupportedSettingsDefineStateOperations method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedSettingsDefineStateOperations method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedSettingsDefineStateOperations
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedSettingsDefineStateOperations method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType returns the supported Operations on a SettingsDefineState association that can be supplied to the ModifySettingsDefineState method.

## Syntax


```mof
uint32 GetSupportedSettingsDefineStateOperations(
  [in]  uint16 ReplicationType,
  [out] uint16 SupportedOperations[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*SupportedOperations* \[out\]
</dt> <dd>

An array of supported Operations. /nActivate Consistency: Enable consistency Deactivate Consistency: Disable consistency Delete: Remove the SettingsDefineState association. Instance of SynchronizationAspect may also be deleted if it is not shared with other elements. Copy To Target: Introduces the target elements and forms the necessary associations between the source and the target elements i.e. StorageSynchronized and GroupSynchronized.

<dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

**Activate Consistency** (2)


</dt> <dd></dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

**Deactivate Consistency** (3)


</dt> <dd></dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>

**Delete** (4)


</dt> <dd></dd> <dt>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>

**Copy To Target** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

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

 

 





