---
title: FormatError method of the Msvm\_VirtualSystemManagementService class
description: Retrieves a formatted error message for an array of Msvm\_Error instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d177abc-c19c-4e3e-9d0f-a1524c6e6900
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- FormatError method
- FormatError method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, FormatError method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.FormatError
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FormatError method of the Msvm\_VirtualSystemManagementService class

Retrieves a formatted error message for an array of [**Msvm\_Error**](msvm-error.md) instances.

## Syntax


```mof
uint32 FormatError(
  [in]  string Errors[],
  [out] string ErrorMessage
);
```



## Parameters

<dl> <dt>

*Errors* \[in\]
</dt> <dd>

An array that contains the [**Msvm\_Error**](msvm-error.md) instances.

</dd> <dt>

*ErrorMessage* \[out\]
</dt> <dd>

The retrieved formatted error message.

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

 

 





