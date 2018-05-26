---
title: GetSupportedWaitForCopyStates method of the CIM\_ReplicationServiceCapabilities class
description: This method, for a given ReplicationType and method, returns the supported CopyStates that can be specified in the methods WaitForCopyState parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 29acefdf-7bfc-4744-818c-39d350547de9
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedWaitForCopyStates method iSCSI Software Target API
- GetSupportedWaitForCopyStates method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedWaitForCopyStates method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedWaitForCopyStates
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedWaitForCopyStates method of the CIM\_ReplicationServiceCapabilities class

This method, for a given ReplicationType and method, returns the supported CopyStates that can be specified in the method's WaitForCopyState parameter.

## Syntax


```mof
uint32 GetSupportedWaitForCopyStates(
  [in]  uint16 ReplicationType,
  [in]  uint16 MethodName,
  [out] uint16 SupportedCopyStates[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*MethodName* \[in\]
</dt> <dd>

A value representing the desired method name.

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


</dt> <dd>7 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SupportedCopyStates* \[out\]
</dt> <dd>

Supported Copy States.

</dd> </dl>

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

 

 





