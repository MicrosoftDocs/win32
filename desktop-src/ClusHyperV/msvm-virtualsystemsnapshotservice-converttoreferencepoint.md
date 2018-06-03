---
title: ConvertToReferencePoint method of the Msvm\_VirtualSystemSnapshotService class
description: Converts a virtual machine snapshot to a reference point.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7f1b6aba-585b-464b-8800-5a215473ec5e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertToReferencePoint method
- ConvertToReferencePoint method, Msvm_VirtualSystemSnapshotService class
- Msvm_VirtualSystemSnapshotService class, ConvertToReferencePoint method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSnapshotService.ConvertToReferencePoint
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertToReferencePoint method of the Msvm\_VirtualSystemSnapshotService class

Converts a virtual machine snapshot to a reference point.

## Syntax


```mof
uint32 ConvertToReferencePoint(
  [in]      CIM_VirtualSystemSettingData     REF AffectedSnapshot,
  [in]      string                               ReferencePointSettings,
  [in, out] Msvm_VirtualSystemReferencePoint REF ResultingReferencePoint,
  [out]     CIM_ConcreteJob                  REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshot* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that represents the virtual machine snapshot.

</dd> <dt>

*ReferencePointSettings* \[in\]
</dt> <dd>

An embedded instance of the [**CIM\_SettingData**](cim-settingdata.md) class that contains the parameter settings for the reference point. This parameter is optional and may be an empty string.

</dd> <dt>

*ResultingReferencePoint* \[in, out\]
</dt> <dd>

A reference to the [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md) instance that represents the new reference point.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Invalid Type** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





