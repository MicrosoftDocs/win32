---
title: GetSupportedCopyStates method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType returns the supported CopyStates and a parallel array to indicate for a given CopyState the target element is host accessible or not.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79f16522-207c-45d0-b923-c2fc5be76dbb
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedCopyStates method iSCSI Software Target API
- GetSupportedCopyStates method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedCopyStates method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedCopyStates
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedCopyStates method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType returns the supported CopyStates and a parallel array to indicate for a given CopyState the target element is host accessible or not.

## Syntax


```mof
uint32 GetSupportedCopyStates(
  [in]  uint16  ReplicationType,
  [out] uint16  SupportedCopyStates[],
  [out] boolean HostAccessible[]
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

</dd> <dt>

*HostAccessible* \[out\]
</dt> <dd>

A parallel array to SupportedCopyStates\[\] to indicate whether in that CopyState the target element is host accessible or not (true or false)

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

 

 





