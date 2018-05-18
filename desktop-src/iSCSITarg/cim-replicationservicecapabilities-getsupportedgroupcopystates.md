---
title: GetSupportedGroupCopyStates method of the CIM\_ReplicationServiceCapabilities class
description: This method, for a given ReplicationType, returns the supported replication group CopyStates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f73fafeb-b94d-4cd1-ba0f-8e7dee4df3ba'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedGroupCopyStates method iSCSI Software Target API", "GetSupportedGroupCopyStates method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedGroupCopyStates method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedGroupCopyStates
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedGroupCopyStates method of the CIM\_ReplicationServiceCapabilities class

This method, for a given ReplicationType, returns the supported replication group CopyStates.

## Syntax


```mof
uint32 GetSupportedGroupCopyStates(
  [in]  uint16 ReplicationType,
  [out] uint16 SupportedCopyStates[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

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

 

 





