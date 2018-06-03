---
title: GetSizeOfSystemFiles method of the Msvm\_VirtualSystemManagementService class
description: Retrieves the total size of the system files for a virtual system or for a virtual system snapshot. The results include configuration and saved state files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b62da53b-f831-44c4-823a-b64587094c7a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSizeOfSystemFiles method
- GetSizeOfSystemFiles method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, GetSizeOfSystemFiles method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetSizeOfSystemFiles
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSizeOfSystemFiles method of the Msvm\_VirtualSystemManagementService class

Retrieves the total size of the system files for a virtual system or for a virtual system snapshot. The results include configuration and saved state files.

## Syntax


```mof
uint32 GetSizeOfSystemFiles(
  [in]  CIM_VirtualSystemSettingData REF Vssd,
  [out] uint64                           Size
);
```



## Parameters

<dl> <dt>

*Vssd* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that contains the system files to retrieve.

</dd> <dt>

*Size* \[out\]
</dt> <dd>

The total size of system files.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





